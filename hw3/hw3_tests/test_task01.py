from hw3.hw3_tasks.task01 import cache
import pytest


@cache(times=2)
def some_function(x):
    return x + 1


@pytest.mark.parametrize("input_to_some_function, expected_result", [(1, 2),
                                                                     (1, 2),
                                                                     (1, 2),
                                                                     (1, 2)])
def test_cache_positive(input_to_some_function, expected_result):
    # First call should compute the result, the rest should be returned according to times
    assert some_function(input_to_some_function) == expected_result


@cache(times=2)
def some_second_function(x):
    return x + 3


@pytest.mark.parametrize("input_to_some_second_function, not_expected_result", [(1, 4),
                                                                                (1, 4),
                                                                                (1, 4),
                                                                                (1, 4)])
def test_cache_negative(input_to_some_second_function, not_expected_result):
    assert some_function(input_to_some_second_function) != not_expected_result


@cache(times=2)
def some_function_noargs():
    return 1


@pytest.mark.parametrize("expected_result", [1,
                                             1])
def test_cache_x(expected_result):
    assert some_function_noargs() == expected_result
