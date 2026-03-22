#!/usr/bin/env python3
"""
Compare Generic CoT vs Guided CoT across all 24 language pairs.
Generates comprehensive summary and interpretation for linguistic experts.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

def parse_analysis_file(filepath: str) -> Dict:
    """Extract all statistics from a COMPREHENSIVE_ANALYSIS.md file."""
    if not os.path.exists(filepath):
        return None
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    data = {
        'total_examples': 0,
        'avg_difficulty': 0.0,
        'difficulty_dist': {},
        'linguistic_phenomena': {},
        'trace_types': {},
        'usefulness': {},
        'overlap': {},
        'metrics': {},
        'cross_tabs': {
            'difficulty_trace': {},
            'trace_usefulness': {}
        }
    }
    
    # Extract total examples
    match = re.search(r'\*\*Total Examples Analyzed\*\*:\s*(\d+)', content)
    if match:
        data['total_examples'] = int(match.group(1))
    
    # Extract average difficulty
    match = re.search(r'Average difficulty score\*\*:\s*([\d.]+)/5.0', content)
    if match:
        data['avg_difficulty'] = float(match.group(1))
    
    # Extract difficulty distribution
    diff_section = re.search(r'## 1\. Difficulty Distribution.*?(?=##)', content, re.DOTALL)
    if diff_section:
        for line in diff_section.group(0).split('\n'):
            if '|' in line and not line.startswith('|---') and not 'Difficulty Score' in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 3 and parts[0].isdigit():
                    data['difficulty_dist'][int(parts[0])] = {
                        'count': int(parts[1]),
                        'percentage': float(parts[2].rstrip('%'))
                    }
    
    # Extract linguistic phenomena
    ling_section = re.search(r'## 2\. Linguistic Phenomena Frequencies.*?(?=##)', content, re.DOTALL)
    if ling_section:
        for line in ling_section.group(0).split('\n'):
            if '|' in line and not line.startswith('|---') and not 'Phenomenon' in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 3 and parts[0] and parts[1].isdigit():
                    data['linguistic_phenomena'][parts[0]] = {
                        'count': int(parts[1]),
                        'percentage': float(parts[2].rstrip('%'))
                    }
    
    # Extract trace type distribution
    trace_section = re.search(r'## 3\. Primary Trace Type Distribution.*?(?=##)', content, re.DOTALL)
    if trace_section:
        for line in trace_section.group(0).split('\n'):
            if '|' in line and not line.startswith('|---') and not 'Trace Type' in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 3 and parts[0] and parts[1].isdigit():
                    data['trace_types'][parts[0]] = {
                        'count': int(parts[1]),
                        'percentage': float(parts[2].rstrip('%'))
                    }
    
    # Extract usefulness distribution
    useful_section = re.search(r'## 4\. Trace Usefulness Distribution.*?(?=##)', content, re.DOTALL)
    if useful_section:
        for line in useful_section.group(0).split('\n'):
            if '|' in line and not line.startswith('|---') and not 'Usefulness Level' in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 3 and parts[0] and parts[1].isdigit():
                    data['usefulness'][parts[0]] = {
                        'count': int(parts[1]),
                        'percentage': float(parts[2].rstrip('%'))
                    }
    
    # Extract overlap distribution
    overlap_section = re.search(r'## 5\. Trace-Translation Overlap Distribution.*?(?=##)', content, re.DOTALL)
    if overlap_section:
        for line in overlap_section.group(0).split('\n'):
            if '|' in line and not line.startswith('|---') and not 'Overlap Level' in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 3 and parts[0] and parts[1].isdigit():
                    data['overlap'][parts[0]] = {
                        'count': int(parts[1]),
                        'percentage': float(parts[2].rstrip('%'))
                    }
    
    # Extract quality correlations for ALL metrics
    metric_sections = re.finditer(r'### (BLEU|chrF\+\+|COMET|MetricX-24) Metric', content)
    for metric_match in metric_sections:
        metric_name = metric_match.group(1)
        start = metric_match.end()
        next_metric = re.search(r'###', content[start:])
        end = start + next_metric.start() if next_metric else len(content)
        metric_content = content[start:end]
        
        data['metrics'][metric_name] = {
            'by_usefulness': {},
            'by_trace_type': {},
            'by_overlap': {}
        }
        
        # Parse "by Trace Type" table
        type_match = re.search(r'\*\*Average.*?by Trace Type\*\*\s*\n+(.*?)(?=\n\*\*|\n###|\n---|\Z)', metric_content, re.DOTALL)
        if type_match:
            table_content = type_match.group(1)
            for line in table_content.split('\n'):
                if '|' in line and not line.startswith('|---') and 'Trace Type' not in line and 'Average Score' not in line:
                    parts = [p.strip() for p in line.split('|') if p.strip()]
                    if len(parts) >= 2 and parts[0] and parts[1]:
                        try:
                            data['metrics'][metric_name]['by_trace_type'][parts[0]] = float(parts[1])
                        except (ValueError, IndexError):
                            pass
        
        # Parse "by Trace Usefulness" table
        useful_match = re.search(r'\*\*Average.*?by Trace Usefulness\*\*\s*\n+(.*?)(?=\n\*\*|\n###|\n---|\Z)', metric_content, re.DOTALL)
        if useful_match:
            table_content = useful_match.group(1)
            for line in table_content.split('\n'):
                if '|' in line and not line.startswith('|---') and 'Usefulness Level' not in line and 'Average Score' not in line:
                    parts = [p.strip() for p in line.split('|') if p.strip()]
                    if len(parts) >= 2 and parts[0] and parts[1]:
                        try:
                            data['metrics'][metric_name]['by_usefulness'][parts[0]] = float(parts[1])
                        except (ValueError, IndexError):
                            pass
        
        # Parse "by Overlap" table
        overlap_match = re.search(r'\*\*Average.*?by Trace-Translation Overlap\*\*\s*\n+(.*?)(?=\n\*\*|\n###|\n---|\Z)', metric_content, re.DOTALL)
        if overlap_match:
            table_content = overlap_match.group(1)
            for line in table_content.split('\n'):
                if '|' in line and not line.startswith('|---') and 'Overlap Level' not in line and 'Average Score' not in line:
                    parts = [p.strip() for p in line.split('|') if p.strip()]
                    if len(parts) >= 2 and parts[0] and parts[1]:
                        try:
                            data['metrics'][metric_name]['by_overlap'][parts[0]] = float(parts[1])
                        except (ValueError, IndexError):
                            pass
    
    return data

def generate_comparison_report(language_pairs: List[str], output_file: str):
    """Generate comprehensive comparison report for linguistic experts."""
    
    comparisons = []
    
    for pair in language_pairs:
        # Paths to analysis files
        generic_path = f"evaluations/comprehensive_cot_eval/{pair}/gemma-3-1b-it/{pair.replace('_', '_to_')}_0_shot_seed_42_identity_None_0_0_0/COMPREHENSIVE_ANALYSIS.md"
        guided_path = f"evaluations/guided_cot_eval/{pair}/gemma-3-1b-it/{pair.replace('_', '_to_')}_0_shot_seed_42_identity_None_0_0_0/COMPREHENSIVE_ANALYSIS.md"
        
        generic_data = parse_analysis_file(generic_path)
        guided_data = parse_analysis_file(guided_path)
        
        if generic_data and guided_data:
            comparisons.append({
                'pair': pair,
                'generic': generic_data,
                'guided': guided_data
            })
    
    # Generate report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Comprehensive Linguistic Analysis: Generic CoT vs Guided CoT\n\n")
        f.write(f"**Analysis Date**: 2026-03-22\n\n")
        f.write(f"**Language Pairs Analyzed**: {len(comparisons)}/24\n\n")
        f.write(f"**Model**: google/gemma-3-1b-it\n\n")
        f.write(f"**Evaluation Setup**: Each language pair evaluated on 64 translation examples with Phase 2 linguistic annotation\n\n")
        f.write("---\n\n")
        
        # Table of contents
        f.write("## Table of Contents\n\n")
        f.write("1. [Executive Summary](#1-executive-summary)\n")
        f.write("2. [Aggregate Statistics](#2-aggregate-statistics-across-all-language-pairs)\n")
        f.write("3. [Language Pair Detailed Comparisons](#3-language-pair-detailed-comparisons)\n")
        f.write("4. [CoT Paradox Analysis](#4-cot-paradox-analysis)\n")
        f.write("5. [Linguistic Expert Interpretation Guide](#5-linguistic-expert-interpretation-guide)\n")
        f.write("\n---\n\n")
        
        # Executive Summary
        f.write("## 1. Executive Summary\n\n")
        
        # Aggregate metrics
        generic_totals = {
            'examples': 0, 
            'NONE': 0, 
            'TRANSLATION_ATTEMPT': 0,
            'CORRECT_LINGUISTIC_ANALYSIS': 0,
            'neutral': 0
        }
        guided_totals = {
            'examples': 0, 
            'NONE': 0, 
            'TRANSLATION_ATTEMPT': 0,
            'CORRECT_LINGUISTIC_ANALYSIS': 0,
            'neutral': 0
        }
        
        generic_metrics = {'BLEU': [], 'chrF++': [], 'COMET': [], 'MetricX-24': []}
        guided_metrics = {'BLEU': [], 'chrF++': [], 'COMET': [], 'MetricX-24': []}
        
        for comp in comparisons:
            generic_totals['examples'] += comp['generic']['total_examples']
            guided_totals['examples'] += comp['guided']['total_examples']
            
            for trace_type, data in comp['generic']['trace_types'].items():
                if trace_type == 'NONE':
                    generic_totals['NONE'] += data['count']
                elif trace_type == 'neutral':
                    generic_totals['neutral'] += data['count']
                elif trace_type == 'TRANSLATION_ATTEMPT':
                    generic_totals['TRANSLATION_ATTEMPT'] += data['count']
                elif trace_type == 'CORRECT_LINGUISTIC_ANALYSIS':
                    generic_totals['CORRECT_LINGUISTIC_ANALYSIS'] += data['count']
            
            for trace_type, data in comp['guided']['trace_types'].items():
                if trace_type == 'NONE':
                    guided_totals['NONE'] += data['count']
                elif trace_type == 'neutral':
                    guided_totals['neutral'] += data['count']
                elif trace_type == 'TRANSLATION_ATTEMPT':
                    guided_totals['TRANSLATION_ATTEMPT'] += data['count']
                elif trace_type == 'CORRECT_LINGUISTIC_ANALYSIS':
                    guided_totals['CORRECT_LINGUISTIC_ANALYSIS'] += data['count']
            
            # Collect metric scores
            for metric in ['BLEU', 'chrF++', 'COMET', 'MetricX-24']:
                if metric in comp['generic']['metrics']:
                    gen_scores = comp['generic']['metrics'][metric]['by_trace_type'].values()
                    if gen_scores:
                        generic_metrics[metric].extend(gen_scores)
                
                if metric in comp['guided']['metrics']:
                    guid_scores = comp['guided']['metrics'][metric]['by_trace_type'].values()
                    if guid_scores:
                        guided_metrics[metric].extend(guid_scores)
        
        f.write("### Key Findings\n\n")
        
        empty_reduction = 100*guided_totals['NONE']/guided_totals['examples'] - 100*generic_totals['NONE']/generic_totals['examples']
        f.write(f"1. **Empty Trace Reduction**: Guided CoT reduces empty traces (NONE) by **{abs(empty_reduction):.1f} percentage points** ")
        f.write(f"(Generic: {100*generic_totals['NONE']/generic_totals['examples']:.1f}%, Guided: {100*guided_totals['NONE']/guided_totals['examples']:.1f}%)\n\n")
        
        attempt_increase = 100*guided_totals['TRANSLATION_ATTEMPT']/guided_totals['examples'] - 100*generic_totals['TRANSLATION_ATTEMPT']/generic_totals['examples']
        f.write(f"2. **Translation Attempt Increase**: Guided CoT increases translation attempts by **{attempt_increase:.1f}pp** ")
        f.write(f"(Generic: {100*generic_totals['TRANSLATION_ATTEMPT']/generic_totals['examples']:.1f}%, Guided: {100*guided_totals['TRANSLATION_ATTEMPT']/guided_totals['examples']:.1f}%)\n\n")
        
        ling_increase = 100*guided_totals['CORRECT_LINGUISTIC_ANALYSIS']/guided_totals['examples'] - 100*generic_totals['CORRECT_LINGUISTIC_ANALYSIS']/generic_totals['examples']
        f.write(f"3. **Linguistic Analysis Increase**: Guided CoT increases correct linguistic analysis by **{ling_increase:.1f}pp** ")
        f.write(f"(Generic: {100*generic_totals['CORRECT_LINGUISTIC_ANALYSIS']/generic_totals['examples']:.1f}%, Guided: {100*guided_totals['CORRECT_LINGUISTIC_ANALYSIS']/guided_totals['examples']:.1f}%)\n\n")
        
        # Overall quality metrics
        f.write(f"4. **Translation Quality Impact**:\n")
        for metric in ['BLEU', 'chrF++', 'COMET', 'MetricX-24']:
            if generic_metrics[metric] and guided_metrics[metric]:
                gen_avg = sum(generic_metrics[metric]) / len(generic_metrics[metric])
                guid_avg = sum(guided_metrics[metric]) / len(guided_metrics[metric])
                diff = guid_avg - gen_avg
                diff_pct = (diff / gen_avg * 100) if gen_avg > 0 else 0
                sign = "+" if diff > 0 else ""
                f.write(f"   - **{metric}**: Generic={gen_avg:.2f}, Guided={guid_avg:.2f} ({sign}{diff:.2f}, {sign}{diff_pct:.1f}%)\n")
        f.write("\n")
        
        f.write("---\n\n")
        
        # Aggregate statistics table
        f.write("## 2. Aggregate Statistics Across All Language Pairs\n\n")
        
        f.write("### 2.1 Trace Distribution Summary\n\n")
        f.write("| Metric | Generic CoT | Guided CoT | Difference |\n")
        f.write("|--------|-------------|------------|------------|\n")
        f.write(f"| Total Examples | {generic_totals['examples']} | {guided_totals['examples']} | {guided_totals['examples'] - generic_totals['examples']} |\n")
        f.write(f"| Empty Traces (NONE) | {generic_totals['NONE']} ({100*generic_totals['NONE']/generic_totals['examples']:.1f}%) | ")
        f.write(f"{guided_totals['NONE']} ({100*guided_totals['NONE']/guided_totals['examples']:.1f}%) | ")
        f.write(f"{guided_totals['NONE']-generic_totals['NONE']} ({empty_reduction:.1f}pp) |\n")
        f.write(f"| Translation Attempts | {generic_totals['TRANSLATION_ATTEMPT']} ({100*generic_totals['TRANSLATION_ATTEMPT']/generic_totals['examples']:.1f}%) | ")
        f.write(f"{guided_totals['TRANSLATION_ATTEMPT']} ({100*guided_totals['TRANSLATION_ATTEMPT']/guided_totals['examples']:.1f}%) | ")
        f.write(f"+{guided_totals['TRANSLATION_ATTEMPT']-generic_totals['TRANSLATION_ATTEMPT']} ({attempt_increase:.1f}pp) |\n")
        f.write(f"| Linguistic Analysis | {generic_totals['CORRECT_LINGUISTIC_ANALYSIS']} ({100*generic_totals['CORRECT_LINGUISTIC_ANALYSIS']/generic_totals['examples']:.1f}%) | ")
        f.write(f"{guided_totals['CORRECT_LINGUISTIC_ANALYSIS']} ({100*guided_totals['CORRECT_LINGUISTIC_ANALYSIS']/guided_totals['examples']:.1f}%) | ")
        f.write(f"+{guided_totals['CORRECT_LINGUISTIC_ANALYSIS']-generic_totals['CORRECT_LINGUISTIC_ANALYSIS']} ({ling_increase:.1f}pp) |\n")
        f.write(f"| Neutral/Generic | {generic_totals['neutral']} ({100*generic_totals['neutral']/generic_totals['examples']:.1f}%) | ")
        f.write(f"{guided_totals['neutral']} ({100*guided_totals['neutral']/guided_totals['examples']:.1f}%) | ")
        neutral_diff = 100*guided_totals['neutral']/guided_totals['examples'] - 100*generic_totals['neutral']/generic_totals['examples']
        f.write(f"{guided_totals['neutral']-generic_totals['neutral']} ({neutral_diff:.1f}pp) |\n")
        f.write("\n")
        
        # Language pair by language pair comparison
        f.write("## 3. Language Pair Detailed Comparisons\n\n")
        
        for comp in comparisons:
            pair = comp['pair']
            generic = comp['generic']
            guided = comp['guided']
            
            f.write(f"### 3.{comparisons.index(comp)+1} {pair.replace('_', ' → ')}\n\n")
            
            # Basic statistics
            f.write(f"**Examples**: {generic['total_examples']} | ")
            f.write(f"**Avg Difficulty**: Generic={generic['avg_difficulty']:.2f}, Guided={guided['avg_difficulty']:.2f}\n\n")
            
            # Linguistic phenomena (if available)
            if generic['linguistic_phenomena'] or guided['linguistic_phenomena']:
                f.write("**Linguistic Phenomena Frequency**:\n\n")
                f.write("| Phenomenon | Generic | Guided |\n")
                f.write("|------------|---------|--------|\n")
                all_phenomena = set(list(generic['linguistic_phenomena'].keys()) + list(guided['linguistic_phenomena'].keys()))
                for phenom in sorted(all_phenomena):
                    gen_pct = generic['linguistic_phenomena'].get(phenom, {}).get('percentage', 0)
                    guid_pct = guided['linguistic_phenomena'].get(phenom, {}).get('percentage', 0)
                    f.write(f"| {phenom} | {gen_pct:.1f}% | {guid_pct:.1f}% |\n")
                f.write("\n")
            
            # Trace type comparison
            f.write("**Trace Type Distribution**:\n\n")
            f.write("| Trace Type | Generic Count | Generic % | Guided Count | Guided % | Δ Count | Δ % |\n")
            f.write("|------------|---------------|-----------|--------------|----------|---------|-----|\n")
            
            all_types = set(list(generic['trace_types'].keys()) + list(guided['trace_types'].keys()))
            for trace_type in sorted(all_types):
                gen_count = generic['trace_types'].get(trace_type, {}).get('count', 0)
                gen_pct = generic['trace_types'].get(trace_type, {}).get('percentage', 0)
                guid_count = guided['trace_types'].get(trace_type, {}).get('count', 0)
                guid_pct = guided['trace_types'].get(trace_type, {}).get('percentage', 0)
                delta_count = guid_count - gen_count
                delta_pct = guid_pct - gen_pct
                sign = "+" if delta_count > 0 else ""
                sign_pct = "+" if delta_pct > 0 else ""
                f.write(f"| {trace_type} | {gen_count} | {gen_pct:.1f}% | {guid_count} | {guid_pct:.1f}% | {sign}{delta_count} | {sign_pct}{delta_pct:.1f}pp |\n")
            f.write("\n")
            
            # Usefulness distribution
            if generic['usefulness'] or guided['usefulness']:
                f.write("**Trace Usefulness Distribution**:\n\n")
                f.write("| Usefulness | Generic | Guided | Δ |\n")
                f.write("|------------|---------|--------|---|\n")
                all_useful = set(list(generic['usefulness'].keys()) + list(guided['usefulness'].keys()))
                for useful in sorted(all_useful):
                    gen_pct = generic['usefulness'].get(useful, {}).get('percentage', 0)
                    guid_pct = guided['usefulness'].get(useful, {}).get('percentage', 0)
                    delta = guid_pct - gen_pct
                    sign = "+" if delta > 0 else ""
                    f.write(f"| {useful} | {gen_pct:.1f}% | {guid_pct:.1f}% | {sign}{delta:.1f}pp |\n")
                f.write("\n")
            
            # Quality metrics comparison
            f.write("**Translation Quality by Metric**:\n\n")
            
            for metric_name in ['BLEU', 'chrF++', 'COMET', 'MetricX-24']:
                if metric_name in generic['metrics'] and metric_name in guided['metrics']:
                    gen_by_type = generic['metrics'][metric_name]['by_trace_type']
                    guid_by_type = guided['metrics'][metric_name]['by_trace_type']
                    gen_by_useful = generic['metrics'][metric_name]['by_usefulness']
                    guid_by_useful = guided['metrics'][metric_name]['by_usefulness']
                    
                    if gen_by_type or guid_by_type:
                        f.write(f"<details>\n<summary><b>{metric_name}</b> (click to expand)</summary>\n\n")
                        
                        # Overall averages
                        if gen_by_type and guid_by_type:
                            gen_avg = sum(gen_by_type.values()) / len(gen_by_type) if gen_by_type else 0
                            guid_avg = sum(guid_by_type.values()) / len(guid_by_type) if guid_by_type else 0
                            diff = guid_avg - gen_avg
                            diff_sign = "+" if diff > 0 else ""
                            f.write(f"**Overall Average**: Generic={gen_avg:.3f}, Guided={guid_avg:.3f} (Δ {diff_sign}{diff:.3f})\n\n")
                        
                        # By trace type table
                        if gen_by_type or guid_by_type:
                            f.write("**By Trace Type**:\n\n")
                            f.write("| Trace Type | Generic | Guided | Δ |\n")
                            f.write("|------------|---------|--------|---|\n")
                            all_trace_types = set(list(gen_by_type.keys()) + list(guid_by_type.keys()))
                            for ttype in sorted(all_trace_types):
                                gen_val = gen_by_type.get(ttype, 0)
                                guid_val = guid_by_type.get(ttype, 0)
                                delta = guid_val - gen_val
                                sign = "+" if delta > 0 else ""
                                f.write(f"| {ttype} | {gen_val:.3f} | {guid_val:.3f} | {sign}{delta:.3f} |\n")
                            f.write("\n")
                        
                        # By usefulness table
                        if gen_by_useful or guid_by_useful:
                            f.write("**By Trace Usefulness**:\n\n")
                            f.write("| Usefulness | Generic | Guided | Δ |\n")
                            f.write("|------------|---------|--------|---|\n")
                            all_useful_levels = set(list(gen_by_useful.keys()) + list(guid_by_useful.keys()))
                            for ulevel in sorted(all_useful_levels):
                                gen_val = gen_by_useful.get(ulevel, 0)
                                guid_val = guid_by_useful.get(ulevel, 0)
                                delta = guid_val - gen_val
                                sign = "+" if delta > 0 else ""
                                f.write(f"| {ulevel} | {gen_val:.3f} | {guid_val:.3f} | {sign}{delta:.3f} |\n")
                            f.write("\n")
                        
                        # Best/worst analysis
                        if gen_by_type and guid_by_type:
                            gen_best = max(gen_by_type.items(), key=lambda x: x[1])
                            gen_worst = min(gen_by_type.items(), key=lambda x: x[1])
                            guid_best = max(guid_by_type.items(), key=lambda x: x[1])
                            guid_worst = min(guid_by_type.items(), key=lambda x: x[1])
                            
                            f.write(f"**Performance Range**:\n")
                            f.write(f"- Generic: Best={gen_best[0]} ({gen_best[1]:.3f}), Worst={gen_worst[0]} ({gen_worst[1]:.3f}), Gap={gen_best[1]-gen_worst[1]:.3f}\n")
                            f.write(f"- Guided: Best={guid_best[0]} ({guid_best[1]:.3f}), Worst={guid_worst[0]} ({guid_worst[1]:.3f}), Gap={guid_best[1]-guid_worst[1]:.3f}\n")
                            f.write("\n")
                        
                        f.write("</details>\n\n")
            
            f.write("---\n\n")
        
        # CoT Paradox Analysis
        f.write("## 4. CoT Paradox Analysis\n\n")
        f.write("**The CoT Paradox**: Instances where empty traces (NONE/neutral) perform better than linguistic analysis traces.\n\n")
        
        paradox_cases = {'BLEU': [], 'chrF++': [], 'COMET': [], 'MetricX-24': []}
        
        for comp in comparisons:
            pair = comp['pair']
            for variant, variant_name in [(comp['generic'], 'Generic'), (comp['guided'], 'Guided')]:
                for metric in ['BLEU', 'chrF++', 'COMET', 'MetricX-24']:
                    if metric in variant['metrics']:
                        by_type = variant['metrics'][metric]['by_trace_type']
                        
                        # Check if NONE/neutral outperforms CORRECT_LINGUISTIC_ANALYSIS
                        none_score = by_type.get('NONE', 0)
                        neutral_score = by_type.get('neutral', 0)
                        ling_score = by_type.get('CORRECT_LINGUISTIC_ANALYSIS', 0)
                        
                        empty_score = max(none_score, neutral_score)
                        
                        if ling_score > 0 and empty_score > ling_score:
                            paradox_cases[metric].append({
                                'pair': pair,
                                'variant': variant_name,
                                'empty_score': empty_score,
                                'ling_score': ling_score,
                                'gap': empty_score - ling_score
                            })
        
        for metric in ['BLEU', 'chrF++', 'COMET', 'MetricX-24']:
            if paradox_cases[metric]:
                f.write(f"### {metric} Paradox Cases\n\n")
                f.write(f"**Found {len(paradox_cases[metric])} instances where empty traces outperform linguistic analysis**\n\n")
                f.write("| Language Pair | CoT Variant | Empty Score | Linguistic Score | Gap |\n")
                f.write("|---------------|-------------|-------------|------------------|-----|\n")
                for case in sorted(paradox_cases[metric], key=lambda x: x['gap'], reverse=True)[:10]:
                    f.write(f"| {case['pair'].replace('_', '→')} | {case['variant']} | {case['empty_score']:.3f} | {case['ling_score']:.3f} | {case['gap']:.3f} |\n")
                f.write("\n")
        
        # Interpretation guide
        f.write("## 5. Linguistic Expert Interpretation Guide\n\n")
        f.write("### 5.1 Experimental Setup\n\n")
        f.write("**Evaluation Framework**:\n")
        f.write("- **24 language pairs** covering diverse typological characteristics\n")
        f.write("- **64 examples per language pair** (1,536 per CoT variant, 3,072 total)\n")
        f.write("- **Model**: google/gemma-3-1b-it (1B parameter LLM)\n")
        f.write("- **Two CoT variants**:\n")
        f.write("  - **Generic CoT**: Standard \"think step by step\" prompting\n")
        f.write("  - **Guided CoT**: Linguistic phenomenon-specific prompting with structured analysis\n\n")
        
        f.write("**Evaluation Metrics**:\n")
        f.write("- **BLEU** (with effective_order=True): N-gram overlap, sentence-level\n")
        f.write("- **chrF++**: Character n-gram F-score\n")
        f.write("- **COMET**: Neural learned metric (wmt22-comet-da)\n")
        f.write("- **MetricX-24**: Google's MT5-based learned metric\n\n")
        
        f.write("**Phase 2 Annotation Categories**:\n")
        f.write("- **Trace Types**: NONE, TRANSLATION_ATTEMPT, CORRECT_LINGUISTIC_ANALYSIS, HALLUCINATED_RULE, etc.\n")
        f.write("- **Usefulness**: high, medium, neutral (how helpful the reasoning trace was)\n")
        f.write("- **Difficulty**: 1-5 scale (translation complexity)\n")
        f.write("- **Linguistic Phenomena**: named_entities, complex_syntax, long_distance_dependency\n\n")
        
        f.write("### 5.2 Key Questions for Analysis\n\n")
        f.write("1. **Does guided prompting increase reasoning quality?**\n")
        f.write("   - Compare CORRECT_LINGUISTIC_ANALYSIS rates between variants\n")
        f.write("   - Examine trace usefulness distributions\n\n")
        
        f.write("2. **Does the CoT Paradox persist across metrics?**\n")
        f.write("   - Check if empty traces (NONE/neutral) outperform linguistic analysis\n")
        f.write("   - Identify language pairs where the paradox is strongest\n\n")
        
        f.write("3. **Are there language-specific patterns?**\n")
        f.write("   - Compare morphologically rich vs. isolating languages\n")
        f.write("   - Examine directions (e.g., English→X vs. X→English)\n\n")
        
        f.write("4. **What linguistic phenomena benefit most from guided CoT?**\n")
        f.write("   - Cross-reference phenomena frequencies with quality improvements\n")
        f.write("   - Identify where explicit linguistic prompting helps vs. hurts\n\n")
        
        f.write("### 5.3 Statistical Notes\n\n")
        f.write("- **Sample size**: 64 examples per language pair provides moderate statistical power\n")
        f.write("- **Percentage point (pp) differences**: Direct subtraction of percentages (e.g., 45% - 30% = 15pp)\n")
        f.write("- **Metric score ranges**: BLEU (0-100), chrF++ (0-100), COMET (-inf to 1.0), MetricX-24 (0-25)\n")
        f.write("- **Suggested significance threshold**: >5pp difference or >10% relative change\n\n")
        
        f.write("---\n\n")
        f.write("*Analysis generated from COMPREHENSIVE_ANALYSIS.md files in both evaluation directories*\n")
        f.write(f"*Total pairs analyzed: {len(comparisons)}/24*\n")
        f.write(f"*Total examples: {generic_totals['examples'] + guided_totals['examples']} ({generic_totals['examples']} Generic + {guided_totals['examples']} Guided)*\n")
    
    print(f"✅ Detailed comparison report saved to: {output_file}")
    print(f"   - Analyzed {len(comparisons)} language pairs")
    print(f"   - Total examples: {generic_totals['examples'] + guided_totals['examples']}")
    print(f"   - Includes: trace distributions, quality metrics, CoT paradox analysis, interpretation guide")

def main():
    # All 24 language pairs
    pairs = [
        "English_Finnish", "English_French", "English_German", "English_Kazakh",
        "English_Lithuanian", "English_Turkish", "English_Xhosa",
        "Finnish_English", "Finnish_Turkish",
        "French_English", "French_German",
        "German_English", "German_French",
        "Kazakh_English", "Kazakh_Xhosa",
        "Lithuanian_English", "Lithuanian_Turkish", "Lithuanian_Xhosa",
        "Turkish_English", "Turkish_Finnish", "Turkish_Lithuanian",
        "Xhosa_English", "Xhosa_Kazakh", "Xhosa_Lithuanian"
    ]
    
    generate_comparison_report(pairs, "COT_COMPARISON_REPORT.md")

if __name__ == "__main__":
    main()
