from copy import deepcopy
from tsp_core import Timer, generate_network, score_tour
from tsp_solve import branch_and_bound, branch_and_bound_smart, PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST

params = deepcopy(PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST)
timeout = params.pop('timeout')
locations, edges = generate_network(**params)

print("Running greedy...")
from tsp_solve import greedy_tour
greedy_timer = Timer(5)
greedy_stats = greedy_tour(deepcopy(edges), greedy_timer)
greedy_score = score_tour(greedy_stats[-1].tour, edges)
print(f"Greedy score: {greedy_score}")
print(f"Greedy tour: {greedy_stats[-1].tour}")
print()

print("Running regular B&B...")
timer = Timer(timeout)
bnb_stats = branch_and_bound(deepcopy(edges), timer)
bnb_score = score_tour(bnb_stats[-1].tour, edges)
print(f"Regular B&B score: {bnb_score}")
print(f"Regular B&B tour: {bnb_stats[-1].tour}")
print(f"Nodes expanded: {bnb_stats[-1].n_nodes_expanded}")
print(f"Nodes pruned: {bnb_stats[-1].n_nodes_pruned}")
print(f"Max queue size: {bnb_stats[-1].max_queue_size}")
print(f"Number of solutions found: {len(bnb_stats)}")
print()

print("Running smart B&B...")
timer = Timer(timeout)
stats = branch_and_bound_smart(deepcopy(edges), timer)
smart_score = score_tour(stats[-1].tour, edges)
print(f"Smart B&B score: {smart_score}")
print(f"Smart B&B tour: {stats[-1].tour}")
print(f"Nodes expanded: {stats[-1].n_nodes_expanded}")
print(f"Nodes pruned: {stats[-1].n_nodes_pruned}")
print(f"Max queue size: {stats[-1].max_queue_size}")
print(f"Number of solutions found: {len(stats)}")
