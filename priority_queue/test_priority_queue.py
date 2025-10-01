from priority_queue import Task, MinHeapPriorityQueue, MaxHeapPriorityQueue
import time
import random


def test_basic_operations():
    """Test basic operations of priority queues"""
    print("=== Testing Priority Queue Operations ===")

    # Test MinHeapPriorityQueue
    print("\n-- Testing MinHeapPriorityQueue --")
    min_pq = MinHeapPriorityQueue()

    # Test is_empty
    print("Is empty initially:", min_pq.is_empty())

    # Test insertion
    tasks = [
        Task(1, 7, 0),
        Task(2, 4, 0),
        Task(3, 9, 0),
        Task(4, 3, 0),
        Task(5, 10, 0),
    ]

    for task in tasks:
        min_pq.insert(task)
        print(f"Inserted: {task}")

    print("Is empty after insertions:", min_pq.is_empty())

    # Test extraction
    print("\nExtracting tasks from min-heap:")
    while not min_pq.is_empty():
        task = min_pq.extract_min()
        print(f"Extracted: {task}")

    # Test MaxHeapPriorityQueue
    print("\n-- Testing MaxHeapPriorityQueue --")
    max_pq = MaxHeapPriorityQueue()

    # Test insertion
    for task in tasks:
        max_pq.insert(task)
        print(f"Inserted: {task}")

    # Test extraction
    print("\nExtracting tasks from max-heap:")
    while not max_pq.is_empty():
        task = max_pq.extract_max()
        print(f"Extracted: {task}")


def test_priority_changes():
    """Test key modification operations"""
    print("\n=== Testing Priority Modification ===")

    # Test on MinHeapPriorityQueue
    print("\n-- Testing on MinHeapPriorityQueue --")
    min_pq = MinHeapPriorityQueue()

    tasks = [
        Task(1, 7, 0),
        Task(2, 4, 0),
        Task(3, 9, 0),
        Task(4, 3, 0),
        Task(5, 10, 0),
    ]

    for task in tasks:
        min_pq.insert(task)

    # Test decrease_key
    print(f"Decreasing priority of {min_pq.heap[min_pq.task_position[3]]} to 2")
    min_pq.decrease_key(3, 2)

    print("Extracting tasks after priority change:")
    while not min_pq.is_empty():
        task = min_pq.extract_min()
        print(f"Extracted: {task}")

    # Test on MaxHeapPriorityQueue
    print("\n-- Testing on MaxHeapPriorityQueue --")
    max_pq = MaxHeapPriorityQueue()

    for task in tasks:
        max_pq.insert(task)

    # Test increase_key
    print(f"Increasing priority of {max_pq.heap[max_pq.task_position[2]]} to 8")
    max_pq.increase_key(2, 8)

    print("Extracting tasks after priority change:")
    while not max_pq.is_empty():
        task = max_pq.extract_max()
        print(f"Extracted: {task}")


def test_performance():
    """Test average time per operation for different queue sizes"""
    print("\n=== Performance Testing ===")

    sizes = [1000, 10000, 100000]

    for size in sizes:
        print(f"\n-- Queue Size: {size} --")

        tasks = [Task(i, random.randint(1, 1000), 0) for i in range(size)]

        # MinHeap
        min_pq = MinHeapPriorityQueue()

        start = time.time()
        for task in tasks:
            min_pq.insert(task)
        avg_insert = (time.time() - start) / size * 1000

        start = time.time()
        for i in range(100):
            min_pq.decrease_key(i, 1)
        avg_decrease = (time.time() - start) / 100 * 1000

        start = time.time()
        for _ in range(size):
            min_pq.extract_min()
        avg_extract = (time.time() - start) / size * 1000

        print(f"MinHeap - Insert: {avg_insert:.4f}ms/op, Decrease: {avg_decrease:.4f}ms/op, Extract: {avg_extract:.4f}ms/op")

        # MaxHeap
        max_pq = MaxHeapPriorityQueue()

        start = time.time()
        for task in tasks:
            max_pq.insert(task)
        avg_insert = (time.time() - start) / size * 1000

        start = time.time()
        for i in range(100):
            max_pq.increase_key(i, 1000)
        avg_increase = (time.time() - start) / 100 * 1000

        start = time.time()
        for _ in range(size):
            max_pq.extract_max()
        avg_extract = (time.time() - start) / size * 1000

        print(f"MaxHeap - Insert: {avg_insert:.4f}ms/op, Increase: {avg_increase:.4f}ms/op, Extract: {avg_extract:.4f}ms/op")


if __name__ == "__main__":
    test_basic_operations()
    test_priority_changes()
    test_performance()
