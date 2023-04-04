from hw1.hw1_tasks.task04 import check_sum_of_four
import pytest
from typing import List


@pytest.mark.parametrize('a, b, c, d, expected_result', [([1, 2, 3, -1, -2, -3], [0, 1, -1, 2, -2, 3],
                                                          [-2, 4, -4, 0], [1, -1, 2, -2], 49),
                                                         ([-2, 3, 1, 5], [4, -1, 2, -3],
                                                          [-3, -1, 4, 6], [1, 2, 3, -6], 20),
                                                         ([2, 3, 1, 5], [4, 1, 2, 3],
                                                          [3, 1, 4, 6], [1, 2, 3, 6], 0)])
def test_check_sum_positive(a: List, b: List, c: List, d: List, expected_result: int):
    assert check_sum_of_four(a, b, c, d) == expected_result


@pytest.mark.parametrize('a, b, c, d, not_expected_result',
                         [([1, 2, 3, -1, -2, -3], [0, 1, -1, 2, -2, 3],
                           [-2, 4, -4, 0], [1, -1, 2, -2], 123),
                          ([-2, 3, 1, 5], [4, -1, 2, -3],
                           [-3, -1, 4, 6], [1, 2, 3, -6], 0),
                          ([2, 3, 1, 5], [4, 1, 2, 3],
                           [3, 1, 4, 6], [1, 2, 3, 6], 4)])
def test_check_sum_of_four_negative(a: List, b: List, c: List, d: List, not_expected_result: int):
    assert check_sum_of_four(a, b, c, d) != not_expected_result


@pytest.mark.parametrize('wrong_a, wrong_b, wrong_c, wrong_d, exception', [(1, 3, 0, '1', TypeError),
                                                                           (1, '2', 'a', 1, TypeError),
                                                                           ([1, 3], 1, '1', 0, TypeError)])
def test_check_sum_of_four_exception(wrong_a: List, wrong_b: List, wrong_c: List, wrong_d: List, exception: Exception):
    with pytest.raises(exception):
        check_sum_of_four(wrong_a, wrong_b, wrong_c, wrong_d)
