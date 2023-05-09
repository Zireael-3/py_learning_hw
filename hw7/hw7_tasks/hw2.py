"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class Supressor:
    def __int__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == self.exception:
            return True


@contextmanager
def suppressor(exception):
    try:
        yield
    except exception:
        pass
