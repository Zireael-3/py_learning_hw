from hw2.hw2_tasks.task01 import get_longest_diverse_words, get_rarest_char, count_punctuation_chars, \
    count_non_ascii_chars, get_most_common_non_ascii_char
import pytest

"""
Some tests to check the first task: 
2 tests for every function (first - to check the result, second - to check the filename)
"""


@pytest.mark.parametrize("file_name, expected_result", [('data.txt',
                                                         ['alsSicherung', 'Ei-genschaft', 'Beschwörung,',
                                                          'Umschreibung',
                                                          'prakti-schen', 'fürzuständig', 'morali-schen',
                                                          'erstaunlich,',
                                                          'To-desfurcht', 'Nichtkämpfern'])])
def test_get_longest_diverse_words_result(file_name, expected_result):
    assert get_longest_diverse_words(file_name) == expected_result


@pytest.mark.parametrize('file_name, exception',
                         [('', FileNotFoundError),
                          (' ', FileNotFoundError),
                          ('idk', FileNotFoundError)])
def test_get_longest_diverse_words_exceptions(file_name, exception):
    with pytest.raises(exception):
        get_longest_diverse_words(file_name)


def test_get_rarest_char():
    assert get_rarest_char('data.txt') == "›"


@pytest.mark.parametrize('file_name, exception',
                         [('', FileNotFoundError),
                          (' ', FileNotFoundError),
                          ('idk', FileNotFoundError)])
def test_get_longest_diverse_words_exceptions(file_name, exception):
    with pytest.raises(exception):
        get_rarest_char(file_name)


def test_count_punctuation_chars():
    assert count_punctuation_chars('data.txt') == 5475


@pytest.mark.parametrize('file_name, exception',
                         [('', FileNotFoundError),
                          (' ', FileNotFoundError),
                          ('idk', FileNotFoundError)])
def test_get_longest_diverse_words_exceptions(file_name, exception):
    with pytest.raises(exception):
        count_punctuation_chars(file_name)


def test_count_non_ascii_chars():
    assert count_non_ascii_chars('data.txt') == 2972


@pytest.mark.parametrize('file_name, exception',
                         [('', FileNotFoundError),
                          (' ', FileNotFoundError),
                          ('idk', FileNotFoundError)])
def test_get_longest_diverse_words_exceptions(file_name, exception):
    with pytest.raises(exception):
        count_non_ascii_chars(file_name)


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char('data.txt') == "ä"


@pytest.mark.parametrize('file_name, exception',
                         [('', FileNotFoundError),
                          (' ', FileNotFoundError),
                          ('idk', FileNotFoundError)])
def test_get_longest_diverse_words_exceptions(file_name, exception):
    with pytest.raises(exception):
        get_most_common_non_ascii_char(file_name)
