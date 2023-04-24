from typing import List

from hw6.hw6_tasks.task_03 import tic_tac_toe_checker
import pytest


@pytest.mark.parametrize("input, expected_result", [([['-', '-', 'o'], ['-', 'x', 'o'], ['x', 'o', 'x']], "unfinished"),
                                                    ([['-', '-', 'o'], ['-', 'o', 'o'], ['x', 'x', 'x']], "x wins!"),
                                                    ([['-', '-', 'o'], ['-', 'o', 'o'], ['o', 'x', 'x']], "o wins!")])
def test_tic_tac_toe_checker_positive(input: List[List], expected_result: str):
    assert tic_tac_toe_checker(input) == expected_result


@pytest.mark.parametrize("input, not_expected_result", [([['-', '-', 'o'], ['-', 'x', 'o'], ['x', 'o', 'x']], 1),
                                                    ([['-', '-', 'o'], ['-', 'o', 'o'], ['x', 'x', 'x']], "o wins!"),
                                                    ([['-', '-', 'o'], ['-', 'o', 'o'], ['o', 'x', 'x']], "frl")])
def test_tic_tac_toe_checker_negative(input: List[List], not_expected_result: str):
    assert tic_tac_toe_checker(input) != not_expected_result


@pytest.mark.parametrize("wrong_input, exception", [([12], TypeError),
                                                    ("-, 2, x", TypeError),
                                                    (3219, TypeError)])
def test_tic_tac_toe_checker_exception(wrong_input: List[List], exception: Exception):
    with pytest.raises(exception):
        test_tic_tac_toe_checker_positive(wrong_input)