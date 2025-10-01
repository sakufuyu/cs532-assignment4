# CS532 Assignment 4: Heap Data Structures

This repository contains implementations of heap-based algorithms including heapsort and priority queues.


## Heapsort (`heapsort/heapsort.py`)

**Features:**
- Implements an in-place sorting algorithm using max-heap
- Time complexity: O(n log n) for all cases
- Space complexity: O(1) auxiliary space
- Key functions:
  - `heapify()`: Maintains heap property for subtree
  - `heapsort()`: Main sorting function that builds heap and extracts elements
- Successfully passes validation with random arrays of 1000 elements

**Execution:**
```bash
cd heapsort
python heapsort.py
```


## Priority Queue (`priority_queue/priority_queue.py`)

**Features:**
- Implements both min-heap and max-heap priority queues
- Supports task scheduling with priority-based extraction
- Key features:
  - Task insertion: O(log n)
  - Priority extraction: O(log n)
  - Priority modification: O(log n)
  - Position tracking for efficient key updates
- Classes:
  - `Task`: Represents individual tasks with ID, priority, and metadata
  - `MinHeapPriorityQueue`: Extracts lowest priority tasks first
  - `MaxHeapPriorityQueue`: Extracts highest priority tasks first

**Execution:**
```bash
cd priority_queue
python priority_queue.py
```


## Research Overview

### [Algorithm Comparison between Heapsort and Randomized Quicksort]
- Compares heapsort vs randomized quicksort performance across different input sizes (100-10,000 elements)
- Tests three data distributions: random, sorted, and reverse sorted arrays
- Measures execution time for each algorithm-distribution combination
- Provides performance analysis table showing time complexity behavior in practice

### [Priority Queue Testing]
- Tests basic operations: insertion, extraction, and empty state checking
- Validates priority modification operations (decrease_key for min-heap, increase_key for max-heap)
- Performance benchmarking across queue sizes (1,000-100,000 elements)
- Measures average time per operation for insert, extract, and priority change operations