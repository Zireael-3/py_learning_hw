"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    """function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one"""
    result = []
    i_list = 0
    j_list = 1
    while i_list < len(args):
        while j_list < len(args):
            for i in args[i_list]:
                for j in args[j_list]:
                    result.append([i, j])
            j_list += 1
        i_list += 1
    return result

print(combinations([1, 2], [3, 4], [5, 6]))