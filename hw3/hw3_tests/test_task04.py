from hw3.hw3_tasks.task04 import is_armstrong
import pytest


@pytest.mark.parametrize('input, expected_result', [(153, True), (370, True), (9, True), (371, True), (10, False)])
def test_is_armstrong_positive(input: int, expected_result: bool):
    assert is_armstrong(input) == expected_result


@pytest.mark.parametrize('input, not_expected_result', [(153, False), (10, True), (12, True), (371, False)])
def test_is_armstrong_negative(input: int, not_expected_result: bool):
    assert is_armstrong(input) != not_expected_result


@pytest.mark.parametrize('wrong_input, exception', [({12}, ValueError), ('a', ValueError), ([1], ValueError)])
def test_is_armstrong_exceptions(wrong_input, exception: Exception):
    with pytest.raises(exception):
        is_armstrong(wrong_input)
