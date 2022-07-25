"""Insertion sort.

Simple yet inefficient sorting algorithm.  Iterate through each element 
and if the next element is smaller than the current element, switch with 
the current element then pass element behind the current element.  
Check with each element behind current element to see where the passed element
belongs. 

Process: 
    1. Place first element in sorted list.
    2. If next element is larger, then pass behind current element. 
       If next element is smaller, then switch places.  
    3. 
"""

import logging
from typing import Any

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    logging.info("Insertion sort")

    input1: list(int) = [25, 20, 15, 1, 5, 8, 18, 12]
    input2: list(int) = [24, 11, 0, 34, 89, 11, 12, 88, 88, 88]
    input3: list(int) = []

    logging.info("Sorted: %s", sorted(input1))
    logging.info("Solution: %s", insertion_sort(input1))

    assert insertion_sort(input1) == sorted(input1)
    assert insertion_sort(input2) == sorted(input2)
    assert insertion_sort(input3) == sorted(input3)


def insertion_sort(input: list) -> list:
    """Use insertion sort.

    Args:
        input (list): List to sort. 

    Returns:
        List of sorted values.
    """
    for a_idx in range(1, len(input)):
        logging.info("Array: %s", input)

        # Start at second element since we'll include first element as part of
        # sorted array.
        key: list = input[a_idx]
        logging.debug("Key: %s", key)

        sub_idx: int = a_idx - 1  # Pointer for "sub array" of sorted elements

        # Place key in correct place in the already sorted "sub array"
        while key < input[sub_idx] and sub_idx >= 0:
            input[sub_idx + 1] = input[sub_idx]  # Shift the "sub array" by one
            sub_idx -= 1  # Move down the "sub array"

        input[sub_idx + 1] = key

    return input


if __name__ == "__main__":
    main()
