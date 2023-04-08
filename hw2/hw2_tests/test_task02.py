from hw2.hw2_tasks.task02 import major_and_minor_elem
import pytest

"""
The condition to task02 says: 
You may assume that the array is non-empty and the most common element always exist in the array.
So, I have done only 1 test to check the result
"""


@pytest.mark.parametrize("a, expected_result", [([3, 2, 3], [3, 2]),
                                                ([2, 2, 1, 1, 1, 2, 2], [2, 1]),
                                                ([8, 8, 8, 3, 3], [8, 3])])
def test_major_and_minor_elem_positive(a, expected_result):
    assert major_and_minor_elem(a) == expected_result

