from tsp_core import Timer, generate_network, score_tour
from tsp_solve import branch_and_bound
from copy import deepcopy

sizes = [5, 10, 15, 20, 30, 50]
seeds = [100, 200, 300, 400, 500, 600]

print("| N   | Seed | Solution | time (ms) |")
print("|-----|------|----------|-----------|")

for n, seed in zip(sizes, seeds):
    locations, edges = generate_network(
        n,
        euclidean=True,
        reduction=0.2,
        normal=False,
        seed=seed
    )
    
    timer = Timer(120)
    stats = branch_and_bound(deepcopy(edges), timer)
    
    if stats and len(stats[-1].tour) > 0:
        final_score = stats[-1].score
        final_time_ms = stats[-1].time * 1000
        print(f"| {n:<3} | {seed:<4} | {final_score:<8.3f} | {final_time_ms:<9.2f} |")
    else:
        print(f"| {n:<3} | {seed:<4} | timeout  | timeout   |")