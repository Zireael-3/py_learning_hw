"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


>>> fizzbuzz(5)
['1', '2', 'fizz', '4', 'buzz']

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """function returns fizzbuzz sequence as list of str args
        To run doctest:
            1) Open the directory containing test_task04.py file:
                Input in the command line:
                    cd \hw4\hw4_tests
            2) And then run it
                shift + f10 buttons
                    or
                python test_task04.py
        """
    fizz_buzz_list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz_list.append('fizzbuzz')
        elif i % 3 == 0:
            fizz_buzz_list.append('fizz')
        elif i % 5 == 0:
            fizz_buzz_list.append('buzz')
        else:
            fizz_buzz_list.append(f'{i}')
    return fizz_buzz_list
