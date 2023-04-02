from hw3.hw3_tasks.task03 import Filter
import pytest
from typing import List
from collections.abc import Callable


@pytest.mark.parametrize('input_functions, range_num, expected_result', [([lambda a: a % 2 == 0, lambda a: a > 0,
                                                                           lambda a: isinstance(a, int)], 100,
                                                                          [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24,
                                                                           26,
                                                                           28, 30,
                                                                           32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52,
                                                                           54,
                                                                           56, 58, 60,
                                                                           62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82,
                                                                           84,
                                                                           86, 88, 90, 92, 94, 96, 98]),
                                                                         ([lambda a: a % 16 == 0, lambda a: a > 20,
                                                                           lambda a: isinstance(a, int)], 500,
                                                                          [32, 48, 64, 80, 96, 112, 128, 144, 160, 176,
                                                                           192, 208, 224, 240, 256, 272, 288, 304, 320,
                                                                           336, 352, 368, 384, 400, 416, 432, 448, 464,
                                                                           480, 496])])
def test_Filter_positive(input_functions: Callable, range_num: int, expected_result: List):
    assert Filter(*input_functions).apply(range(range_num)) == expected_result


@pytest.mark.parametrize('input_functions, range_num, not_expected_result', [([lambda a: a % 2 == 0, lambda a: a > 0,
                                                                               lambda a: isinstance(a, int)], 100,
                                                                              [1, 3, 5, 7, 9]),
                                                                             ([lambda a: a % 16 == 0, lambda a: a > 20,
                                                                               lambda a: isinstance(a, int)], 500,
                                                                              [32, 48, 384, 400, 416, 432, 448, 464,
                                                                               480, 496])])
def test_Filter_negative(input_functions: List, range_num: int, not_expected_result: List):
    assert Filter(*input_functions).apply(range(range_num)) != not_expected_result


@pytest.mark.parametrize('input_functions, wrong_range_num, exception', [([lambda a: a % 2 == 0, lambda a: a > 0,
                                                                           lambda a: isinstance(a, int)], '2112',
                                                                          TypeError),
                                                                         ([lambda a: a % 16 == 0,
                                                                           lambda a: a > 20,
                                                                           lambda a: isinstance(a, int)],
                                                                          [12, 2], TypeError)])
def test_Filter_exception(input_functions: Callable, wrong_range_num: int, exception: Exception):
    with pytest.raises(exception):
        Filter(*input_functions).apply(range(wrong_range_num))
