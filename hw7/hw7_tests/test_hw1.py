from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str], ...]) -> Iterator:
    a = []
    for i in file_list:
        with open(i) as file:
            for line in file:
                a.append(int(line[:len(line) - 1]))
    return iter(sorted(a))


def test_merge_sorted_files(tmp_path):
    # Create temporary files with sorted numbers
    file1 = tmp_path / "file1.txt"
    file1.write_text("1n2n3n")
    file2 = tmp_path / "file2.txt"
    file2.write_text("4n5n6n")

    # Test the function
    result = list(merge_sorted_files([file1, file2]))
    assert result == [1, 2, 3, 4, 5, 6]
