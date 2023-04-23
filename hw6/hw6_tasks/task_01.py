"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contain basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    count = 0
    for value in tree.values():
        if value == element:
            count += 1
        elif isinstance(value, (list, tuple, set)):
            count += value.count(element)
            for i in value:
                if isinstance(i, dict):
                    count += find_occurrences(i, element)
        elif isinstance(value, dict):
            count += find_occurrences(value, element)
    return count


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
