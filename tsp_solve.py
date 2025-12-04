import math
import random
import heapq

from tsp_core import Tour, SolutionStats, Timer, score_tour, Solver
from tsp_cuttree import CutTree

PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST = {
    "n": 14,
    "euclidean": True,
    "reduction": 0.2,
    "normal": False,
    "seed": 42,
    "timeout" : 10
}

def reduce_cost_matrix(matrix):
    n = len(matrix)
    reduced = [row[:] for row in matrix]
    total_reduction = 0

    for i in range(n):
        min_val = min(reduced[i])
        if not math.isinf(min_val) and min_val > 0:
            total_reduction += min_val
            for j in range(n):
                if not math.isinf(reduced[i][j]):
                    reduced[i][j] -= min_val

    for j in range(n):
        col_min = min(reduced[i][j] for i in range(n))
        if not math.isinf(col_min) and col_min > 0:
            total_reduction += col_min
            for i in range(n):
                if not math.isinf(reduced[i][j]):
                    reduced[i][j] -= col_min

    return reduced, total_reduction

def random_tour(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
    stats = []
    n_nodes_expanded = 0
    n_nodes_pruned = 0
    cut_tree = CutTree(len(edges))

    while True:
        if timer.time_out():
            return stats

        tour = random.sample(list(range(len(edges))), len(edges))
        n_nodes_expanded += 1

        cost = score_tour(tour, edges)
        if math.isinf(cost):
            n_nodes_pruned += 1
            cut_tree.cut(tour)
            continue

        if stats and cost > stats[-1].score:
            n_nodes_pruned += 1
            cut_tree.cut(tour)
            continue

        stats.append(SolutionStats(
            tour=tour,
            score=cost,
            time=timer.time(),
            max_queue_size=1,
            n_nodes_expanded=n_nodes_expanded,
            n_nodes_pruned=n_nodes_pruned,
            n_leaves_covered=cut_tree.n_leaves_cut(),
            fraction_leaves_covered=cut_tree.fraction_leaves_covered()
        ))

    if not stats:
        return [SolutionStats(
            [],
            math.inf,
            timer.time(),
            1,
            n_nodes_expanded,
            n_nodes_pruned,
            cut_tree.n_leaves_cut(),
            cut_tree.fraction_leaves_covered()
        )]

def greedy_tour(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
    n = len(edges)
    stats = []

    for start in range(n):
        if timer.time_out():
            return stats if stats else [SolutionStats([], math.inf, timer.time(), 1, 0, 0, 0, 0.0)]

        tour = [start]
        visited = {start}
        current = start
        valid = True

        while len(tour) < n:
            if timer.time_out():
                return stats if stats else [SolutionStats([], math.inf, timer.time(), 1, 0, 0, 0, 0.0)]

            best_next = None
            best_weight = math.inf
            for city in range(n):
                if city in visited:
                    continue
                w = edges[current][city]
                if math.isinf(w):
                    continue
                if w < best_weight or (w == best_weight and city < (best_next if best_next is not None else n)):
                    best_weight = w
                    best_next = city

            if best_next is None:
                valid = False
                break

            tour.append(best_next)
            visited.add(best_next)
            current = best_next

        if not valid:
            continue

        if math.isinf(edges[current][start]):
            continue

        cost = score_tour(tour, edges)
        if not stats or cost < stats[-1].score:
            stats.append(SolutionStats(
                tour=tour,
                score=cost,
                time=timer.time(),
                max_queue_size=1,
                n_nodes_expanded=0,
                n_nodes_pruned=0,
                n_leaves_covered=0,
                fraction_leaves_covered=0.0
            ))

    if not stats:
        return [SolutionStats([], math.inf, timer.time(), 1, 0, 0, 0, 0.0)]

    return stats


def dfs(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
    return []


def branch_and_bound(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
    n = len(edges)
    stats = []

    greedy_timer = Timer(5)
    greedy_stats = greedy_tour(edges, greedy_timer)
    bssf = greedy_stats[-1].score if greedy_stats and not math.isinf(greedy_stats[-1].score) else math.inf
    if greedy_stats and not math.isinf(bssf):
        stats.extend(greedy_stats)

    max_queue_size = 0
    n_nodes_expanded = 0
    n_nodes_pruned = 0
    cut_tree = CutTree(n)

    initial_matrix, initial_cost = reduce_cost_matrix(edges)
    counter = 0
    pq = [(initial_cost, counter, [0], {0}, initial_matrix)]
    counter += 1
    max_queue_size = max(max_queue_size, len(pq))

    while pq and not timer.time_out():
        if len(pq) > 20000:
            pq = heapq.nsmallest(10000, pq)
            heapq.heapify(pq)

        lower_bound, _, path, path_set, matrix = heapq.heappop(pq)

        if lower_bound >= bssf:
            n_nodes_pruned += 1
            cut_tree.cut(path)
            continue

        if len(path) == n:
            if math.isinf(edges[path[-1]][path[0]]):
                n_nodes_pruned += 1
                cut_tree.cut(path)
                continue

            cost = score_tour(path, edges)
            if cost < bssf:
                bssf = cost
                stats.append(SolutionStats(
                    tour=path,
                    score=cost,
                    time=timer.time(),
                    max_queue_size=max_queue_size,
                    n_nodes_expanded=n_nodes_expanded,
                    n_nodes_pruned=n_nodes_pruned,
                    n_leaves_covered=cut_tree.n_leaves_cut(),
                    fraction_leaves_covered=cut_tree.fraction_leaves_covered()
                ))
            else:
                n_nodes_pruned += 1
                cut_tree.cut(path)
            continue

        current = path[-1]
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
            heapq.heappush(pq, (child_cost, counter, path + [next_city], new_path_set, reduced_matrix))
            counter += 1
            max_queue_size = max(max_queue_size, len(pq))

    if not stats:
        return [SolutionStats(
            [],
            math.inf,
            timer.time(),
            max_queue_size or 1,
            n_nodes_expanded,
            n_nodes_pruned,
            cut_tree.n_leaves_cut(),
            cut_tree.fraction_leaves_covered()
        )]

    return stats


def branch_and_bound_smart(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
    n = len(edges)
    stats = []

    greedy_timer = Timer(5)
    greedy_stats = greedy_tour(edges, greedy_timer)
    bssf = greedy_stats[-1].score if greedy_stats and not math.isinf(greedy_stats[-1].score) else math.inf
    if greedy_stats and not math.isinf(bssf):
        stats.extend(greedy_stats)

    max_queue_size = 0
    n_nodes_expanded = 0
    n_nodes_pruned = 0
    cut_tree = CutTree(n)

    initial_matrix, initial_cost = reduce_cost_matrix(edges)
    counter = 0
    pq = [(-1, initial_cost, counter, [0], {0}, initial_matrix)]
    counter += 1
    max_queue_size = max(max_queue_size, len(pq))

    while pq and not timer.time_out():
        if len(pq) > 50000:
            pq = heapq.nsmallest(25000, pq)
            heapq.heapify(pq)

        depth, lower_bound, _, path, path_set, matrix = heapq.heappop(pq)

        if lower_bound >= bssf:
            n_nodes_pruned += 1
            cut_tree.cut(path)
            continue

        if len(path) == n:
            if math.isinf(edges[path[-1]][path[0]]):
                n_nodes_pruned += 1
                cut_tree.cut(path)
                continue

            cost = score_tour(path, edges)
            if cost < bssf:
                bssf = cost
                stats.append(SolutionStats(
                    tour=path,
                    score=cost,
                    time=timer.time(),
                    max_queue_size=max_queue_size,
                    n_nodes_expanded=n_nodes_expanded,
                    n_nodes_pruned=n_nodes_pruned,
                    n_leaves_covered=cut_tree.n_leaves_cut(),
                    fraction_leaves_covered=cut_tree.fraction_leaves_covered()
                ))
            else:
                n_nodes_pruned += 1
                cut_tree.cut(path)
            continue

        current = path[-1]
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
            new_depth = -len(new_path)
            heapq.heappush(pq, (new_depth, child_cost, counter, new_path, new_path_set, reduced_matrix))
            counter += 1
            max_queue_size = max(max_queue_size, len(pq))

    if not stats:
        return [SolutionStats(
            [],
            math.inf,
            timer.time(),
            max_queue_size or 1,
            n_nodes_expanded,
            n_nodes_pruned,
            cut_tree.n_leaves_cut(),
            cut_tree.fraction_leaves_covered()
        )]

    return stats
