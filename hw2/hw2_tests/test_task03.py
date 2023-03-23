from hw2.hw2_tasks.task03 import combinations


def test_combinations_positive():
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]
    assert combinations([1, 2], [3, 4], [5, 6]) == [[1, 3], [1, 4], [2, 3], [2, 4], [1, 5], [1, 6], [2, 5], [2, 6]]


