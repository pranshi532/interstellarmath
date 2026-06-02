Mathematical Universality: Evaluating Prime-Based Encoding Schemes for Interstellar Communication
"If we ever receive a signal from the stars, how will we know it’s not just cosmic noise? Mathematics is the only universal language."
This is a terminal-based Python research project that investigates a fundamental question in astrobiology and information theory: Are prime-number-based messages more recognizable and resilient than other mathematical sequences when transmitted through noisy, deep-space environments?
Built entirely from scratch using only the Python Standard Library, this project simulates interstellar signal degradation, applies custom error-detection encoding, and evaluates sequence survival using original, mathematically derived resilience metrics.
💡 The Motivation
In SETI (Search for Extraterrestrial Intelligence), distinguishing a deliberate signal from natural astrophysical noise (like pulsars or quasars) is the hardest challenge. Prime numbers are often proposed as the ideal "hello" because their distribution is deterministic yet non-repeating, giving them high Kolmogorov complexity.
I built this project to test that hypothesis empirically. By pitting prime numbers against Fibonacci sequences, perfect squares, and triangular numbers under simulated cosmic noise, we can mathematically quantify which structure survives transmission best.
🚀 Core Features
🧮 Sequence Generator: Deterministically generates Prime, Fibonacci, Square, and Triangular sequences with O(n) to O(nloglogn) efficiency.
📡 Custom Binary Encoding: Converts integers to base-2 and appends a modular parity bit (p=∑b_imod2) for structural verification.
🌩️ Stochastic Noise Simulation: Models deep-space channel degradation using independent Bernoulli trials (bit-flip probability p).
📊 Original Resilience Metrics: Calculates custom information-theoretic scores, including Pattern Preservation Score (PPS) and Recognition Probability (RP).
🖥️ Zero-Dependency Architecture: Runs entirely in the terminal. No pip install, no external packages, no bloat.

How to use this project:
This is a terminal based python application so you have to download the files to run the project , after downloading just write python main.py on the terminal and see the project running :))
