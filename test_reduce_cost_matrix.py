from tsp_solve import reduce_cost_matrix
import math

def test_reduced_cost_matrix_1():
    matrix = [
        [math.inf, 3, 4, 2, 7],
        [3, math.inf, 4, 6, 3],
        [4, 4, math.inf, 5, 8],
        [2, 6, 5, math.inf, 6],
        [7, 3, 8, 6, math.inf]
    ]

    reduced, cost = reduce_cost_matrix(matrix)

    assert cost == 15

    expected = [
        [math.inf, 1, 1, 0, 5],
        [0, math.inf, 0, 3, 0],
        [0, 0, math.inf, 1, 4],
        [0, 4, 2, math.inf, 4],
        [4, 0, 4, 3, math.inf]
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            assert reduced[i][j] == expected[i][j]


def test_reduced_cost_matrix_2():
    matrix = [
        [math.inf, 10, 15, 20],
        [10, math.inf, 35, 25],
        [15, 35, math.inf, 30],
        [20, 25, 30, math.inf]
    ]

    reduced, cost = reduce_cost_matrix(matrix)

    assert cost == 70

    expected = [
        [math.inf, 0, 0, 0],
        [0, math.inf, 20, 5],
        [0, 20, math.inf, 5],
        [0, 5, 5, math.inf]
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            assert reduced[i][j] == expected[i][j]
