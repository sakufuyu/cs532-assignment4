import random


def heapify(arr, n, i):
    """
    Convert the subtree rooted at the i-th element of array arr into a max heap

    Args:
        arr: Array to convert into a heap
        n: Number of elements in the array (range to convert)
        i: Index of the element to use as the root
    """

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and larger than parent
    if (left < n and arr[left] > arr[largest]):
        largest = left

    # Check if right child exists and larger than parent
    if (right < n and arr[right] > arr[largest]):
        largest = right

    # Place the largest value of the triangle at the root position
    if (largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,  n, largest)


def heapsort(arr):
    """
    Sort array in ascending order using heap sort algorithm

    Args:
        arr: List of comparable elements to sort

    Returns:
        Sorted array in ascending order
    """

    n = len(arr)

    # Build a max heap: Starting from the back, we build a heap of subtrees rooted at each element.
    # Since the number of elements increases by 2^n at each level,
    # the root index of the bottom triangle is at most n/2.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    # Move current root (maximum) to end and reduce heap size
    for i in range(n - 1, 0, -1):
        # Swap root with last element
        arr[i], arr[0] = arr[0], arr[i]
        # Restore heap property for reduced heap
        heapify(arr, i, 0)
    return arr


if __name__ == "__main__":
    for _ in range(5):
        arr = [random.randint(0, 500) for _ in range(1000)]
        assert heapsort(arr.copy()) == sorted(arr.copy())
    print("\nSorting algorithm works property.\n")
