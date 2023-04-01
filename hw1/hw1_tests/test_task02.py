import pytest

from typing import List

from hw1.hw1_tasks import task02


@pytest.mark.parametrize('input_sequence', [([0, 1, 1, 2, 3, 5, 8, 13]),
                                            ([1, 2, 3, 5]),
                                            ([3, 5, 8]),
                                            ([55, 89, 144, 233]),
                                            ([0, 1, 1])])
def test_check_fib_positive(input_sequence: List):
    assert task02.check_fibonacci(input_sequence)


@pytest.mark.parametrize('wrong_input_sequence', [([0, 1]),
                                                  ([0, 8, 6, 4]),
                                                  ([8, 5, 3, 2, 1, 1, 0])])
def test_check_fib_negative(wrong_input_sequence: List):
    assert not task02.check_fibonacci(wrong_input_sequence)


@pytest.mark.parametrize('not_sequence, exception', [(11, TypeError),
                                                     (0, TypeError),
                                                     ('1, 2', TypeError)])
def test_check_fib_exceptions(not_sequence: List, exception: Exception):
    with pytest.raises(exception):
        task02.check_fibonacci(not_sequence)
