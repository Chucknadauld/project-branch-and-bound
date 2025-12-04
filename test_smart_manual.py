from copy import deepcopy
from tsp_core import Timer, generate_network, score_tour
from tsp_solve import branch_and_bound, branch_and_bound_smart, PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST

params = deepcopy(PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST)
timeout = params.pop('timeout')
locations, edges = generate_network(**params)

print("=" * 60)
print("Testing Regular B&B")
print("=" * 60)
timer = Timer(timeout)
bnb_stats = branch_and_bound(deepcopy(edges), timer)
bnb_score = score_tour(bnb_stats[-1].tour, edges)
print(f"Regular B&B score: {bnb_score}")
print(f"Number of solutions: {len(bnb_stats)}")
for i, stat in enumerate(bnb_stats):
    print(f"  Solution {i}: score={stat.score}, nodes_exp={stat.n_nodes_expanded}, tour={stat.tour}")

print("\n" + "=" * 60)
print("Testing Smart B&B")
print("=" * 60)
timer = Timer(timeout)
smart_stats = branch_and_bound_smart(deepcopy(edges), timer)
smart_score = score_tour(smart_stats[-1].tour, edges)
print(f"Smart B&B score: {smart_score}")
print(f"Number of solutions: {len(smart_stats)}")
for i, stat in enumerate(smart_stats):
    print(f"  Solution {i}: score={stat.score}, nodes_exp={stat.n_nodes_expanded}, tour={stat.tour}")

print("\n" + "=" * 60)
print(f"Regular B&B final score: {bnb_score}")
print(f"Smart B&B final score: {smart_score}")
print(f"Smart better than regular? {smart_score < bnb_score}")
