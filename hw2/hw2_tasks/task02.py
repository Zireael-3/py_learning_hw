"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than others.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """function that finds the most common and the least common elements
    using the dictionary with the number of occurrences"""
    quantity = {}
    for num in inp:
        if num in quantity:
            quantity[num] += 1
        else:
            quantity[num] = 1
    m_common = None
    l_common = None
    for key, value in quantity.items():
        if m_common is None or value > quantity[m_common]:
            m_common = key
        if l_common is None or value < quantity[l_common]:
            l_common = key
    result = [int(m_common), int(l_common)]
    return result

