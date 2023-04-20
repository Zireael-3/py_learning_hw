from hw4.hw4_tasks.task05 import fizzbuzz
import pytest


@pytest.mark.parametrize("input, expected_result", [(20,
                                                     ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz',
                                                      '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17', 'fizz', '19',
                                                      'buzz'])])
def test_fizzbuzz_positive(input: int, expected_result: list):
    assert list(fizzbuzz(input)) == expected_result


@pytest.mark.parametrize("input, not_expected_result", [(10,
                                                         ['1', '2', 'buzz', '4', 'buzz', 'fizz', '7', '8', 'fizz',
                                                          'buzz'])])
def test_fizzbuzz_negative(input: int, not_expected_result: list):
    assert list(fizzbuzz(input)) != not_expected_result


@pytest.mark.parametrize("wrong_input, exception", [('wds', TypeError),
                                                    ([21], TypeError)])
def test_fizzbuzz_exception(wrong_input: int, exception: Exception):
    with pytest.raises(exception):
        list(fizzbuzz(wrong_input))
