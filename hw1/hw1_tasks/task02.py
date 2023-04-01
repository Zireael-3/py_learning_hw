"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    The function checks if each member of the sequence is a fibonacci number
    and checks the sequence itself for the fibonacci rule
    """
    if len(data) < 3:
        return False
    else:
        for j in range(len(data)):
            """
            Checking the basic rule of Fib Seq:
            """
            if j >= 2:
                if data[j - 2] + data[j - 1] != data[j]:
                    return False
            i = data[j]

            """
            Checking if the num is fib num:
            """
            a = 0
            b = 1
            if i == a or i == b:
                continue
            c = a + b
            while c < i:
                a = b
                b = c
                c = a + b
            if c != i:
                return False
    return True

