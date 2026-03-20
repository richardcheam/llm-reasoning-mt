# Windows Environment Setup for LLM Reasoning MT

This guide provides Windows-specific setup instructions for running the Phase 2 annotation pipeline.

## Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- At least 4GB free disk space

## Quick Setup (Recommended)

### Option 1: Using Python venv (Standard)

```cmd
REM 1. Create virtual environment
python -m venv .venv

REM 2. Activate virtual environment
.venv\Scripts\activate.bat

REM 3. Upgrade pip
python -m pip install --upgrade pip

REM 4. Install dependencies
pip install -r requirements-phase2.txt

REM 5. Install spaCy English model
python -m spacy download en_core_web_sm

REM 6. Verify installation
python -c "import torch; import transformers; import datasets; print('Environment ready!')"
```

### Option 2: Using PowerShell

```powershell
# 1. Create virtual environment
python -m venv .venv

# 2. Activate virtual environment
.venv\Scripts\Activate.ps1

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install dependencies
pip install -r requirements-phase2.txt

# 5. Install spaCy English model
python -m spacy download en_core_web_sm

# 6. Verify installation
python -c "import torch; import transformers; import datasets; print('Environment ready!')"
```

## Step-by-Step Instructions

### Step 1: Create Virtual Environment

```cmd
python -m venv .venv
```

This creates a `.venv` directory with a clean Python environment.

### Step 2: Activate Virtual Environment

**Command Prompt (cmd.exe):**
```cmd
.venv\Scripts\activate.bat
```

**PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

**Git Bash (if you have it):**
```bash
source .venv/Scripts/activate
```

You should see `(.venv)` at the beginning of your command prompt.

### Step 3: Install Dependencies

```cmd
python -m pip install --upgrade pip
pip install -r requirements-phase2.txt
```

This will install:
- `torch` (PyTorch for deep learning)
- `transformers` (HuggingFace models)
- `datasets` (data handling)
- `sacrebleu` (BLEU metrics)
- `unbabel-comet` (COMET metrics)
- And other required packages

**Note**: Installation may take 10-20 minutes depending on your internet speed.

### Step 4: Install spaCy Model

```cmd
python -m spacy download en_core_web_sm
```

This downloads the English language model needed by some components.

### Step 5: Verify Installation

```cmd
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import transformers; print(f'Transformers: {transformers.__version__}')"
python -c "import spacy; nlp = spacy.load('en_core_web_sm'); print('spaCy: OK')"
python -c "import analysis.phase2_utils; print('Phase 2 utilities: OK')"
```

All commands should complete without errors.

## Optional: GPU Support

If you have an NVIDIA GPU and want to use it for faster annotation:

### Check CUDA Availability

```cmd
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'CUDA version: {torch.version.cuda if torch.cuda.is_available() else 'N/A'}')"
```

### Install CUDA-Enabled PyTorch (if needed)

If CUDA is not available but you have an NVIDIA GPU:

1. Check your CUDA version: Visit [NVIDIA CUDA Downloads](https://developer.nvidia.com/cuda-downloads)
2. Install PyTorch with CUDA support:

```cmd
REM For CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

REM For CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Running Phase 2 Annotation

Once your environment is set up, you can run the annotation pipeline:

### Manual Annotation (Pilot)

```cmd
python analysis\annotate_dataset.py ^
    --input_file path\to\phase2_dataset.jsonl ^
    --output_file pilot_manual.jsonl ^
    --manual_mode ^
    --sample_size 50 ^
    --annotator_id RC
```

**Note**: In Windows cmd, use `^` for line continuation. In PowerShell, use `` ` ``.

### LLM-Assisted Annotation

```cmd
python analysis\annotate_dataset.py ^
    --input_file path\to\phase2_dataset.jsonl ^
    --output_file llm_annotations.jsonl ^
    --annotation_model google/gemma-2-9b-it ^
    --temperature 0.0 ^
    --seed 42 ^
    --batch_size 8 ^
    --save_raw_outputs ^
    --annotator_id RC
```

### Generate Analysis Tables

```cmd
python analysis\analyze_traces.py ^
    --annotated_file llm_annotations.jsonl ^
    --phase2_file phase2_dataset.jsonl ^
    --output_dir results\
```

## Troubleshooting

### "python: command not found"

Make sure Python is installed and in your PATH:
```cmd
python --version
```

If this fails, reinstall Python from [python.org](https://www.python.org/) and check "Add Python to PATH" during installation.

### "Activate.ps1 cannot be loaded because running scripts is disabled"

PowerShell requires you to enable script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again.

### "No module named 'torch'" after installation

Make sure you're in the activated virtual environment:
- You should see `(.venv)` in your prompt
- Run `.venv\Scripts\activate.bat` again if needed

### Out of Memory Errors

If you run out of memory during annotation:
1. Reduce batch size: `--batch_size 1`
2. Use CPU instead of GPU: `--device cpu`
3. Annotate in smaller chunks: `--sample_size 100`

### Slow Download Speeds

HuggingFace model downloads can be slow. Be patient or:
1. Use a VPN if in a restricted region
2. Set HuggingFace cache location:
```cmd
set HF_HOME=D:\huggingface_cache
```

## Directory Structure After Setup

```
llm-reasoning-mt/
├── .venv/                          # Virtual environment
├── analysis/
│   ├── annotation_codebook_v1.md
│   ├── annotate_dataset.py
│   ├── analyze_traces.py
│   └── ...
├── requirements-phase2.txt
├── SETUP_WINDOWS.md               # This file
└── ...
```

## Deactivating the Environment

When you're done working:

```cmd
deactivate
```

This returns you to your system Python environment.

## Next Steps

After setup is complete:

1. Read [`analysis/RC_QUICKSTART.md`](analysis/RC_QUICKSTART.md)
2. Review [`analysis/annotation_codebook_v1.md`](analysis/annotation_codebook_v1.md)
3. Start with manual pilot annotation (50 examples)
4. Scale up with LLM-assisted annotation

## Environment Variables (Optional)

For HuggingFace authentication (if using gated models):

```cmd
set HF_TOKEN=your_huggingface_token_here
```

Or create a `.env` file in the project root:
```
HF_TOKEN=your_token_here
HUGGINGFACE_HUB_TOKEN=your_token_here
```

## Testing Your Setup

Run this test script to verify everything works:

```cmd
python -c "import sys; print(f'Python: {sys.version}'); import torch; print(f'PyTorch: {torch.__version__}'); import transformers; print(f'Transformers: {transformers.__version__}'); from analysis.phase2_utils import load_jsonl; print('Phase 2 utils: OK')"
```

Expected output:
```
Python: 3.x.x
PyTorch: 2.x.x
Transformers: 4.x.x
Phase 2 utils: OK
```

## Additional Resources

- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [HuggingFace Installation](https://huggingface.co/docs/transformers/installation)
- [PyTorch Windows Installation](https://pytorch.org/get-started/locally/)

## Contact

If you encounter issues not covered here, refer to:
- Project README: [`README.md`](README.md)
- Phase 2 README: [`analysis/README.md`](analysis/README.md)
- Handoff document: [`RC_LLM_HANDOFF.txt`](RC_LLM_HANDOFF.txt)

---

**Last Updated**: 2026-03-20  
**Platform**: Windows 10/11  
**Python**: 3.8+
