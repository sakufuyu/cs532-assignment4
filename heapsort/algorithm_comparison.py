import time
import random
from heapsort import heapsort
from randomized_quicksort import randomized_quicksort


def generate_random_array(n):
    """Generate a random array of size n with values between 0 and 10000"""
    return [random.randint(0, 10000) for _ in range(n)]


def generate_sorted_array(n):
    """Generate a sorted array of size n"""
    return list(range(n))


def generate_reverse_sorted_array(n):
    """Generate a reverse sorted array of size n"""
    return list(range(n, 0, -1))


def run_algorithm(algorithm, arr, *args):
    """Run the sorting algorithm and measure execution time"""
    # Create a copy to avoid modifying the original array
    arr_copy = arr.copy()

    start_time = time.time()
    if algorithm == randomized_quicksort:
        high = args[0] if args else None
        algorithm(arr_copy, 0, high)
    else:
        algorithm(arr_copy)
    end_time = time.time()

    return end_time - start_time


def compare_sorting_algorithms():
    """
    Compare heapsort with quicksort performance
    on different input sizes and distributions
    """
    # Define input sizes to test
    input_sizes = [100, 500, 1000, 5000, 10000]

    # Define data distributions to test
    distributions = {
        'Random': generate_random_array,
        'Sorted': generate_sorted_array,
        'Reverse Sorted': generate_reverse_sorted_array
    }

    # Store results
    heapsort_times = {dist: [] for dist in distributions}
    quicksort_times = {dist: [] for dist in distributions}

    # Run the comparison
    for size in input_sizes:
        print(f"Testing with array size: {size}")

        for dist_name, dist_func in distributions.items():
            # Generate array according to distribution
            arr = dist_func(size)

            # Test heapsort
            heap_time = run_algorithm(heapsort, arr)
            heapsort_times[dist_name].append(heap_time)
            print(f"  Heapsort on {dist_name} distribution: {heap_time:.6f} seconds")

            # Test quicksort (with high parameter set to n-1)
            quick_time = run_algorithm(randomized_quicksort, arr, len(arr) - 1)
            quicksort_times[dist_name].append(quick_time)
            print(f"  Quicksort on {dist_name} distribution: {quick_time:.6f} seconds")

    # Print a summary table
    print("\nSummary Table (Execution times in seconds):")
    print("=" * 80)
    print(f"{'Array Size':<15}", end="")
    for dist_name in distributions:
        print(f"{dist_name + ' Heap':<15}{dist_name + ' Quick':<15}", end="")
    print()
    print("-" * 80)

    for i, size in enumerate(input_sizes):
        print(f"{size:<15}", end="")
        for dist_name in distributions:
            print(f"{heapsort_times[dist_name][i]:<15.6f}{quicksort_times[dist_name][i]:<15.6f}", end="")
        print()


if __name__ == "__main__":

    # Run the comparison
    compare_sorting_algorithms()

    # Additional verification test with a small array
    test_array = [generate_random_array(10)]
    print("\nVerification test:")
    print("Original array:", test_array)

    heap_sorted = heapsort(test_array.copy())
    print("Heapsort result:", heap_sorted)

    quick_array = test_array.copy()
    randomized_quicksort(quick_array, 0, len(quick_array) - 1)
    print("Quicksort result:", quick_array)
