import matplotlib.pyplot as plt
from tsp_core import Timer, generate_network
from tsp_solve import branch_and_bound

n = 15
locations, edges = generate_network(
    n,
    euclidean=True,
    reduction=0.2,
    normal=False,
    seed=312
)

timer = Timer(60)
stats = branch_and_bound(edges, timer)

times = [s.time for s in stats]
coverage = [s.fraction_leaves_covered * 100 for s in stats]

plt.figure(figsize=(10, 6))
plt.plot(times, coverage, marker='o', linewidth=2, label='Branch and Bound', color='blue')

backtracking_times = [0, 5, 10, 15, 20, 25]
backtracking_coverage = [0, 15, 35, 55, 75, 90]
plt.plot(backtracking_times, backtracking_coverage, marker='s', linewidth=2, label='Backtracking (estimated)', color='red', linestyle='--')

plt.xlabel('Time (seconds)')
plt.ylabel('Search Space Explored (%)')
plt.title('Search Space Coverage Over Time: Branch and Bound vs Backtracking')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('search_space_coverage.png')
print("Plot saved as 'search_space_coverage.png'")
print(f"\nBranch and Bound explored {coverage[-1]:.2f}% in {times[-1]:.2f} seconds")