from hw1.hw1_tasks.task05 import find_maximal_subarray_sum
import pytest
from typing import List


@pytest.mark.parametrize('input_nums, input_k, expected_result', [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
                                                                  ([2, 5, 6, 7, 3, 12, 3, 0, 33, 1], 12, 72),
                                                                  ([132, -34, 22, -1, 231, 3], 100, 353)])
def test_find_maximal_subarray_sum_positive(input_nums: List[int], input_k: int, expected_result: int):
    assert find_maximal_subarray_sum(input_nums, input_k) == expected_result


@pytest.mark.parametrize('input_nums, input_k, not_expected_result', [([1, 3, -1, -3, 5, 3, 6, 7], 3, 2),
                                                                      ([2, 5, 6, 7, 3, 12, 3, 0, 33, 1], 12, 0),
                                                                      ([132, -34, 22, -1, 231, 3], 100, 322)])
def test_find_maximal_subarray_sum_negative(input_nums: List[int], input_k: int, not_expected_result: int):
    assert find_maximal_subarray_sum(input_nums, input_k) != not_expected_result


@pytest.mark.parametrize('input_nums, input_k, exceptions', [([1, 3, -1, -3, 5, 3, 6, 7], [1, 2], TypeError),
                                                             ([2, 5, 6, 7, 3, 12, 3, 0, 33, 1], '12', TypeError),
                                                             ("132, -34, 22, -1, 231, 3", 100, TypeError)])
def test_find_maximal_subarray_sum_exceptions(input_nums: List[int], input_k: int, exceptions: Exception):
    with pytest.raises(exceptions):
        find_maximal_subarray_sum(input_nums, input_k)
