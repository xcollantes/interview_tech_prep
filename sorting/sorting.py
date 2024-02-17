"""Collection of sorting algorithms."""

import copy
from typing import Any, List


def main():
    numList: List[int] = [2, 23, 55, 50, 50, 1, 0, 100, 788, 420, 70]
    print(sorted(numList))

    print("Bubble sort")
    print(bubble(copy.deepcopy(numList)))

    print("Merge Sort")
    print(merge(copy.deepcopy(numList)))


def bubble(u: List[int]) -> List[int]:
    l = len(u)
    for x in range(l):
        print("x:     ", u)
        for y in range(0, l - x - 1):
            print("    y: ", u)
            if u[y] > u[y + 1]:
                u[y + 1], u[y] = u[y], u[y + 1]
    return u


def merge(u: List[int]) -> List[int]:
    print("u: ", u)
    if len(u) > 1:
        mid: int = len(u) // 2
        L = merge(u[:mid])
        R = merge(u[mid:])
        Lpos = Rpos = pos = 0

        while Lpos < len(L) and Rpos < len(R):
            if L[Lpos] > R[Rpos]:
                u[pos] = R[Rpos]
                Rpos += 1
            else:
                u[pos] = L[Lpos]
                Lpos += 1
            pos += 1

        while Lpos < len(L):
            u[pos] = L[Lpos]
            Lpos += 1
            pos += 1

        while Rpos < len(R):
            u[pos] = R[Rpos]
            Rpos += 1
            pos += 1

    return u


if __name__ == "__main__":
    main()
