import random


def randomized_quicksort(arr, low=0, high=None):
    """
    Randomized Quicksort implementation.
    Args:
        arr: Array to be sorted
        low: Start index
        high: End index
    """

    if (high is None):
        high = len(arr) - 1

    if (low < high):
        # Choose a random pivot index
        pivot_index = random.randint(low, high)

        # Swap the pivot with the last element
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        # Partition the array
        pivot_pos = partition(arr, low, high)

        # Recursively sort the left and right subarrays
        randomized_quicksort(arr, low, pivot_pos - 1)
        randomized_quicksort(arr, pivot_pos + 1, high)

    return arr


def partition(arr, low, high):
    """
    Partition function for quicksort.
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if (arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
