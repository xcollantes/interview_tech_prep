"""Use Bubble sort.

The shittiest of the sorting algorithms with 
time complexity of O(n^2). 

At the worst scenario, you have to make the switch 
on each element in the array/list. Then that move will be made
for each array/list element. n for each element then that can 
happen n times so n * n or n^2.  

Example: https://stackabuse.com/bubble-sort-in-python/ 
"""

from typing import List


def main():
    input: List[int] = [3, 5, 1, 56, 12, 0, 1]
    input_second: List[int] = [15, 2, 4, 9, 23, 0, 3]
    input_third: List[int] = []

    print("SOLUTIUON: ", sorted(input))
    print("RESULT: ", basic_bubble_sort(input))

    # sort() will sort in place and sorted() will not alter original
    assert basic_bubble_sort(input) == sorted(input)
    assert basic_bubble_sort(input_second) == sorted(input_second)
    assert basic_bubble_sort(input_third) == sorted(input_third)

    print("OPTIMIZTED RESULT: ", optimized_bubble_sort(input))

    assert optimized_bubble_sort(input) == sorted(input)
    assert optimized_bubble_sort(input_second) == sorted(input_second)
    assert optimized_bubble_sort(input_third) == sorted(input_third)


def basic_bubble_sort(input: List[int]) -> List[int]:
    """Sort list using Bubble Sort algorithm.

    Args:
        input: Array input.

    Returns:
        Sorted array.
    """
    if len(input) < 1:
        return input

    idx: int = 0
    # Best case, you only need to iterate through the
    # array once to check if the array is in order
    for _ in range(len(input)):
        while idx < len(input) - 1:
            if input[idx] > input[idx + 1]:
                # Perform swap
                input[idx], input[idx + 1] = input[idx + 1], input[idx]
                # This is Python specific syntax but to generalize using
                # temp variable:
                # ```
                # temp: int = None  # Outside of loops
                # ...
                # temp = input[idx]
                # input[idx] = input[idx + 1]
                # input[idx + 1] = temp
                # ```
            idx += 1
        idx = 0  # Reset to the first index
    return input


def optimized_bubble_sort(input: List[int]) -> List[int]:
    """Improved performance on Bubble Sort algorithm.

    Improvements: 
    1)  NO-SWAP 
        When no swap is made, that means list is already sorted. 
        Algorithm is the same but will stop once the list is 
        sorted. 

    2)  IGNORE-ALREADY-SORTED
        We know Bubble Sort ends each pass with the largest number at
        the end of the list. The first pass gurantees that the last
        element or n is the largest element, then in the second pass
        the second to last element is the second-largest or n - 1, and 
        so forth. 

        This means for each pass, we can ignore one less element on the 
        end of the list. More precisely, the k-th iteration, we only need 
        to look at n - k + 1 number of elements. 
    """
    if len(input) < 1:
        return input

    swapped: bool = True  # NO-SWAP
    num_of_iterations: int = 0  # IGNORE-ALREADY-SORTED
    idx: int = 0

    while swapped:  # NO-SWAP: Instead check for if a swap occured
        swapped = False  # NO-SWAP

        # IGNORE-ALREADY-SORTED: Reduce the number elements to iterate
        # for each pass since we know the largest values "Bubble up" to
        # the end.
        while idx < len(input) - num_of_iterations - 1:

            # NO-SWAP: If this never occurs on a single pass, then you
            # can safely say the list is sorted without continuing
            # to the already sorted parts of the list.
            if input[idx] > input[idx + 1]:
                input[idx], input[idx + 1] = input[idx + 1], input[idx]

                swapped = True  # NO-SWAP

            idx += 1
        idx = 0
        num_of_iterations += 1  # IGNORE-ALREADY-SORTED: Add one for each pass

    return input


if __name__ == "__main__":
    main()
