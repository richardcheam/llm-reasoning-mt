#!/bin/bash
# Script to manually download FLORES-200 dataset on a machine without SSL issues
# After running this script, copy the entire output directory to the target machine

set -e

echo "=== FLORES-200 Manual Download Script ==="
echo ""

# Create output directory
OUTPUT_DIR="./flores_download"
mkdir -p "$OUTPUT_DIR"

echo "1. Downloading FLORES-200 dataset..."
echo "   This will download from: https://tinyurl.com/flores200dataset"
echo ""

cd "$OUTPUT_DIR"

# Try direct download from tinyurl
wget https://tinyurl.com/flores200dataset -O flores200.tar.gz || \
curl -L https://tinyurl.com/flores200dataset -o flores200.tar.gz

echo ""
echo "2. Extracting dataset..."
tar -xzf flores200.tar.gz

echo ""
echo "3. Verifying download..."
if [ -d "floresp-v2.0-rc.3" ] || [ -d "flores200_dataset" ] || ls -d flores* 2>/dev/null | grep -v "\.tar\.gz"; then
    echo "   ✓ Dataset extracted successfully"
    echo ""
    echo "   Contents:"
    ls -lah
else
    echo "   ✗ Extraction may have failed. Contents:"
    ls -lah
fi

echo ""
echo "=== Download Complete ==="
echo ""
echo "Next steps:"
echo "1. Copy the entire '$OUTPUT_DIR' directory to your target machine"
echo "2. Place it at: /home/richard/flores_dataset"
echo ""
echo "Commands to run on target machine:"
echo "   mkdir -p /home/richard/flores_dataset"
echo "   # Copy the extracted contents to /home/richard/flores_dataset"
echo ""
echo "Alternative: Use HuggingFace datasets cache format"
echo "   You can also download via Python on the working machine:"
echo ""
echo "   python3 -c \""
echo "   from datasets import load_dataset"
echo "   dataset = load_dataset('facebook/flores', 'eng_Latn', trust_remote_code=True)"
echo "   dataset = load_dataset('facebook/flores', 'fra_Latn', trust_remote_code=True)"
echo "   print('Downloaded to:', '~/.cache/huggingface/datasets/')"
echo "   \""
echo ""
echo "   Then copy ~/.cache/huggingface/datasets/ to the target machine"
