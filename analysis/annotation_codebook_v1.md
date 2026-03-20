# Annotation Codebook v1.0

**Project**: LLM Reasoning for Machine Translation  
**Owner**: Richard Cheam [RC]  
**Date**: 2026-03-20  
**Purpose**: Codebook-guided LLM-assisted annotation with manual audit

---

## Overview

This codebook defines the annotation schema for Phase 2 analysis of reasoning traces in machine translation. All annotations should be deterministic, reproducible, and follow this codebook exactly.

---

## 1. Sentence Difficulty Scoring

**Important**: Difficulty is assessed **only from the source sentence**, without looking at reference translation, model translation, or reasoning trace.

### Scale Definition

| Score | Label | Definition |
|-------|-------|------------|
| 1 | Trivial | Very simple sentence with basic vocabulary and simple grammar. Direct word-for-word translation would work. No cultural context needed. |
| 2 | Easy | Simple sentence with common vocabulary and straightforward grammar. Minor grammatical adjustments needed but meaning is transparent. |
| 3 | Moderate | Sentence requires grammatical transformations, has some domain-specific vocabulary, or requires understanding of standard context. |
| 4 | Difficult | Complex sentence with advanced vocabulary, complex syntax (e.g., multiple clauses, passive voice), idiomatic expressions, or cultural references. |
| 5 | Very Difficult | Extremely complex sentence with multiple challenges: technical jargon, nested clauses, ambiguity, figurative language, cultural nuances, or rare constructions. |

### Examples

**Score 1 (Trivial)**:
- "The cat is black."
- "I have a book."

**Score 2 (Easy)**:
- "The weather is nice today."
- "She went to the market yesterday."

**Score 3 (Moderate)**:
- "The government has announced new economic policies to address inflation."
- "Scientists have discovered a new species in the Amazon rainforest."

**Score 4 (Difficult)**:
- "The negotiations, which had been ongoing for several months, finally broke down over disagreements about intellectual property rights."
- "Despite the company's assurances, stakeholders remained skeptical about the proposed merger."

**Score 5 (Very Difficult)**:
- "The zeitgeist of post-war Europe, characterized by existential angst and a profound questioning of traditional values, permeated the literary works of the period."
- "Notwithstanding the aforementioned constraints, the implementation of the protocol necessitates a paradigm shift in organizational culture."

### Annotation Guidelines

1. Read **only** the source sentence
2. Consider vocabulary complexity
3. Consider syntactic complexity
4. Consider cultural/domain knowledge requirements
5. Consider ambiguity or multiple interpretations
6. Do **not** look at the translation or trace
7. Provide a brief justification (1-2 sentences)

---

## 2. Linguistic Phenomena Annotation

**Purpose**: Identify specific linguistic challenges in the source sentence that may affect translation.

### Phenomenon Definitions

#### 2.1 Ambiguity
**Definition**: The sentence has multiple valid interpretations due to lexical, syntactic, or semantic ambiguity.

**Types**:
- Lexical ambiguity: Words with multiple meanings (e.g., "bank" = financial institution or river bank)
- Syntactic ambiguity: Structural ambiguity (e.g., "I saw the man with the telescope")
- Anaphoric ambiguity: Unclear pronoun reference
- Scope ambiguity: Unclear scope of modifiers or quantifiers

**Examples**:
- "The chicken is ready to eat." (Is the chicken eating or being eaten?)
- "Visiting relatives can be boring." (Are you visiting them, or are they visiting you?)

**Annotation**: Mark as `true` if ANY type of ambiguity exists that could lead to different valid translations.

#### 2.2 Idiom
**Definition**: A multi-word expression whose meaning cannot be derived from the literal meanings of its components.

**Examples**:
- "It's raining cats and dogs."
- "Kick the bucket" (meaning: die)
- "Break a leg" (meaning: good luck)
- "Piece of cake" (meaning: easy)

**Annotation**: Mark as `true` if the sentence contains idiomatic expressions that require non-literal translation.

#### 2.3 Complex Syntax
**Definition**: The sentence has complex grammatical structure that requires careful parsing.

**Indicators**:
- Multiple embedded clauses (3+ levels)
- Long-distance dependencies
- Passive voice with complex agent structure
- Coordination of unlike elements
- Heavy center-embedding
- Non-standard word order

**Examples**:
- "The report that the committee that was formed last year submitted has been rejected."
- "Rarely have I seen such dedication."

**Annotation**: Mark as `true` if the syntactic structure goes beyond simple SVO patterns or requires significant restructuring in translation.

#### 2.4 Named Entities
**Definition**: The sentence contains proper names of persons, places, organizations, or other specific entities.

**Types**:
- Person names (e.g., "Marie Curie", "Nelson Mandela")
- Place names (e.g., "Johannesburg", "Mount Kilimanjaro")
- Organization names (e.g., "United Nations", "Harvard University")
- Product/brand names (e.g., "iPhone", "Coca-Cola")
- Event names (e.g., "World War II", "Olympics")

**Annotation**: Mark as `true` if the sentence contains one or more named entities that need special handling (transliteration, translation, or retention).

#### 2.5 Figurative Language
**Definition**: Language that uses figures of speech beyond literal meaning.

**Types**:
- Metaphor (e.g., "Time is money")
- Simile (e.g., "As brave as a lion")
- Personification (e.g., "The wind whispered")
- Hyperbole (e.g., "I've told you a million times")
- Irony/Sarcasm

**Annotation**: Mark as `true` if the sentence uses non-literal language that requires interpretation beyond surface meaning. Note: This is distinct from idioms (which are fixed expressions).

#### 2.6 Long-Distance Dependency
**Definition**: Grammatical relationships where dependent elements are separated by other constituents.

**Examples**:
- Wh-movement: "What did you say that John thinks that Mary bought __?"
- Relative clauses: "The book that I told you about yesterday is on the table."
- Topicalization: "This book, I really enjoyed."

**Annotation**: Mark as `true` if the sentence has dependencies spanning multiple phrases or clauses, requiring careful tracking of relationships.

### Multi-Label Annotation

A single sentence can have multiple linguistic phenomena. Mark all that apply.

---

## 3. Trace Type Classification

**Purpose**: Categorize the content and quality of reasoning traces produced by models.

**Important**: This annotation requires reading the reasoning trace (if present).

### 3.1 CORRECT_LINGUISTIC_ANALYSIS

**Definition**: The trace contains accurate analysis of linguistic properties, grammatical structures, or translation strategies.

**Indicators**:
- Correct identification of parts of speech
- Accurate description of syntactic structure
- Valid discussion of translation challenges
- Proper identification of idioms, ambiguities, or other phenomena
- Sound reasoning about translation choices

**Examples**:
- "The passive voice construction 'was eaten' requires restructuring in Xhosa."
- "The idiom 'break a leg' means 'good luck' and should not be translated literally."
- "The pronoun 'it' refers to 'the book' mentioned earlier."

**Annotation**: Mark as primary or secondary type if the trace shows genuine linguistic insight.

### 3.2 HALLUCINATED_RULE

**Definition**: The trace invents or misapplies grammatical rules, translation principles, or linguistic facts.

**Indicators**:
- Factually incorrect grammatical statements
- Made-up translation rules
- Misidentification of linguistic phenomena
- Incorrect word meanings
- False claims about language structure

**Examples**:
- "In Xhosa, all verbs must end with -ing." (incorrect)
- "This idiom comes from ancient Greek mythology." (when it doesn't)
- "The word 'bank' always means 'financial institution' in this context." (when ambiguous)

**Annotation**: Mark as primary type if the trace contains significant factual errors or invented rules.

### 3.3 VACUOUS_FILLER

**Definition**: The trace contains generic statements, repetitions, or content that provides no useful information.

**Indicators**:
- Repetition of the source sentence
- Generic statements like "This is a translation task."
- Placeholder text without substance
- Circular reasoning
- Statements that don't advance understanding

**Examples**:
- "To translate this sentence, I will translate it."
- "This sentence is about X. X is mentioned in the sentence."
- "I need to be careful with this translation."

**Annotation**: Mark as primary type if >50% of the trace is vacuous content.

### 3.4 TRANSLATION_ATTEMPT

**Definition**: The trace contains actual translation attempts, intermediate translations, or translation drafts.

**Indicators**:
- Partial translations
- Word-by-word translation attempts
- Multiple translation candidates
- Translation refinement steps
- Back-translation

**Examples**:
- "First attempt: 'Le chat noir'. Better: 'Le chat est noir.'"
- "Word-by-word: 'The' → 'Le', 'cat' → 'chat'..."
- "Draft translation: [...]. Revised translation: [...]"

**Annotation**: Mark as primary or secondary type if the trace shows actual translation work.

### 3.5 REPETITION

**Definition**: The trace repeats the same content multiple times without adding new information.

**Indicators**:
- Verbatim repetition of phrases
- Rephrasing of the same point without elaboration
- Circular loops in reasoning
- Copy-pasted segments

**Examples**:
- "The sentence is complex. Due to its complexity, it is complex. This complexity makes it complex."

**Annotation**: Mark as primary type if repetition is the dominant characteristic, or as secondary if some repetition exists alongside other content.

### Multi-Label Classification

Traces can be assigned:
- **One primary type** (dominant characteristic)
- **Multiple secondary types** (present but not dominant)

---

## 4. Trace Usefulness Analysis

**Purpose**: Assess whether the reasoning trace actually helps produce a better translation.

### 4.1 Helpful

**Definition**: The trace provides insights or reasoning that leads to better translation quality.

**Indicators**:
- Identifies real translation challenges
- Proposes valid solutions
- Shows beneficial intermediate steps
- Catches and corrects errors
- Provides useful context or analysis

**Annotation**: Mark as "helpful" if the trace demonstrably contributes to translation quality.

### 4.2 Neutral

**Definition**: The trace is neither helpful nor harmful—it doesn't affect translation quality.

**Indicators**:
- Generic reasoning that doesn't address specific challenges
- Correct but obvious statements
- Tangential analysis
- No clear connection between trace and final translation

**Annotation**: Mark as "neutral" if the trace could be removed without affecting translation quality.

### 4.3 Harmful

**Definition**: The trace introduces errors, confusion, or leads to worse translation.

**Indicators**:
- Incorrect analysis that leads to wrong translation choices
- Introduction of hallucinated information
- Fixation on irrelevant aspects
- Misleading reasoning paths
- Self-contradiction that causes errors

**Annotation**: Mark as "harmful" if the trace appears to degrade translation quality.

---

## 5. Trace-Translation Overlap

**Purpose**: Measure how much content from the trace appears in the final translation.

### 5.1 None

**Definition**: No discernible overlap between trace content and final translation.

**Indicators**:
- Trace discusses different content
- Translation doesn't use words or phrases from trace
- Completely separate generation paths

### 5.2 Low

**Definition**: Minimal overlap (roughly <25% of translation content from trace).

**Indicators**:
- A few words or phrases reused
- Some minor elements carried over
- Mostly independent generation

### 5.3 Medium

**Definition**: Moderate overlap (roughly 25-75% of translation content from trace).

**Indicators**:
- Substantial reuse of phrases
- Key translation choices visible in trace
- Clear connection but not complete copy

### 5.4 High

**Definition**: Strong overlap (roughly >75% of translation content from trace).

**Indicators**:
- Translation closely follows trace
- Most words/phrases from trace appear in translation
- Near-direct extraction from trace

**Annotation**: This is a qualitative judgment. Consider both lexical overlap and conceptual overlap.

---

## 6. Trace Length Estimation

**Purpose**: Estimate the length of the reasoning trace for correlation analysis.

### Measurement

Count one of the following (be consistent):
- **Word count**: Number of whitespace-separated tokens
- **Character count**: Total characters including spaces
- **Token count**: Number of tokens after tokenization (if using LLM)

**Annotation**: Record as an integer. Specify the unit used.

---

## Reproducibility Requirements

### For Manual Annotation
1. Follow this codebook exactly
2. Document any edge cases or uncertainties
3. Include inter-annotator agreement checks
4. Record date, annotator ID, and codebook version

### For LLM-Assisted Annotation
1. Use a fixed model (e.g., specific HuggingFace checkpoint)
2. Use deterministic decoding (temperature=0.0, greedy=True)
3. Use a fixed prompt template (see annotation_prompt_v1.txt)
4. Save raw model outputs
5. Save parsed JSON outputs
6. Include annotation metadata:
   - annotation_model_name
   - annotation_model_revision
   - annotation_prompt_version
   - annotation_codebook_version
   - annotation_date
   - annotation_temperature
   - annotation_seed

---

## Annotation Output Format

For each example, produce a JSON object with the following structure:

```json
{
  "example_id": "flores:English:Xhosa:0:123",
  "difficulty": {
    "score": 3,
    "justification": "Sentence contains domain-specific vocabulary and requires understanding of economic context."
  },
  "linguistic_phenomena": {
    "ambiguity": false,
    "idiom": false,
    "complex_syntax": true,
    "named_entities": false,
    "figurative_language": false,
    "long_distance_dependency": false
  },
  "trace_analysis": {
    "primary_trace_type": "CORRECT_LINGUISTIC_ANALYSIS",
    "secondary_trace_types": ["TRANSLATION_ATTEMPT"],
    "usefulness": "helpful",
    "overlap": "medium",
    "length_tokens": 245
  },
  "annotator_notes": "Optional free-text notes",
  "annotation_metadata": {
    "codebook_version": "v1.0",
    "annotator_id": "RC",
    "annotation_date": "2026-03-20"
  }
}
```

---

## Edge Cases and Guidelines

### When Source Language is Not English
- Difficulty scoring should still consider complexity from a translation perspective
- Linguistic phenomena definitions apply to the source language

### When No Reasoning Trace Exists
- Skip trace_analysis section
- Set all trace fields to `null`

### When Trace is Very Short (<10 tokens)
- Can still classify, but consider if it's substantial enough to be useful
- Likely "VACUOUS_FILLER" or "REPETITION"

### When Multiple Interpretations are Possible
- Choose the most reasonable interpretation
- Document uncertainty in annotator_notes
- Prefer objective criteria over subjective judgment

### Contamination Safety
- **NEVER** use the reference translation when scoring difficulty
- **NEVER** use the model translation when scoring difficulty
- **NEVER** use the reasoning trace when scoring difficulty
- Difficulty is **source-only**

---

## Version History

- **v1.0** (2026-03-20): Initial codebook creation for RC Phase 2 analysis

---

## Quality Control

### Pilot Annotation (50-100 examples)
1. Annotate pilot set using this codebook
2. Review for consistency
3. Identify ambiguous cases
4. Refine codebook if needed (increment version)
5. Re-annotate pilot set with refined codebook

### Full Annotation
1. Stratify by model, prompt type, language pair, shot count
2. Sample to include quality variation (strong and weak translations)
3. Sample to include trace variation (short and long traces)
4. Maintain consistency across batches
5. Audit sample for quality control (10-20% manual review)

---

**End of Codebook v1.0**
