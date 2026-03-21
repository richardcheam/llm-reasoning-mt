#!/usr/bin/env python3
"""
Script to download FLORES-200 dataset via HuggingFace on a machine without SSL issues.
After running this script, copy the cache directory to the target machine.

Usage:
    python download_flores_python.py

This will download English and French FLORES data to ~/.cache/huggingface/datasets/
"""

from datasets import load_dataset
import os
from pathlib import Path

def main():
    print("=== FLORES-200 Dataset Download (via HuggingFace) ===")
    print()
    
    # Languages to download for English→French translation
    languages = {
        'English': 'eng_Latn',
        'French': 'fra_Latn'
    }
    
    cache_dir = Path.home() / ".cache" / "huggingface" / "datasets"
    print(f"Cache directory: {cache_dir}")
    print()
    
    for lang_name, lang_code in languages.items():
        print(f"Downloading {lang_name} ({lang_code})...")
        try:
            dataset = load_dataset(
                'facebook/flores',
                lang_code,
                trust_remote_code=True
            )
            
            print(f"  ✓ {lang_name} downloaded successfully")
            print(f"    - dev split: {len(dataset['dev'])} samples")
            print(f"    - devtest split: {len(dataset['devtest'])} samples")
            print()
            
        except Exception as e:
            print(f"  ✗ Error downloading {lang_name}: {e}")
            print()
    
    print("=== Download Complete ===")
    print()
    print("Next steps:")
    print(f"1. Locate the downloaded cache at: {cache_dir}")
    print("2. Copy the entire facebook___flores directory to the target machine:")
    print(f"   Source: {cache_dir}/facebook___flores/")
    print(f"   Target: /home/richard/.cache/huggingface/datasets/facebook___flores/")
    print()
    print("Commands for target machine:")
    print("   mkdir -p /home/richard/.cache/huggingface/datasets/")
    print("   # Copy the facebook___flores directory")
    print()
    print("Also copy the dataset modules:")
    print(f"   Source: {Path.home()}/.cache/huggingface/modules/datasets_modules/datasets/facebook--flores/")
    print("   Target: /home/richard/.cache/huggingface/modules/datasets_modules/datasets/facebook--flores/")
    print()
    
    # Show cache structure
    print("Cache structure to copy:")
    print("~/.cache/huggingface/")
    print("├── datasets/")
    print("│   └── facebook___flores/")
    print("│       └── (all downloaded files)")
    print("└── modules/")
    print("    └── datasets_modules/")
    print("        └── datasets/")
    print("            └── facebook--flores/")
    print("                └── (loader scripts)")

if __name__ == "__main__":
    main()
