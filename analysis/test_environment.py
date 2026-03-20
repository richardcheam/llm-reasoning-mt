"""
Environment test script for Phase 2 annotation pipeline.

Run this script to verify your environment is correctly set up.

Usage:
    python analysis/test_environment.py
"""

import sys
import os

def check_python_version():
    """Check Python version."""
    print("Checking Python version...")
    version = sys.version_info
    print(f"  Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("  ❌ ERROR: Python 3.8 or higher required")
        return False
    else:
        print("  ✓ Python version OK")
        return True


def check_required_packages():
    """Check if required packages are installed."""
    print("\nChecking required packages...")
    
    packages = [
        ("torch", "PyTorch"),
        ("transformers", "Transformers"),
        ("datasets", "Datasets"),
        ("sacrebleu", "SacreBLEU"),
        ("spacy", "spaCy"),
        ("numpy", "NumPy"),
    ]
    
    all_ok = True
    for module_name, display_name in packages:
        try:
            module = __import__(module_name)
            version = getattr(module, "__version__", "unknown")
            print(f"  ✓ {display_name}: {version}")
        except ImportError:
            print(f"  ❌ {display_name}: NOT INSTALLED")
            all_ok = False
    
    return all_ok


def check_spacy_model():
    """Check if spaCy English model is installed."""
    print("\nChecking spaCy English model...")
    
    try:
        import spacy
        nlp = spacy.load("en_core_web_sm")
        print(f"  ✓ en_core_web_sm: {nlp.meta['version']}")
        return True
    except OSError:
        print("  ❌ en_core_web_sm: NOT INSTALLED")
        print("     Install with: python -m spacy download en_core_web_sm")
        return False


def check_phase2_scripts():
    """Check if Phase 2 scripts are accessible."""
    print("\nChecking Phase 2 scripts...")
    
    scripts = [
        "analysis/phase2_utils.py",
        "analysis/annotate_dataset.py",
        "analysis/analyze_traces.py",
        "analysis/build_phase2_dataset.py",
        "analysis/export_sentence_metrics.py",
    ]
    
    all_ok = True
    for script in scripts:
        if os.path.exists(script):
            print(f"  ✓ {script}")
        else:
            print(f"  ❌ {script}: NOT FOUND")
            all_ok = False
    
    return all_ok


def check_phase2_imports():
    """Check if Phase 2 utilities can be imported."""
    print("\nChecking Phase 2 imports...")
    
    try:
        from analysis.phase2_utils import load_jsonl, write_jsonl
        print("  ✓ phase2_utils imports OK")
        return True
    except ImportError as e:
        print(f"  ❌ phase2_utils import failed: {e}")
        return False


def check_cuda_availability():
    """Check CUDA/GPU availability."""
    print("\nChecking GPU availability...")
    
    try:
        import torch
        if torch.cuda.is_available():
            print(f"  ✓ CUDA available")
            print(f"    CUDA version: {torch.version.cuda}")
            print(f"    GPU count: {torch.cuda.device_count()}")
            for i in range(torch.cuda.device_count()):
                print(f"    GPU {i}: {torch.cuda.get_device_name(i)}")
        else:
            print("  ℹ CUDA not available (CPU mode only)")
            print("    This is OK - annotation can run on CPU")
    except Exception as e:
        print(f"  ℹ Could not check CUDA: {e}")


def check_documentation():
    """Check if documentation files exist."""
    print("\nChecking documentation...")
    
    docs = [
        ("analysis/annotation_codebook_v1.md", "Annotation Codebook"),
        ("analysis/annotation_prompt_v1.txt", "Annotation Prompt"),
        ("analysis/RC_METHODOLOGY.md", "Methodology Document"),
        ("analysis/RC_QUICKSTART.md", "Quick Start Guide"),
        ("analysis/README.md", "Phase 2 README"),
    ]
    
    all_ok = True
    for filepath, name in docs:
        if os.path.exists(filepath):
            print(f"  ✓ {name}")
        else:
            print(f"  ❌ {name}: NOT FOUND")
            all_ok = False
    
    return all_ok


def main():
    """Run all environment checks."""
    print("=" * 60)
    print("Phase 2 Environment Test")
    print("=" * 60)
    
    results = []
    
    results.append(("Python Version", check_python_version()))
    results.append(("Required Packages", check_required_packages()))
    results.append(("spaCy Model", check_spacy_model()))
    results.append(("Phase 2 Scripts", check_phase2_scripts()))
    results.append(("Phase 2 Imports", check_phase2_imports()))
    results.append(("Documentation", check_documentation()))
    
    check_cuda_availability()
    
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "✓ PASS" if passed else "❌ FAIL"
        print(f"{name:.<40} {status}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n✓ All checks passed!")
        print("\nYour environment is ready for Phase 2 annotation.")
        print("\nNext steps:")
        print("1. Read: analysis/RC_QUICKSTART.md")
        print("2. Read: analysis/annotation_codebook_v1.md")
        print("3. Start pilot annotation with:")
        print("   python analysis/annotate_dataset.py --help")
        return 0
    else:
        print("\n❌ Some checks failed.")
        print("\nPlease fix the issues above before proceeding.")
        print("See SETUP_WINDOWS.md for installation instructions.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
