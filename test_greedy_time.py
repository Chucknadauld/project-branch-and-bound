from copy import deepcopy
from tsp_core import Timer, generate_network, score_tour
from tsp_solve import greedy_tour, PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST

params = deepcopy(PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST)
params.pop('timeout')
locations, edges = generate_network(**params)

print("Greedy with 2 second timer:")
timer = Timer(2)
greedy_stats = greedy_tour(edges, timer)
print(f"Number of solutions: {len(greedy_stats)}")
for i, stat in enumerate(greedy_stats):
    print(f"  Solution {i}: score={stat.score}, tour starts with {stat.tour[0]}")

print("\nGreedy with 5 second timer:")
timer = Timer(5)
greedy_stats = greedy_tour(edges, timer)
print(f"Number of solutions: {len(greedy_stats)}")
for i, stat in enumerate(greedy_stats):
    print(f"  Solution {i}: score={stat.score}, tour starts with {stat.tour[0]}")
