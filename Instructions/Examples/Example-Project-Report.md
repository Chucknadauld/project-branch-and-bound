# Project Fib

## Baseline

### Theoretical Time Analysis for fib_iter

#### fib_iterative

```py
def fib_iterative(n):
    """Calculates the fibonacci sequence using iteration"""
    if n < 2:                                           # O(1) - comparison is constant
        return n                                        # O(1) - returning is constant

    seq = [0, 1]                                        # O(1) - declaring variables is constant
    for i in range(1, n):                               # O(n) - The overall loop is O(n) - the for loop loops n times
        seq.append(seq[i] + seq[i - 1])                 # O(1) - The python append function is constant time, and addition is also constant time
    return seq[-1]                                      # O(1) - Returning and indexing into a python list is constant time
```

The largest operation is the for loop. The loop loops n times with a constant time complexity for each loop leading to an overall time complexity of **O(n)**.

### Theoretical Space Analysis for fib_iter

#### fib_iterative

```py
def fib_iterative(n):
    """Calculates the fibonacci sequence using iteration"""
    if n < 2:
        return n

    seq = [0, 1]
    for i in range(1, n):                           # O(1) - Range has constant space complexity, see note below
        seq.append(seq[i] + seq[i - 1])             # O(n) - seq grows to the size of n
    return seq[-1]
```

For analyzing space complexity of this function, we will look at the data structures and the space complexity of the functions being called.

Within the context of this function, there is only 1 data structure being used -- `seq`. The variable declarations can be assumed to be constant time. The `seq` array will contain `n` items at the end, resulting in an overall space complexity of O(n).

The functions called within this context are `range` and `append`. The [python documentation][1] for range states that only a small amount of memory will be used as it stores only the start, stop, and step values. Thus, range results in O(1) space complexity. The built in `append` function does not use additional space complexity.

The overall space complexity is **O(n)** because the largest space complexity within the function is O(n).

### Empirical Data for fib_iter

| N   | Time (ms) |
| --- | --------- |
| 4   | 0.00129   |
| 8   | 0.00074   |
| 16  | 0.00117   |
| 32  | 0.00212   |
| 64  | 0.00527   |
| 128 | 0.00868   |

### Comparison of Theoretical and Empirical Results for fib_iter

#### Summary

- Theoretical order of growth: **O(n)**
- Measured constant of proportionality for theoretical order: **7.640625e-05**
- Empirical order of growth:
- Measured constant of proportionality for empirical order:

![Fib Iterative Plot](images/fib_iter.png)

The theoretical order of growth matches the empirical order of growth.

## Core

### Theoretical Time Analysis for fib_recursive

#### fib_recursive(n)

```py
def fib_recursive(n):                                   # O(2^n) - Overall complexity
    """Calculates the fibonacci sequence using recursion"""
    if n < 2:                                           # O(1) - comparisons are constant time
        return n                                        # O(1) - returning is constant time
    return fib_recursive(n - 1) + fib_recursive(n - 2)  # O(2^n) - recursive calls, see further explanation below, assuming addition is constant time
```

For each recursive call, it calls itself two more times.

There are `n` layers because each call only reduces n by 1.

Each layer will double because for each recursive call, it calls itself 2 more times.

Thus, if we are to think about the layers as a tree, the bottom layer would have `2^n` leaves because each layer doubles the number of leaves.

Each leaf does a constant amount of work (ie addition and comparison), so 2^n times a constant amount of work is still 2^n, thus **O(2^n)** is the overall time complexity.

### Theoretical Space Analysis for fib_recursive

#### fib_recursive(n)

```py
def fib_recursive(n):
    """Calculates the fibonacci sequence using recursion"""
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)
```

As explained earlier, there will be 2^n leaves. Assuming each recursive frame of the function takes up O(1) space on the stack, we will have 2^n frames. Thus, we will have overall space complexity of n^2 \* 1 or **O(2^n)**.

### Empirical Data for fib_recursive

| N   | Time (ms)  |
| --- | ---------- |
| 1   | 0.0        |
| 5   | 0.0        |
| 10  | 0.09997    |
| 15  | 0.59969    |
| 20  | 20.81475   |
| 25  | 252.49302  |
| 30  | 1168.91997 |

### Comparison of Theoretical and Empirical Results for fib_recursive

- Theoretical order of growth: **O(2^n)**
- Measured constant of proportionality for theoretical order: **2.6188e-05**
- Empirical order of growth: **O(1.6^n)**
- Measured constant of proportionality for empirical order: **0.00081024**

![fib recursive plot](images/fib_recursive1.png)

![fib recursive plot](images/fib_recursive2.png)

The expected analysis does not match the theoretical analysis.

If I were to call fib_recursive(7), the call tree would look like this:

```
                  7
           6              5
       5      4       4      3
     4   3  3   2   3   2  2   1
   3  2 2 1 2 1 1 0 2 1 1 0 1 0
 2 1 10 10  10     1 0
1 0

```

- fib(6) is called 1 time
- fib(5) is called 2 times
- fib(4) is called 3 times
- fib(3) is called 5 times
- fib(2) is called 8 times
- fib(1) is called 13 times
- fib(0) is called 8 times

The worse case scenario, as determined in the theoretical time complexity earlier, where all the leaves are filled in, is not correct.

If all the leaves were filled in, we would expect 32 (2^5) leaves and 63 (2^6 -1) calls.
Instead, we have 21 leaves and 40 calls. Thus, we have a fraction of the number expected.

Rather than each node expanding an average of 2 times, each node expands an average of 1.6 times (the golden ratio).

Thus, the time complexity is n^1.6 instead of n^2.

## Stretch 1

The stretch 1 report would go here

## Stretch 2

### Discussion

The stretch 1 report would go here

## Discussion With Peer

I met with John for this assignment on September 7th to discuss this assignment. We discussed how we each implemented the functions, compared theoretical analyses, compared runtimes and empirical line of best fit, and discussed our stretch 2 strategies.

We implemented the functions very similarly, except for fib iterative. Instead of using an entire list, he replaced the values as he went. So, he had a smaller space complexity than I did for fib_iterative.

John's runtimes were all faster than mine. He has a newer computer than me, so it makes sense that his times are a little bit faster. Our empirical orders of growth matched for all of our functions. John's constant of proportionalities all were a little smaller than mine. He also found that his fib_iterative empirical order of growth didn't match his theoretical order of growth.

For stretch 2, John did **_. I did not think about that when I did mine. I think it would be interesting to try that and see if I would get the same results as him. I did _** and John had not thought of that. While we were meeting, John tried my strategy and found the same result I did.

## References

[1]: https://docs.python.org/3/library/stdtypes.html#ranges "Python Documentation - Range"
