from tsp_core import Timer, generate_network, score_tour
from tsp_solve import branch_and_bound, branch_and_bound_smart
from copy import deepcopy

n = 14
timeout = 10
results = []

print("Running 20 different seeds...")
print()

for seed in range(1, 21):
    locations, edges = generate_network(
        n,
        euclidean=True,
        reduction=0.2,
        normal=False,
        seed=seed
    )
    
    timer1 = Timer(timeout)
    bnb_stats = branch_and_bound(deepcopy(edges), timer1)
    bnb_score = score_tour(bnb_stats[-1].tour, edges) if bnb_stats and len(bnb_stats[-1].tour) > 0 else float('inf')
    
    timer2 = Timer(timeout)
    smart_stats = branch_and_bound_smart(deepcopy(edges), timer2)
    smart_score = score_tour(smart_stats[-1].tour, edges) if smart_stats and len(smart_stats[-1].tour) > 0 else float('inf')
    
    improvement = ((bnb_score - smart_score) / bnb_score) * 100 if bnb_score > 0 else 0
    
    results.append({
        'seed': seed,
        'bnb_score': bnb_score,
        'smart_score': smart_score,
        'improvement': improvement
    })
    
    print(f"Seed {seed:2d}: Regular={bnb_score:.3f}, Smart={smart_score:.3f}, Improvement={improvement:.1f}%")

print("\n\nMarkdown Table:")
print("| Seed | Regular B&B | Smart B&B | Improvement |")
print("|------|-------------|-----------|-------------|")
for r in results:
    print(f"| {r['seed']:<4} | {r['bnb_score']:<11.3f} | {r['smart_score']:<9.3f} | {r['improvement']:<11.1f}% |")

avg_improvement = sum(r['improvement'] for r in results) / len(results)
print(f"\nAverage improvement: {avg_improvement:.1f}%")

import matplotlib.pyplot as plt

seeds = [r['seed'] for r in results]
bnb_scores = [r['bnb_score'] for r in results]
smart_scores = [r['smart_score'] for r in results]

plt.figure(figsize=(10, 6))
plt.plot(seeds, bnb_scores, marker='o', label='Regular B&B', linewidth=2)
plt.plot(seeds, smart_scores, marker='s', label='Smart B&B', linewidth=2)
plt.xlabel('Seed')
plt.ylabel('Tour Score')
plt.title('Regular B&B vs Smart B&B Across 20 Seeds')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('smart_comparison.png')
print("\nPlot saved as 'smart_comparison.png'")