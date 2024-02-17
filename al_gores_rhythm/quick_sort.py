"""Quick sort.

Select a pivot element then perform swaps to get the lesser values before the 
pivot and greater values after.  

Time complexity: O(n log n) on average; O(n^2) worst case; 
Since the partition is not guaranteed to be the median, the 
algorithm potentially could take n^2.  
"""

import logging
from typing import Any


logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    logging.info("Quick sort")


def quicksort():
    pass


def _recursive_quicksort():
    pass


if __name__ == "__main__":
    main()
