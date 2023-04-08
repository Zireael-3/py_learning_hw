"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from typing import List
import re


def get_longest_diverse_words(file_path: str) -> List[str]:
    """function that finds 10 longest words consisting from largest amount of unique symbols"""
    with open(file_path) as file:
        text = file.read().encode().decode('unicode-escape')
        text = text.replace('\n', '')
        text = re.sub('[.№;%:?*()_+=/!@#$]', ' ', text)
        text = re.sub(r'\d+', ' ', text)

        words = text.split(' ')
        list_of_l = []
        i = 0
        while i < len(words):
            """checkin if a word consists of unique characters"""
            if len(set(words[i])) == len(words[i]):
                list_of_l.append(words[i])
            i += 1
        sorted_list = sorted(list_of_l, key=len)
        """returning the result"""
        result = []
        j = 10
        while j > 0:
            result.append(sorted_list[-j])
            j -= 1
        return result


def get_rarest_char(file_path: str) -> str:
    """function that finds the rarest symbol for document using dictionary"""
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


def count_punctuation_chars(file_path: str) -> int:
    """function that counts every punctuation char by the discarding all other kinds of characters"""
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


def count_non_ascii_chars(file_path: str) -> int:
    """function that counts every non ascii char"""
    with open(file_path) as file:
        text = file.read().encode().decode('unicode-escape')
        text = text.replace('\n', '')
        total_count = len(text)
        ascii_count = len(text.encode("ascii", "ignore"))
        return total_count - ascii_count


def get_most_common_non_ascii_char(file_path: str) -> str:
    """function that finds most common non ascii char for document"""
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
