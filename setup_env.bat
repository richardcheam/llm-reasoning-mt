@echo off
REM Windows Setup Script for LLM Reasoning MT - Phase 2
REM This script sets up the Python environment for RC's annotation work

echo ========================================
echo LLM Reasoning MT - Environment Setup
echo ========================================
echo.

REM Check for Python
echo [1/6] Checking for Python installation...
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=python
    goto :python_found
)

where py >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=py
    goto :python_found
)

where python3 >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=python3
    goto :python_found
)

echo ERROR: Python not found!
echo.
echo Please install Python 3.8 or higher from:
echo https://www.python.org/downloads/
echo.
echo Make sure to check "Add Python to PATH" during installation.
pause
exit /b 1

:python_found
echo Found: %PYTHON_CMD%
%PYTHON_CMD% --version
echo.

REM Check Python version
echo [2/6] Checking Python version...
%PYTHON_CMD% -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python 3.8 or higher required
    %PYTHON_CMD% --version
    pause
    exit /b 1
)
echo Python version OK
echo.

REM Create virtual environment
echo [3/6] Creating virtual environment...
if exist .venv (
    echo Virtual environment already exists (.venv)
    echo Skipping creation...
) else (
    %PYTHON_CMD% -m venv .venv
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully
)
echo.

REM Activate virtual environment
echo [4/6] Activating virtual environment...
call .venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo Virtual environment activated
echo.

REM Upgrade pip
echo [5/6] Upgrading pip...
python -m pip install --upgrade pip --quiet
echo Pip upgraded
echo.

REM Install dependencies
echo [6/6] Installing dependencies from requirements-phase2.txt...
echo This may take 10-20 minutes...
echo.
pip install -r requirements-phase2.txt
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Install spaCy model
echo Installing spaCy English model...
python -m spacy download en_core_web_sm
if %ERRORLEVEL% NEQ 0 (
    echo WARNING: Failed to install spaCy model
    echo You may need to install it manually later
)
echo.

REM Verify installation
echo ========================================
echo Verifying Installation
echo ========================================
echo.

python -c "import torch; print('PyTorch:', torch.__version__)"
python -c "import transformers; print('Transformers:', transformers.__version__)"
python -c "import datasets; print('Datasets:', datasets.__version__)"
python -c "from analysis.phase2_utils import load_jsonl; print('Phase 2 utils: OK')"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo Setup Complete!
    echo ========================================
    echo.
    echo Your environment is ready for Phase 2 annotation.
    echo.
    echo Next steps:
    echo 1. Read: analysis\RC_QUICKSTART.md
    echo 2. Read: analysis\annotation_codebook_v1.md
    echo 3. Start pilot annotation
    echo.
    echo To use this environment in the future:
    echo   .venv\Scripts\activate.bat
    echo.
) else (
    echo.
    echo ========================================
    echo Setup completed with warnings
    echo ========================================
    echo.
    echo Some components may not have installed correctly.
    echo Try running the verification commands manually.
    echo.
)

pause
