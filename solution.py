"""
Project 4 - Hybrid Sorting - Solution Code
CSE 331 Fall 2022
"""

import gc
import random
import time
from typing import TypeVar, List, Callable, Dict

T = TypeVar("T")  # represents generic type


# do_comparison is an optional helper function but HIGHLY recommended!!!
def do_comparison(first: T, second: T, key: Callable[[T], T], descending: bool) -> bool:
    """
    Compares two elements based on given lambda function

    :param first: the first element to be compared
    :param second: the second element to be compared
    :param key: the function determining how element's will be compared
    :param descending: a boolean determining if the element will be sorted in ascending or descending order
    :return: a boolean dependent on param descending and first and second vals
    """
    if descending == False:
        if key(first) > key(second):
            return True
        else:
            return False
    else:
        if key(first) < key(second):
            return True
        else:
            return False


def selection_sort(data: List[T], *, key: Callable[[T], T] = lambda x: x,
                   descending: bool = False) -> None:
    """
    A selection based sorting algorithm that will sort a list of objects dependent on the passed lambda function

    :param data: the list to be sorted
    :param key: the lambda function to determine how the list is sorted
    :param descending: a boolean determining whether to sort the list in ascending or descending order
    :return: None
    """
    size = len(data)
    for i in range(0, size):
        small = i
        for j in range(i, size):
            if do_comparison(data[small], data[j], key, descending):  # calls comparison function
                small = j
            j += 1

        # swap elements
        temp = data[i]
        data[i] = data[small]
        data[small] = temp


def bubble_sort(data: List[T], *, key: Callable[[T], T] = lambda x: x,
                descending: bool = False) -> None:
    """
    Sorts a list using a bubble sort algorithm

    :param data: the list to be sorted
    :param key: a function determining how the list will be sorted
    :param descending: a boolean determining whether the list is sorted in ascending or descending order
    :return: None
    """
    size = len(data) - 1
    swapped = False
    for i in range(size):
        for j in range(0, size - i):
            if do_comparison(data[j], data[j + 1], key, descending):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            return


def insertion_sort(data: List[T], *, key: Callable[[T], T] = lambda x: x,
                   descending: bool = False) -> None:
    """
    Sorts a list using an insertion sort algorithm

    :param data: the list to be sorted
    :param key: a function determining how the list will be sorted
    :param descending: a boolean determining whether the list is sorted in ascending or descending order
    :return: None
    """
    size = len(data)
    for i in range(1, size):
        j = i
        while (j > 0 and do_comparison(data[j - 1], data[j], key, descending)):
            temp = data[j]
            data[j] = data[j - 1]
            data[j - 1] = temp
            j = j - 1


def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      key: Callable[[T], T] = lambda x: x, descending: bool = False) -> None:
    """
    Sorts a list using a recursive merge sort algorithm that will use insertion sort once the sub-lists are smaller
    than the threshold.

    :param data: the list to be sorted
    :param threshold: the length of the list that the algorithm will switch to insertion sort
    :param key: a function determining how the list will be sorted
    :param descending: a boolean determining whether the list is sorted in ascending or descending order
    :return: None
    """

    def merge(S1, S2, S):

        if not descending:
            i = j = 0
            while i + j < len(S):
                if j == len(S2) or (i < len(S1) and key(S1[i]) < key(S2[j])):
                    S[i + j] = S1[i]
                    i = i + 1
                else:
                    S[i + j] = S2[j]
                    j = j + 1

        else:
            i = 0
            j = 0
            count = 0
            while i < len(S1) or j < len(S2):
                if j == len(S2) or (i < len(S1) and key(S1[i]) > key(S2[j])):
                    S[count] = S1[i]
                    i = i + 1
                    count += 1
                else:
                    S[count] = S2[j]
                    j = j + 1
                    count += 1

    size = len(data)
    mid = size // 2
    left = data[0:mid]
    right = data[mid:size]

    if size >= threshold:
        hybrid_merge_sort(left, key=key, descending=descending)
        hybrid_merge_sort(right, key=key, descending=descending)
        merge(right, left, data)

    else:
        insertion_sort(left, key=key, descending=descending)
        insertion_sort(right, key=key, descending=descending)
        merge(right, left, data)


def quicksort(data):
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first, last):
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)


def sort_sushi(sushi: List[str], key: Callable[[T], T] = lambda x: {'D': 0, 'A': 1, 'C': 2}[x]) -> None:
    """
    Sort a list of sushi based on the given key. Sorts by using a variable holding the index of the last sorted value
    and will swap the next value after the variable with the desired value. This creates a partition separating the
    sorted values and the non-sorted values. Once the desired values are at the front of the list the loop will end
    and a second one will begin, this time checking for the values that should be in the middle of the list. The
    partition value is retained and the process begins again.

    :param sushi: the list to be sorted
    :param key: a function that determines the order in which the list will be sorted
    :return: None
    """
    dorder = key('D')
    aorder = key('A')
    corder = key('C')
    i = 0

    # determine the order in which the list will be sorted by
    if dorder == 0:
        first = 'D'
    elif dorder == 2:
        last = 'D'
    elif dorder == 1:
        middle = 'D'
    if aorder == 0:
        first = 'A'
    elif aorder == 2:
        last = 'A'
    elif aorder == 1:
        middle = 'A'
    if corder == 0:
        first = 'C'
    elif corder == 2:
        last = 'C'
    elif corder == 1:
        middle = 'C'

    ptr = -1
    i = 0
    while i <= len(sushi) - 1:  # sorts desired values and swaps them to be at the beginning of the list
        if sushi[i] == first:
            sushi[ptr + 1], sushi[i] = sushi[i], sushi[ptr + 1]
            ptr += 1
        i += 1

    i = 0
    while i <= len(sushi) - 1:  # sorts desired values and swaps them to the middle of the list
        if sushi[i] == middle:
            sushi[ptr + 1], sushi[i] = sushi[i], sushi[ptr + 1]
            ptr += 1
        i += 1
