"""
Generate descriptive analysis tables and statistics from annotated datasets.

This script produces the Phase 2 analysis deliverables including:
- Trace type frequency tables
- Trace usefulness vs. translation quality correlations
- Difficulty distribution
- Linguistic phenomena frequencies
- Cross-tabulations by model, prompt type, language pair

Usage:
    python analysis/analyze_traces.py \
        --annotated_file annotated_dataset.jsonl \
        --output_dir analysis_results/
"""

import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from typing import Any, Dict, List

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from analysis.phase2_utils import load_jsonl


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate Phase 2 analysis tables from annotated data"
    )
    parser.add_argument(
        "--annotated_file",
        type=str,
        required=True,
        help="Input annotated JSONL file",
    )
    parser.add_argument(
        "--phase2_file",
        type=str,
        help="Original phase2_dataset.jsonl for joining metadata/scores",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="analysis_results",
        help="Output directory for analysis tables",
    )
    return parser.parse_args()


def load_and_join_data(annotated_file: str, phase2_file: str = None) -> List[Dict[str, Any]]:
    """Load annotated data and optionally join with phase2 metadata."""
    annotations = load_jsonl(annotated_file)
    
    if phase2_file and os.path.exists(phase2_file):
        phase2_data = {ex["example_id"]: ex for ex in load_jsonl(phase2_file)}
        
        # Join annotations with phase2 metadata
        joined = []
        for ann in annotations:
            example_id = ann.get("example_id")
            if example_id in phase2_data:
                joined.append({**phase2_data[example_id], "annotation": ann})
            else:
                joined.append({"annotation": ann})
        return joined
    else:
        return [{"annotation": ann} for ann in annotations]


def compute_difficulty_distribution(data: List[Dict[str, Any]]) -> Dict[int, int]:
    """Compute frequency of each difficulty score."""
    scores = [
        ex["annotation"]["difficulty"]["score"]
        for ex in data
        if ex["annotation"].get("difficulty", {}).get("score") is not None
    ]
    return dict(Counter(scores))


def compute_phenomena_frequencies(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """Compute frequency of each linguistic phenomenon."""
    phenomena_counts = defaultdict(int)
    total = 0
    
    for ex in data:
        phenomena = ex["annotation"].get("linguistic_phenomena", {})
        if phenomena:
            total += 1
            for p, present in phenomena.items():
                if present:
                    phenomena_counts[p] += 1
    
    return dict(phenomena_counts), total


def compute_trace_type_distribution(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """Compute frequency of primary trace types."""
    trace_types = [
        ex["annotation"]["trace_analysis"]["primary_trace_type"]
        for ex in data
        if ex["annotation"].get("trace_analysis") is not None
        and ex["annotation"]["trace_analysis"].get("primary_trace_type") is not None
    ]
    return dict(Counter(trace_types))


def compute_usefulness_distribution(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """Compute frequency of trace usefulness categories."""
    usefulness = [
        ex["annotation"]["trace_analysis"]["usefulness"]
        for ex in data
        if ex["annotation"].get("trace_analysis") is not None
        and ex["annotation"]["trace_analysis"].get("usefulness") is not None
    ]
    return dict(Counter(usefulness))


def compute_overlap_distribution(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """Compute frequency of trace-translation overlap categories."""
    overlap = [
        ex["annotation"]["trace_analysis"]["overlap"]
        for ex in data
        if ex["annotation"].get("trace_analysis") is not None
        and ex["annotation"]["trace_analysis"].get("overlap") is not None
    ]
    return dict(Counter(overlap))


def cross_tabulate(
    data: List[Dict[str, Any]], row_key: str, col_key: str
) -> Dict[tuple, int]:
    """Create cross-tabulation of two categorical variables."""
    crosstab = defaultdict(int)
    
    for ex in data:
        ann = ex["annotation"]
        metadata = ex.get("metadata", {})
        
        # Extract row value
        if row_key == "difficulty":
            row_val = ann.get("difficulty", {}).get("score")
        elif row_key == "primary_trace_type":
            row_val = ann.get("trace_analysis", {}).get("primary_trace_type")
        elif row_key == "usefulness":
            row_val = ann.get("trace_analysis", {}).get("usefulness")
        elif row_key in metadata:
            row_val = metadata[row_key]
        else:
            row_val = None
        
        # Extract column value
        if col_key == "difficulty":
            col_val = ann.get("difficulty", {}).get("score")
        elif col_key == "primary_trace_type":
            col_val = ann.get("trace_analysis", {}).get("primary_trace_type")
        elif col_key == "usefulness":
            col_val = ann.get("trace_analysis", {}).get("usefulness")
        elif col_key in metadata:
            col_val = metadata[col_key]
        else:
            col_val = None
        
        if row_val is not None and col_val is not None:
            crosstab[(row_val, col_val)] += 1
    
    return dict(crosstab)


def compute_quality_correlation(
    data: List[Dict[str, Any]], metric: str = "sentence_bleu"
) -> Dict[str, List[float]]:
    """Compute average quality scores by trace characteristics."""
    quality_by_usefulness = defaultdict(list)
    quality_by_type = defaultdict(list)
    quality_by_overlap = defaultdict(list)
    
    for ex in data:
        scores = ex.get("metadata", {}).get("evaluation_scores", {})
        quality = scores.get(metric)
        
        if quality is None:
            continue
        
        trace = ex["annotation"].get("trace_analysis")
        if trace is None:
            continue
        
        usefulness = trace.get("usefulness")
        if usefulness:
            quality_by_usefulness[usefulness].append(quality)
        
        trace_type = trace.get("primary_trace_type")
        if trace_type:
            quality_by_type[trace_type].append(quality)
        
        overlap = trace.get("overlap")
        if overlap:
            quality_by_overlap[overlap].append(quality)
    
    return {
        "usefulness": {k: sum(v)/len(v) for k, v in quality_by_usefulness.items()},
        "trace_type": {k: sum(v)/len(v) for k, v in quality_by_type.items()},
        "overlap": {k: sum(v)/len(v) for k, v in quality_by_overlap.items()},
    }


def write_markdown_table(filepath: str, title: str, table_data: Dict[Any, Any]):
    """Write a simple markdown table."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write("| Category | Count |\n")
        f.write("|----------|-------|\n")
        for key, value in sorted(table_data.items()):
            f.write(f"| {key} | {value} |\n")


def write_crosstab_markdown(filepath: str, title: str, crosstab: Dict[tuple, int]):
    """Write a crosstab as markdown table."""
    if not crosstab:
        return
    
    # Get unique row and column values
    rows = sorted(set(k[0] for k in crosstab.keys()))
    cols = sorted(set(k[1] for k in crosstab.keys()))
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        
        # Header
        f.write("|  | " + " | ".join(str(c) for c in cols) + " |\n")
        f.write("|" + "---|" * (len(cols) + 1) + "\n")
        
        # Rows
        for row in rows:
            f.write(f"| {row} | ")
            f.write(" | ".join(str(crosstab.get((row, col), 0)) for col in cols))
            f.write(" |\n")


def main():
    args = parse_args()
    
    # Load data
    print(f"Loading annotated data from {args.annotated_file}")
    data = load_and_join_data(args.annotated_file, args.phase2_file)
    print(f"Loaded {len(data)} examples")
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Compute statistics
    print("\nComputing statistics...")
    
    # 1. Difficulty distribution
    difficulty_dist = compute_difficulty_distribution(data)
    write_markdown_table(
        os.path.join(args.output_dir, "difficulty_distribution.md"),
        "Difficulty Distribution",
        difficulty_dist,
    )
    print(f"Difficulty distribution: {difficulty_dist}")
    
    # 2. Linguistic phenomena
    phenomena_freq, phenomena_total = compute_phenomena_frequencies(data)
    write_markdown_table(
        os.path.join(args.output_dir, "phenomena_frequencies.md"),
        f"Linguistic Phenomena Frequencies (n={phenomena_total})",
        phenomena_freq,
    )
    print(f"Phenomena frequencies: {phenomena_freq}")
    
    # 3. Trace type distribution
    trace_dist = compute_trace_type_distribution(data)
    write_markdown_table(
        os.path.join(args.output_dir, "trace_type_distribution.md"),
        "Primary Trace Type Distribution",
        trace_dist,
    )
    print(f"Trace type distribution: {trace_dist}")
    
    # 4. Usefulness distribution
    usefulness_dist = compute_usefulness_distribution(data)
    write_markdown_table(
        os.path.join(args.output_dir, "usefulness_distribution.md"),
        "Trace Usefulness Distribution",
        usefulness_dist,
    )
    print(f"Usefulness distribution: {usefulness_dist}")
    
    # 5. Overlap distribution
    overlap_dist = compute_overlap_distribution(data)
    write_markdown_table(
        os.path.join(args.output_dir, "overlap_distribution.md"),
        "Trace-Translation Overlap Distribution",
        overlap_dist,
    )
    print(f"Overlap distribution: {overlap_dist}")
    
    # 6. Cross-tabulations
    print("\nComputing cross-tabulations...")
    
    # Trace type x usefulness
    crosstab_type_usefulness = cross_tabulate(data, "primary_trace_type", "usefulness")
    write_crosstab_markdown(
        os.path.join(args.output_dir, "crosstab_type_usefulness.md"),
        "Trace Type × Usefulness",
        crosstab_type_usefulness,
    )
    
    # Difficulty x trace type
    crosstab_difficulty_type = cross_tabulate(data, "difficulty", "primary_trace_type")
    write_crosstab_markdown(
        os.path.join(args.output_dir, "crosstab_difficulty_type.md"),
        "Difficulty × Trace Type",
        crosstab_difficulty_type,
    )
    
    # 7. Quality correlations
    if args.phase2_file:
        print("\nComputing quality correlations...")
        quality_corr = compute_quality_correlation(data, metric="sentence_bleu")
        
        with open(os.path.join(args.output_dir, "quality_correlations.md"), "w") as f:
            f.write("# Translation Quality Correlations\n\n")
            f.write("## Average BLEU by Trace Usefulness\n\n")
            for k, v in quality_corr["usefulness"].items():
                f.write(f"- {k}: {v:.2f}\n")
            
            f.write("\n## Average BLEU by Trace Type\n\n")
            for k, v in quality_corr["trace_type"].items():
                f.write(f"- {k}: {v:.2f}\n")
            
            f.write("\n## Average BLEU by Trace-Translation Overlap\n\n")
            for k, v in quality_corr["overlap"].items():
                f.write(f"- {k}: {v:.2f}\n")
        
        print("Quality correlations computed")
    
    # 8. Summary report
    print("\nGenerating summary report...")
    with open(os.path.join(args.output_dir, "SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write("# Phase 2 Analysis Summary\n\n")
        f.write(f"**Total Examples**: {len(data)}\n\n")
        
        f.write("## Difficulty Distribution\n\n")
        total_difficulty = sum(difficulty_dist.values())
        for score in sorted(difficulty_dist.keys()):
            count = difficulty_dist[score]
            pct = 100 * count / total_difficulty
            f.write(f"- Score {score}: {count} ({pct:.1f}%)\n")
        
        f.write("\n## Linguistic Phenomena\n\n")
        for phenom, count in sorted(phenomena_freq.items()):
            pct = 100 * count / phenomena_total
            f.write(f"- {phenom}: {count} ({pct:.1f}%)\n")
        
        f.write("\n## Trace Analysis\n\n")
        total_traces = sum(trace_dist.values())
        if total_traces > 0:
            f.write(f"**Examples with traces**: {total_traces}\n\n")
            
            f.write("### Primary Trace Types\n\n")
            for trace_type, count in sorted(trace_dist.items(), key=lambda x: x[1], reverse=True):
                pct = 100 * count / total_traces
                f.write(f"- {trace_type}: {count} ({pct:.1f}%)\n")
            
            f.write("\n### Trace Usefulness\n\n")
            for usefulness, count in sorted(usefulness_dist.items()):
                pct = 100 * count / sum(usefulness_dist.values())
                f.write(f"- {usefulness}: {count} ({pct:.1f}%)\n")
            
            f.write("\n### Trace-Translation Overlap\n\n")
            for overlap, count in sorted(overlap_dist.items()):
                pct = 100 * count / sum(overlap_dist.values())
                f.write(f"- {overlap}: {count} ({pct:.1f}%)\n")
        else:
            f.write("No examples with reasoning traces in this dataset.\n")
    
    print(f"\nAnalysis complete. Results saved to {args.output_dir}/")
    print("\nGenerated files:")
    for filename in os.listdir(args.output_dir):
        if filename.endswith(".md"):
            print(f"  - {filename}")


if __name__ == "__main__":
    main()
