"""
Reproducible LLM-assisted annotation pipeline for Phase 2 analysis.

This script performs codebook-guided annotation of translation examples,
including difficulty scoring, linguistic phenomena tagging, and trace analysis.

Usage:
    python analysis/annotate_dataset.py \
        --input_file path/to/phase2_dataset.jsonl \
        --output_file path/to/annotated_dataset.jsonl \
        --annotation_model google/gemma-2-9b-it \
        --batch_size 8 \
        --sample_size 100
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from analysis.phase2_utils import load_jsonl, write_jsonl


def parse_args():
    parser = argparse.ArgumentParser(
        description="LLM-assisted annotation pipeline for Phase 2 analysis"
    )
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="Input JSONL file (phase2_dataset.jsonl)",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        required=True,
        help="Output JSONL file for annotations",
    )
    parser.add_argument(
        "--annotation_model",
        type=str,
        default="google/gemma-2-9b-it",
        help="HuggingFace model for annotation (default: google/gemma-2-9b-it)",
    )
    parser.add_argument(
        "--model_revision",
        type=str,
        default=None,
        help="Specific model revision/commit hash for reproducibility",
    )
    parser.add_argument(
        "--prompt_template",
        type=str,
        default="analysis/annotation_prompt_v1.txt",
        help="Path to annotation prompt template",
    )
    parser.add_argument(
        "--codebook_version",
        type=str,
        default="v1.0",
        help="Codebook version used for annotation",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature (use 0.0 for deterministic)",
    )
    parser.add_argument(
        "--max_new_tokens",
        type=int,
        default=512,
        help="Maximum tokens for annotation response",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=8,
        help="Batch size for inference",
    )
    parser.add_argument(
        "--sample_size",
        type=int,
        default=None,
        help="Number of examples to annotate (None = all)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for sampling",
    )
    parser.add_argument(
        "--annotator_id",
        type=str,
        default="RC",
        help="Annotator identifier",
    )
    parser.add_argument(
        "--inference_api",
        type=str,
        default="hf",
        choices=["hf", "vllm"],
        help="Inference API to use",
    )
    parser.add_argument(
        "--device",
        type=str,
        default=None,
        help="Device for inference (cuda, cpu, mps)",
    )
    parser.add_argument(
        "--save_raw_outputs",
        action="store_true",
        help="Save raw model outputs before parsing",
    )
    parser.add_argument(
        "--manual_mode",
        action="store_true",
        help="Manual annotation mode (no LLM, interactive input)",
    )
    return parser.parse_args()


def load_prompt_template(template_path: str) -> str:
    """Load the annotation prompt template."""
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()


def format_prompt(
    template: str,
    example: Dict[str, Any],
    source_lang: str = "English",
    target_lang: str = "Xhosa",
) -> str:
    """Format the prompt with example data."""
    source_sentence = example.get("source_sentence", "")
    reference_translation = example.get("reference_translation", "")
    model_translation = example.get("model_translation", "")
    reasoning_trace = example.get("reasoning_trace", "")
    
    if reasoning_trace is None or reasoning_trace == "":
        reasoning_trace = "[No reasoning trace provided]"
    
    prompt = template.format(
        source_language=source_lang,
        target_language=target_lang,
        source_sentence=source_sentence,
        reference_translation=reference_translation,
        model_translation=model_translation,
        reasoning_trace=reasoning_trace,
    )
    return prompt


def parse_annotation_response(response: str) -> Optional[Dict[str, Any]]:
    """Parse JSON annotation from model response."""
    try:
        # Try to find JSON block in response
        response = response.strip()
        
        # Remove markdown code blocks if present
        if response.startswith("```json"):
            response = response[7:]
        if response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]
        
        response = response.strip()
        
        # Parse JSON
        annotation = json.loads(response)
        return annotation
    except json.JSONDecodeError as e:
        print(f"Warning: Failed to parse JSON response: {e}")
        print(f"Response was: {response[:200]}...")
        return None


def create_annotation_metadata(args) -> Dict[str, Any]:
    """Create metadata object for annotation provenance."""
    return {
        "annotation_model_name": args.annotation_model,
        "annotation_model_revision": args.model_revision or "default",
        "annotation_prompt_version": os.path.basename(args.prompt_template),
        "annotation_codebook_version": args.codebook_version,
        "annotation_date": datetime.utcnow().isoformat(),
        "annotation_temperature": args.temperature,
        "annotation_seed": args.seed,
        "annotation_max_new_tokens": args.max_new_tokens,
        "annotator_id": args.annotator_id,
        "inference_api": args.inference_api,
    }


def annotate_with_hf(
    prompts: List[str],
    model_name: str,
    model_revision: Optional[str],
    temperature: float,
    max_new_tokens: int,
    device: Optional[str],
) -> List[str]:
    """Annotate using HuggingFace transformers."""
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError as exc:
        raise RuntimeError(
            "HuggingFace annotation requires torch and transformers."
        ) from exc
    
    # Load model and tokenizer
    print(f"Loading model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(
        model_name, revision=model_revision
    )
    
    if device is None:
        if torch.cuda.is_available():
            device = "cuda"
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            device = "mps"
        else:
            device = "cpu"
    
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        revision=model_revision,
        torch_dtype=torch.bfloat16 if device == "cuda" else torch.float32,
        device_map=device if device == "cuda" else None,
    )
    
    if device != "cuda":
        model = model.to(device)
    
    model.eval()
    
    # Generate annotations
    responses = []
    for prompt in prompts:
        # Apply chat template if available
        if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template:
            messages = [{"role": "user", "content": prompt}]
            formatted_prompt = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        else:
            formatted_prompt = prompt
        
        inputs = tokenizer(
            formatted_prompt, return_tensors="pt", truncation=True, max_length=2048
        ).to(device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature if temperature > 0 else None,
                do_sample=temperature > 0,
                pad_token_id=tokenizer.eos_token_id,
            )
        
        # Decode response
        response = tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        )
        responses.append(response)
    
    return responses


def annotate_with_vllm(
    prompts: List[str],
    model_name: str,
    model_revision: Optional[str],
    temperature: float,
    max_new_tokens: int,
) -> List[str]:
    """Annotate using vLLM for faster batch inference."""
    try:
        from vllm import LLM, SamplingParams
    except ImportError as exc:
        raise RuntimeError("vLLM annotation requires vllm package.") from exc
    
    print(f"Loading model with vLLM: {model_name}")
    llm = LLM(model=model_name, revision=model_revision, trust_remote_code=True)
    
    sampling_params = SamplingParams(
        temperature=temperature,
        max_tokens=max_new_tokens,
        top_p=1.0,
    )
    
    outputs = llm.generate(prompts, sampling_params)
    responses = [output.outputs[0].text for output in outputs]
    
    return responses


def manual_annotation_interactive(example: Dict[str, Any]) -> Dict[str, Any]:
    """Interactive manual annotation (for pilot or audit)."""
    print("\n" + "=" * 80)
    print("SOURCE SENTENCE:")
    print(example.get("source_sentence", ""))
    print("\nREFERENCE TRANSLATION:")
    print(example.get("reference_translation", ""))
    print("\nMODEL TRANSLATION:")
    print(example.get("model_translation", ""))
    
    trace = example.get("reasoning_trace", "")
    if trace:
        print("\nREASONING TRACE:")
        print(trace[:500] + "..." if len(trace) > 500 else trace)
    
    print("\n" + "=" * 80)
    
    # Difficulty
    print("\nDIFFICULTY SCORE (1-5):")
    difficulty_score = int(input("Score: ").strip())
    difficulty_justification = input("Justification: ").strip()
    
    # Linguistic phenomena
    print("\nLINGUISTIC PHENOMENA (y/n for each):")
    phenomena = {}
    for p in ["ambiguity", "idiom", "complex_syntax", "named_entities",
              "figurative_language", "long_distance_dependency"]:
        response = input(f"{p}: ").strip().lower()
        phenomena[p] = response in ["y", "yes", "true", "1"]
    
    # Trace analysis
    trace_analysis = None
    if trace:
        print("\nTRACE ANALYSIS:")
        primary_type = input("Primary type (CORRECT_LINGUISTIC_ANALYSIS, HALLUCINATED_RULE, VACUOUS_FILLER, TRANSLATION_ATTEMPT, REPETITION): ").strip()
        secondary_types = input("Secondary types (comma-separated, or empty): ").strip()
        secondary_types = [t.strip() for t in secondary_types.split(",")] if secondary_types else []
        usefulness = input("Usefulness (helpful/neutral/harmful): ").strip()
        overlap = input("Overlap (none/low/medium/high): ").strip()
        length_tokens = int(input("Length (tokens): ").strip())
        
        trace_analysis = {
            "primary_trace_type": primary_type,
            "secondary_trace_types": secondary_types,
            "usefulness": usefulness,
            "overlap": overlap,
            "length_tokens": length_tokens,
        }
    
    return {
        "difficulty": {
            "score": difficulty_score,
            "justification": difficulty_justification,
        },
        "linguistic_phenomena": phenomena,
        "trace_analysis": trace_analysis,
    }


def main():
    args = parse_args()
    
    # Load input data
    print(f"Loading input data from {args.input_file}")
    examples = load_jsonl(args.input_file)
    
    # Sample if requested
    if args.sample_size is not None and args.sample_size < len(examples):
        import random
        random.seed(args.seed)
        examples = random.sample(examples, args.sample_size)
        print(f"Sampled {args.sample_size} examples")
    
    print(f"Annotating {len(examples)} examples")
    
    # Load prompt template
    prompt_template = load_prompt_template(args.prompt_template)
    
    # Create annotation metadata
    annotation_metadata = create_annotation_metadata(args)
    
    # Prepare output
    annotated_examples = []
    raw_outputs = []
    
    if args.manual_mode:
        # Manual annotation
        print("\n=== MANUAL ANNOTATION MODE ===")
        for i, example in enumerate(examples):
            print(f"\n[{i+1}/{len(examples)}]")
            annotation = manual_annotation_interactive(example)
            
            annotated_example = {
                "example_id": example.get("example_id"),
                **annotation,
                "annotation_metadata": {**annotation_metadata, "method": "manual"},
            }
            annotated_examples.append(annotated_example)
    else:
        # LLM-assisted annotation
        # Format prompts
        prompts = []
        for example in examples:
            metadata = example.get("metadata", {})
            source_lang = metadata.get("source_language", "English")
            target_lang = metadata.get("target_language", "Xhosa")
            prompt = format_prompt(prompt_template, example, source_lang, target_lang)
            prompts.append(prompt)
        
        # Generate annotations
        print(f"Generating annotations with {args.annotation_model}")
        if args.inference_api == "vllm":
            responses = annotate_with_vllm(
                prompts,
                args.annotation_model,
                args.model_revision,
                args.temperature,
                args.max_new_tokens,
            )
        else:  # hf
            responses = annotate_with_hf(
                prompts,
                args.annotation_model,
                args.model_revision,
                args.temperature,
                args.max_new_tokens,
                args.device,
            )
        
        # Parse and save annotations
        for i, (example, response) in enumerate(zip(examples, responses)):
            raw_outputs.append({
                "example_id": example.get("example_id"),
                "raw_response": response,
            })
            
            annotation = parse_annotation_response(response)
            
            if annotation is None:
                print(f"Warning: Failed to parse annotation for example {i}")
                # Create placeholder
                annotation = {
                    "difficulty": {"score": None, "justification": "PARSE_ERROR"},
                    "linguistic_phenomena": {},
                    "trace_analysis": None,
                    "parse_error": True,
                }
            
            annotated_example = {
                "example_id": example.get("example_id"),
                **annotation,
                "annotation_metadata": annotation_metadata,
            }
            annotated_examples.append(annotated_example)
    
    # Save annotations
    write_jsonl(args.output_file, annotated_examples)
    print(f"Wrote {len(annotated_examples)} annotations to {args.output_file}")
    
    # Save raw outputs if requested
    if args.save_raw_outputs and not args.manual_mode:
        raw_output_file = args.output_file.replace(".jsonl", "_raw.jsonl")
        write_jsonl(raw_output_file, raw_outputs)
        print(f"Wrote raw outputs to {raw_output_file}")
    
    # Save annotation metadata
    metadata_file = args.output_file.replace(".jsonl", "_metadata.json")
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(annotation_metadata, f, indent=2)
    print(f"Wrote annotation metadata to {metadata_file}")
    
    # Print summary statistics
    print("\n=== ANNOTATION SUMMARY ===")
    if not args.manual_mode:
        parse_errors = sum(1 for ex in annotated_examples if ex.get("parse_error"))
        print(f"Parse errors: {parse_errors}/{len(annotated_examples)}")
    
    valid_annotations = [ex for ex in annotated_examples if not ex.get("parse_error")]
    if valid_annotations:
        difficulty_scores = [
            ex["difficulty"]["score"]
            for ex in valid_annotations
            if ex["difficulty"]["score"] is not None
        ]
        if difficulty_scores:
            print(f"Average difficulty: {sum(difficulty_scores) / len(difficulty_scores):.2f}")
        
        trace_analysis_count = sum(
            1 for ex in valid_annotations if ex.get("trace_analysis") is not None
        )
        print(f"Examples with trace analysis: {trace_analysis_count}/{len(valid_annotations)}")


if __name__ == "__main__":
    main()
