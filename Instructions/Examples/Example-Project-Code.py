# Project Example Code

def fib_recursive(n):
    """Calculates the fibonacci sequence using recursion"""
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    """Calculates the fibonacci sequence using iteration"""
    if n < 2:
        return n

    seq = [0, 1]
    for i in range(1, n):
        seq.append(seq[i] + seq[i - 1])
    return seq[-1]


def fib_fancy(n, m):
    """Calculates a fancy fibonacci number"""
    total = 0
    for i in range(n):
        for j in range(n):
            total += fib_recursive(m)
    return total