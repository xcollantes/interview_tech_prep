"""You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""


def main():
    print(type(subarray_avg([1, 12, -5, -6, 50, 3], 4)))
    print(subarray_avg([1, -1, -1, -1, -1], 2))
    assert subarray_avg([1, 12, -5, -6, 50, 3], 4) == 12.75000
    assert subarray_avg([5], 1) == 5.00000
    assert subarray_avg([0], 1) == 0.00000
    assert subarray_avg([5], 1) == 5.00000


def subarray_avg(nums: list[int], k: int) -> float:
    if len(nums) <= k:
        return average(nums)

    averages: list[float] = []
    left: int = 0
    right: int = left + (k - 1)

    while right < len(nums):
        average_window: float = average(nums[left: right + 1])

        print(nums[left: right + 1])
        print("average: ", average_window)
        averages.append(average_window)

        left += 1
        right += 1

    return max(averages)


def average(nums: list[int]) -> float:
    average: float = 0.00000
    for num in nums:
        average += num
    return average / len(nums)


if __name__ == "__main__":
    main()
