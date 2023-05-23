import pytest
from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    counter = 0
    for file in dir_path.glob(f'*.{file_extension}'):
        with file.open('r') as f:
            if tokenizer is None:
                counter += len(f.readlines())
            else:
                counter += len(tokenizer(' '.join(f.readlines())))
    return counter


def test_universal_file_counter(tmp_path):
    # Create test files
    file1 = tmp_path / "test_file1.txt"
    file2 = tmp_path / "test_file2.txt"
    file1.write_text("Hello, world!nHow are you?")
    file2.write_text("This is a test.nIt should work.")

    # Test the function with no tokenizer
    assert universal_file_counter(tmp_path, "txt") == 4

    # Test the function with a tokenizer
    assert universal_file_counter(tmp_path, "txt", str.split) == 8

    # Clean up test files
    file1.unlink()
    file2.unlink()