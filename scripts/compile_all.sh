#!/bin/bash

# Compile all benchmark programs
# Usage: ./compile_all.sh

echo "Compiling lightweight cryptography benchmarks..."

# Check if gcc is installed
if ! command -v gcc &> /dev/null; then
    echo "Error: gcc not found. Please install gcc to compile the benchmarks."
    exit 1
fi

# Create build directory if it doesn't exist
mkdir -p ../build

# Compile ASCON benchmark
echo "Compiling ascon_benchmark.c..."
gcc -O2 -o ../build/ascon_benchmark ../code/ascon_benchmark.c -lm
if [ $? -eq 0 ]; then
    echo "  ✓ ascon_benchmark compiled successfully"
else
    echo "  ✗ Failed to compile ascon_benchmark"
fi

# Compile AES-CCM benchmark
echo "Compiling aesccm_benchmark.c..."
gcc -O2 -o ../build/aesccm_benchmark ../code/aesccm_benchmark.c -lm
if [ $? -eq 0 ]; then
    echo "  ✓ aesccm_benchmark compiled successfully"
else
    echo "  ✗ Failed to compile aesccm_benchmark"
fi

# Compile ChaCha20 benchmark
echo "Compiling chacha20_benchmark.c..."
gcc -O2 -o ../build/chacha20_benchmark ../code/chacha20_benchmark.c -lm
if [ $? -eq 0 ]; then
    echo "  ✓ chacha20_benchmark compiled successfully"
else
    echo "  ✗ Failed to compile chacha20_benchmark"
fi

echo ""
echo "Compilation complete! Executables are in the build/ directory."
echo "Run individual benchmarks from the build directory:"
echo "  ./build/ascon_benchmark"
echo "  ./build/aesccm_benchmark"
echo "  ./build/chacha20_benchmark"
