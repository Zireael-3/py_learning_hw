"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""

from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    else:
        for i in range(2, len(data)):
            a = 0
            b = 1
            for j in range(i):
                a = b
                b = a + b
                if j != b:
                    return False
            if data[i - 2] + data[i - 1] != data[i]:
                return False
            return True


Sequence = [8, 13, 21]
print(check_fibonacci(Sequence))
