"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    """
    Сheckin subarrays and the sum of the elements, no longer than k
    """
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(len(nums)):
            """
            length should be less equal to "k"
            """
            if i - j < k:
                curr_sum += nums[j]
        max_sum = curr_sum
    return max_sum

