from hw6.hw6_tasks.task_02 import backspace_compare
import pytest


@pytest.mark.parametrize("input_first, input_second, expected_result", [("ab#c", "ad#c", True),
                                                                        ("abfgs#f##asf", "ad#c", False),
                                                                        ("xcccs#pp", "xcccE#pp", True),
                                                                        ("a#d", "b", False)])
def test_backspace_compare_positive(input_first: str, input_second: str, expected_result: bool):
    assert backspace_compare(input_first, input_second) == expected_result


@pytest.mark.parametrize("input_first, input_second, expected_result", [("ab#c", "ad#c", False),
                                                                        ("abfgs#f##asf", "ad#c", True),
                                                                        ("xcccs#pp", "xcccE#pp", False),
                                                                        ("a#d", "b", True)])
def test_backspace_compare_negative(input_first: str, input_second: str, expected_result: bool):
    assert backspace_compare(input_first, input_second) != expected_result


@pytest.mark.parametrize("mb_wrong_input_first, mb_wrong_input_second, exception", [([123], "ad#c", TypeError),
                                                                                    ({12: "12"}, "ad#c",
                                                                                     TypeError),
                                                                                    (700, "xcccE#pp", TypeError),
                                                                                    ("a#d", 12, TypeError)])
def test_backspace_compare_exception(mb_wrong_input_first: str, mb_wrong_input_second: str, exception: Exception):
    with pytest.raises(exception):
        backspace_compare(mb_wrong_input_first, mb_wrong_input_second)