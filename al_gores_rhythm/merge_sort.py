"""Merge sort.

Divide and conquer technique with time complexity of O(n log n). 
The array is broken down to its most atomic parts then put back 
together but the parts are compared when reorganized. 

The mid element is chosen using `mid: int = len(input) // 2` where the 
`//` will return the floor divide of the operands. This is true for Python3.  

Time complexity: O(n log n).  Breaks down the list of elements and makes 
comparisons for each atomic value. 
"""

import logging
from typing import List

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    input: List[int] = [3, 5, 0, 56, 12, 4, 1]
    input_second: List[int] = [15, 2, 4, 9, 23, 0, 3]
    input_third: List[int] = []

    logging.info("SOLUTION: %s", sorted(input))
    logging.info("RESULT: %s", merge_sort(input))
    assert merge_sort(input_second) == sorted(input_second)
    assert merge_sort(input_third) == sorted(input_third)


def merge_sort(input: List[int]) -> List[int]:
    """Sort list using Merge Sort algorithm.

    The array is sorted in place.

    Args:
        input: Array input.

    Returns:
        Sorted array in place. 
    """
    if len(input) > 1:

        mid: int = len(input) // 2

        logging.debug("%s | %s", input[:mid], input[mid:])

        L: List[int] = merge_sort(input[:mid])
        R: List[int] = merge_sort(input[mid:])

        logging.debug("put back together")

        leftIdx: int = 0
        rightIdx: int = 0
        currIdx: int = 0

        while leftIdx < len(L) and rightIdx < len(R):
            if L[leftIdx] < R[rightIdx]:
                input[currIdx] = L[leftIdx]
                leftIdx += 1
            else:
                input[currIdx] = R[rightIdx]
                rightIdx += 1

            currIdx += 1

        while leftIdx < len(L):
            input[currIdx] = L[leftIdx]
            leftIdx += 1
            currIdx += 1

        while rightIdx < len(R):
            input[currIdx] = R[rightIdx]
            rightIdx += 1
            currIdx += 1

    return input


if __name__ == "__main__":
    main()
