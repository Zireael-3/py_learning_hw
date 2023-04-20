"""
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number in functionally style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""
from functools import reduce


def is_armstrong(number: int) -> bool:
    """Dividing a number into digits, using map function"""
    digits = list(map(int, str(number)))
    """The power is the number of digits, so it's the length of the list"""
    power = len(digits)
    """
    Using the `reduce` function to calculate the sum of the digits raised to the power.
    The anonymous function takes two arguments x and y, where x is the result of the function
    in the previous steps, and y is the next value in the list.
    It starts from 0 as x to create an accumulative variable.
    """
    return reduce(lambda x, y: x + pow(y, power), digits, 0) == number

