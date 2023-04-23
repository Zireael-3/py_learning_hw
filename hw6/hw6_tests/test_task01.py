from hw6.hw6_tasks.task_01 import find_occurrences
import pytest


example_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simpl", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "BLUE", {"nested_key": "RED"}],
            }
        },
        "fourth": "RED",
    }


@pytest.mark.parametrize("input_element, expected_result", [("RED", 6),
                                                            (["simpl", "list", "of", "RED", "valued"], 1),
                                                            ("BLUE", 3)])
def test_find_occurrences_positive(input_element: str, expected_result: int):
    assert find_occurrences(example_tree, input_element) == expected_result


@pytest.mark.parametrize("input_element, not_expected_result", [("RED", 5), ("of", 1), ("BLUE", 8)])
def test_find_occurrences_negative(input_element: str, not_expected_result: int):
    assert find_occurrences(example_tree, input_element) != not_expected_result
