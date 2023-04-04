"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    With a large number of elements, we get a degree of complexity of 10 ^ 4,
        which is not good, but I did not find another solution
    """
    res = 0
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                for f in range(len(d)):
                    if a[i] + b[j] + c[k] + d[f] == 0:
                        res += 1
    return res
