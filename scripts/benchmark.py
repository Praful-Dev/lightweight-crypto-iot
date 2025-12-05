#!/usr/bin/env python3
"""
Benchmark runner and results analyzer
Runs all cryptographic benchmarks and generates comparison reports
"""

import subprocess
import csv
import os
import sys
from datetime import datetime

class BenchmarkRunner:
    def __init__(self):
        self.results = []
        self.build_dir = os.path.join(os.path.dirname(__file__), '..', 'build')
        self.results_dir = os.path.join(os.path.dirname(__file__), '..', 'results')
        
    def ensure_compiled(self):
        """Ensure all benchmarks are compiled"""
        compile_script = os.path.join(os.path.dirname(__file__), 'compile_all.sh')
        if not os.path.exists(compile_script):
            print("Error: compile_all.sh not found")
            return False
            
        print("Compiling benchmarks...")
        result = subprocess.run(['bash', compile_script], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Compilation failed:\n{result.stderr}")
            return False
        print("Compilation successful!\n")
        return True
    
    def run_benchmark(self, name, executable):
        """Run a single benchmark and capture output"""
        exe_path = os.path.join(self.build_dir, executable)
        
        if not os.path.exists(exe_path):
            print(f"Warning: {executable} not found, skipping...")
            return None
        
        print(f"Running {name} benchmark...")
        try:
            result = subprocess.run([exe_path], capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print(f"  ✓ {name} completed")
                return result.stdout
            else:
                print(f"  ✗ {name} failed")
                return None
        except subprocess.TimeoutExpired:
            print(f"  ✗ {name} timed out")
            return None
    
    def run_all_benchmarks(self):
        """Run all available benchmarks"""
        benchmarks = [
            ('ASCON', 'ascon_benchmark'),
            ('AES-CCM', 'aesccm_benchmark'),
            ('ChaCha20', 'chacha20_benchmark'),
        ]
        
        print("=" * 50)
        print("Running Lightweight Cryptography Benchmarks")
        print("=" * 50)
        print()
        
        for name, executable in benchmarks:
            output = self.run_benchmark(name, executable)
            if output:
                self.results.append({
                    'algorithm': name,
                    'timestamp': datetime.now().isoformat(),
                    'output': output
                })
        
        print()
        print("=" * 50)
        print("Benchmark run complete!")
        print("=" * 50)
    
    def save_results(self):
        """Save benchmark results to CSV"""
        if not self.results:
            print("No results to save")
            return
        
        os.makedirs(self.results_dir, exist_ok=True)
        
        csv_file = os.path.join(self.results_dir, 'benchmark_results.csv')
        file_exists = os.path.exists(csv_file)
        
        with open(csv_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['algorithm', 'timestamp', 'output'])
            if not file_exists:
                writer.writeheader()
            writer.writerows(self.results)
        
        print(f"\nResults saved to {csv_file}")
    
    def display_summary(self):
        """Display summary of benchmark results"""
        if not self.results:
            print("\nNo results to display")
            return
        
        print("\n" + "=" * 50)
        print("BENCHMARK SUMMARY")
        print("=" * 50)
        
        for result in self.results:
            print(f"\n{result['algorithm']}:")
            print("-" * 30)
            print(result['output'])

def main():
    runner = BenchmarkRunner()
    
    # Compile benchmarks
    if not runner.ensure_compiled():
        sys.exit(1)
    
    # Run all benchmarks
    runner.run_all_benchmarks()
    
    # Display results
    runner.display_summary()
    
    # Save results
    runner.save_results()

if __name__ == '__main__':
    main()
