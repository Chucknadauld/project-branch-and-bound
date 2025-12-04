import math
import heapq
from copy import deepcopy
from tsp_core import Timer, generate_network, score_tour, SolutionStats
from tsp_solve import PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST, reduce_cost_matrix, greedy_tour
from tsp_cuttree import CutTree

params = deepcopy(PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST)
timeout = params.pop('timeout')
locations, edges = generate_network(**params)

n = len(edges)
stats = []

greedy_timer = Timer(5)
greedy_stats = greedy_tour(edges, greedy_timer)
bssf = greedy_stats[-1].score if greedy_stats and not math.isinf(greedy_stats[-1].score) else math.inf
if greedy_stats and not math.isinf(bssf):
    stats.extend(greedy_stats)

print(f"BSSF from greedy: {bssf}")

max_queue_size = 0
n_nodes_expanded = 0
n_nodes_pruned = 0
cut_tree = CutTree(n)

initial_matrix, initial_cost = reduce_cost_matrix(edges)
counter = 0
pq = []
for start_city in range(min(5, n)):
    pq.append((initial_cost - 0.5, counter, [start_city], {start_city}, initial_matrix, initial_cost))
    counter += 1
heapq.heapify(pq)
max_queue_size = max(max_queue_size, len(pq))

print(f"Initial queue size: {len(pq)}")
print(f"Initial lower bound: {initial_cost}")

timer = Timer(timeout)
iterations = 0
while pq and not timer.time_out() and iterations < 100:
    iterations += 1

    _, _, path, path_set, matrix, lower_bound = heapq.heappop(pq)

    print(f"\nIteration {iterations}")
    print(f"  Path: {path}, Lower bound: {lower_bound}, BSSF: {bssf}")

    if lower_bound >= bssf:
        print(f"  PRUNED: lower_bound ({lower_bound}) >= bssf ({bssf})")
        n_nodes_pruned += 1
        cut_tree.cut(path)
        continue

    if len(path) == n:
        print(f"  Complete tour found!")
        if math.isinf(edges[path[-1]][path[0]]):
            n_nodes_pruned += 1
            cut_tree.cut(path)
            continue

        cost = score_tour(path, edges)
        if cost < bssf:
            bssf = cost
            print(f"  NEW BSSF: {bssf}")
        continue

    current = path[-1]
    children_added = 0
    for next_city in range(n):
        if next_city in path_set:
            continue
        if math.isinf(matrix[current][next_city]):
            n_nodes_pruned += 1
            cut_tree.cut(path + [next_city])
            continue

        child_matrix = [row[:] for row in matrix]
        child_cost = lower_bound + child_matrix[current][next_city]

        for i in range(n):
            child_matrix[current][i] = math.inf
            child_matrix[i][next_city] = math.inf
        child_matrix[next_city][path[0]] = math.inf

        reduced_matrix, reduction = reduce_cost_matrix(child_matrix)
        child_cost += reduction

        if child_cost >= bssf:
            n_nodes_pruned += 1
            cut_tree.cut(path + [next_city])
            continue

        n_nodes_expanded += 1
        new_path_set = path_set | {next_city}
        new_path = path + [next_city]
        depth_priority = child_cost - len(new_path) * 0.5
        heapq.heappush(pq, (depth_priority, counter, new_path, new_path_set, reduced_matrix, child_cost))
        counter += 1
        children_added += 1

    print(f"  Expanded {children_added} children")
    max_queue_size = max(max_queue_size, len(pq))

print(f"\n\nFinal stats:")
print(f"Nodes expanded: {n_nodes_expanded}")
print(f"Nodes pruned: {n_nodes_pruned}")
print(f"Max queue size: {max_queue_size}")
print(f"Final BSSF: {bssf}")
