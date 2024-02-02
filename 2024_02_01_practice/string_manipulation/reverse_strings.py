"""String manipulations.

We're using `list[]` without `from typing import List` since
Python3.9 introduced type hints without imports.
"""

from collections import deque


def reverse_words(sentence: str) -> list[str]:
    """Simplest way."""
    # For each word
    # push onto array
    words: list[str] = sentence.split(" ")

    result: list[str] = []
    idx: int = len(words) - 1
    while idx >= 0:
        result.append(words[idx])
        idx -= 1

    print(result)
    return result


def reverse_words_deque(sentence: str) -> list[str]:
    """Use deque library."""
    stack: deque = deque(sentence)
    print(stack)
    return [""]
