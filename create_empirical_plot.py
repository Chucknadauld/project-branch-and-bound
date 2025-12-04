import matplotlib.pyplot as plt
import numpy as np

n_values = [5, 10, 15, 20, 30, 50]
times_ms = [0.01, 69.18, 6188.22, 0.17, 0.13, 4.16]

times_sec = [t / 1000 for t in times_ms]

k = 3
theoretical = [k ** n for n in n_values]

c = times_sec[2] / theoretical[2]
theoretical_scaled = [c * t for t in theoretical]

plt.figure(figsize=(10, 6))
plt.plot(n_values, times_sec, marker='o', label='Empirical', linewidth=2)
plt.plot(n_values, theoretical_scaled, marker='s', linestyle='--', label=f'Theoretical (k={k})', linewidth=2)
plt.xlabel('Number of Cities (n)')
plt.ylabel('Time (seconds)')
plt.title('Branch and Bound: Empirical vs Theoretical Complexity')
plt.legend()
plt.yscale('log')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('empirical_comparison.png')
print("Plot saved as 'empirical_comparison.png'")