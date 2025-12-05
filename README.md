# Lightweight Cryptography for IoT Devices

This repository contains benchmark implementations and performance evaluations of lightweight cryptographic algorithms suitable for resource-constrained IoT devices.

## Overview

This project evaluates three lightweight cryptographic algorithms:
- **ASCON**: Winner of the CAESAR competition for lightweight authenticated encryption
- **AES-CCM**: Advanced Encryption Standard in Counter with CBC-MAC mode
- **ChaCha20**: High-performance stream cipher

## Repository Structure

```
lightweight-crypto-iot/
├── code/               # Benchmark implementations
│   ├── ascon_benchmark.c
│   ├── aesccm_benchmark.c
│   └── chacha20_benchmark.c
├── scripts/            # Build and benchmark scripts
│   ├── compile_all.sh
│   └── benchmark.py
├── results/            # Benchmark results and graphs
│   ├── benchmark_results.csv
│   └── graphs/
├── paper/              # Research paper (LaTeX)
│   ├── paper.tex
│   └── references.bib
├── README.md
└── LICENSE
```

## Getting Started

### Prerequisites
- GCC compiler
- Python 3.x (for running benchmark scripts)
- Make (optional)

### Building the Benchmarks

Navigate to the `scripts/` directory and run:

```bash
cd scripts
./compile_all.sh
```

This will compile all benchmark programs into the `build/` directory.

### Running Benchmarks

#### Run Individual Benchmarks
```bash
./build/ascon_benchmark
./build/aesccm_benchmark
./build/chacha20_benchmark
```

#### Run All Benchmarks with Python Script
```bash
cd scripts
python3 benchmark.py
```

The Python script will:
1. Compile all benchmarks
2. Run each benchmark
3. Collect and save results to `results/benchmark_results.csv`
4. Display a summary

## Results

Benchmark results are stored in `results/benchmark_results.csv` with metrics including:
- Execution time
- Average time per operation
- Iterations performed

Graphs and visualizations can be placed in the `results/graphs/` directory.

## Research Paper

The `paper/` directory contains a LaTeX research paper template for documenting the performance evaluation findings.

To compile the paper:
```bash
cd paper
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Acknowledgments

- ASCON algorithm developers
- NIST Lightweight Cryptography standardization project
- IoT security research community