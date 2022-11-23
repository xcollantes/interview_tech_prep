"""Sort squares.

Since the array A is sorted, loosely speaking it has some negative elements 
with squares in decreasing order, then some non-negative elements with squares 
in increasing order.

For example, with [-3, -2, -1, 4, 5, 6], we have the negative part 
[-3, -2, -1] with squares [9, 4, 1], and the positive part [4, 5, 6] 
with squares [16, 25, 36]. Our strategy is to iterate over the negative part 
in reverse, and the positive part in the forward direction.
"""

from typing import List


def main():
    print(sortedSquares([-4, -1, 0, 3, 10]))
    # assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


def sortedSquares(nums: List[int]) -> List[int]:
    """Sort given squares.  Input is already sorted."""
    result: List[int] = [0] * len(nums)
    left: int = 0
    right: int = len(nums) - 1

    for resultIdx in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            to_square = nums[left]
            left += 1
        else:
            to_square = nums[right]
            right -= 1

        square: int = to_square ** 2
        print(square)
        result[resultIdx] = square

    return result


if __name__ == "__main__":
    main()
