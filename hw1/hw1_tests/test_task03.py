from hw1.hw1_tasks.task03 import find_maximum_and_minimum
import pytest


@pytest.mark.parametrize('input, expected_result',
                         [('E:\Study\Python\py_learning_hw\hw1\hw1_tests\max_min1.txt', [1, 312]),
                          ('E:\Study\Python\py_learning_hw\hw1\hw1_tests\max_min2.txt', [2, 56])])
def test_finding_max_and_min_positive(input: str, expected_result: tuple[int, int]):
    assert find_maximum_and_minimum(input) == expected_result


@pytest.mark.parametrize('input, not_expected_result',
                         [('E:\Study\Python\py_learning_hw\hw1\hw1_tests\max_min1.txt', [1, 0]),
                          ('E:\Study\Python\py_learning_hw\hw1\hw1_tests\max_min2.txt', [22, 2])])
def test_finding_max_and_min_negative(input: str, not_expected_result: tuple[int, int]):
    assert find_maximum_and_minimum(input) != not_expected_result


@pytest.mark.parametrize('input, exception',
                         [('w.txt', FileNotFoundError),
                          ('E:\Study\Python\py_learning_hw\hw1\hw1_tests\w.txt', FileNotFoundError),
                          ('E:\Study\Python\py_learning_hw\hw1\hw1_tests\max_min8.txt', FileNotFoundError)])
def test_finding_max_and_min_exceptions(input: str, exception: Exception):
    with pytest.raises(exception):
        find_maximum_and_minimum(input)
