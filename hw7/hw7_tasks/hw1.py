"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str], ...]) -> Iterator:
    a = []
    for i in file_list:
        with open(i) as file:
            for line in file:
                a.append(int(line[:len(line) - 1]))
    return iter(sorted(a))


list(merge_sorted_files(["file1.txt", "file2.txt"]))
