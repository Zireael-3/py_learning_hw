from hw2.hw2_tasks.task04 import cache


def test_cache_function():
    """Test to check coincidence of results.
    I tried to determine the difference in the speed of the function execution for the first and subsequent times,
        but without success"""
    def add_numbers(a, b):
        return a + b
    cached_add_numbers = cache(add_numbers)
    result1 = cached_add_numbers(2, 3)
    result2 = cached_add_numbers(2, 3)
    assert result1 == result2
    result3 = cached_add_numbers(3, 4)
    assert result3 == 7
