"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
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


print(universal_file_counter(Path('src/'), "txt", str.split))
