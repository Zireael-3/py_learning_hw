import os
from hw4.hw4_tasks.task01 import read_magic_number
import pytest


@pytest.fixture()
def clean_up(autouse=True):
    # Delete a temporary file before the test runs
    if os.path.exists("testfile.txt"):
        os.remove("testfile.txt")
    yield
    # Delete the temporary file after the test completes
    if os.path.exists("testfile.txt"):
        os.remove("testfile.txt")


@pytest.mark.parametrize('input, expected_result', [('first_line.txt', True),
                                                    ('second_line.txt', False),
                                                    ('third_line.txt', False)
                                                    ])
def test_real_magic_number_positive(input: str, expected_result: bool, clean_up):
    assert read_magic_number(input) == expected_result


@pytest.mark.parametrize('input, not_expected_result', [('first_line.txt', False),
                                                        ('second_line.txt', None),
                                                        ('third_line.txt', True)
                                                        ])
def test_real_magic_number_negative(input: str, not_expected_result: bool, clean_up):
    assert read_magic_number(input) != not_expected_result


@pytest.mark.parametrize('wrong_input, exception', [('12d', FileNotFoundError),
                                                    (122, OSError),
                                                    (["dsa", "sa"], TypeError)
                                                    ])
def test_real_magic_number_exceptions(wrong_input: str, exception: Exception, clean_up):
    with pytest.raises(exception):
        read_magic_number(wrong_input)
