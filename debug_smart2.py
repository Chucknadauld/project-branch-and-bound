from copy import deepcopy
from tsp_core import Timer, generate_network, score_tour
from tsp_solve import branch_and_bound, branch_and_bound_smart, PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST, reduce_cost_matrix

params = deepcopy(PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST)
timeout = params.pop('timeout')
locations, edges = generate_network(**params)

from tsp_solve import greedy_tour
greedy_timer = Timer(5)
greedy_stats = greedy_tour(deepcopy(edges), greedy_timer)
greedy_score = greedy_stats[-1].score
print(f"Greedy score: {greedy_score}")

initial_matrix, initial_cost = reduce_cost_matrix(edges)
print(f"Initial lower bound: {initial_cost}")
print(f"Greedy BSSF: {greedy_score}")
print(f"Can we beat greedy from city 0? {initial_cost < greedy_score}")
