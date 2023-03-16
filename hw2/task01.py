"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
import string


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path) as file:
        text = file.read().encode().decode('unicode-escape')
        text = text.replace('\n', '')
        words = text.split(' ')
        list_of_l = []
        i = 0
        while i < len(words):
            if len(set(words[i])) == len(words[i]):
                list_of_l.append(words[i])
            i += 1
        sorted_list = sorted(list_of_l, key=len)
        result = []
        j = 10
        while j > 0:
            result.append(sorted_list[-j])
            j -= 1
        return result


print(get_longest_diverse_words('data.txt'))


def get_rarest_char(file_path: str) -> str:
    with open(file_path) as file:
        text = file.read().encode().decode('unicode-escape')
        text = text.replace('\n', '')
        frequency = {}
        for char in text:
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
        rarest = min(frequency, key=frequency.get)
        return rarest


# print((get_rarest_char("data.txt")))


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path) as file:
        text = file.read().encode().decode('unicode-escape')
        text = text.replace('\n', '')
        text = text.replace(' ', '')
        count = 0
        for char in text:
            if char.isalpha():
                continue
            elif char.isdigit():
                continue
            else:
                count += 1
        return count


# print(count_punctuation_chars("data.txt"))

def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path) as file:
        text = file.read().encode().decode('unicode-escape')
        text = text.replace('\n', '')
        total_count = len(text)
        ascii_count = len(text.encode("ascii", "ignore"))
        return total_count - ascii_count


# print((count_non_ascii_chars("data.txt")))

def get_most_common_non_ascii_char(file_path: str) -> str:
    """The `string.printable` constant contains all ASCII characters that can be printed,
    which includes the digits, the letters (both lower and upper case),
    punctuation marks, and whitespace characters."""
    with open(file_path) as file:
        text = file.read().encode().decode('unicode-escape')
        text = text.replace('\n', '')
        frequency = {}
        for char in text:
            if char in string.printable:
                continue
            elif char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
        rarest = max(frequency, key=frequency.get)
        return rarest


# print(get_most_common_non_ascii_char("data.txt"))
