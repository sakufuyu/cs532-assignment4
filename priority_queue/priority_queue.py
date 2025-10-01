

class Task:
    """
    Class to represent a task in th priority queue
    """

    def __init__(self, task_id, priority, arrival_time=0, deadline=None):
        """
        Initialize Task object
        task_id: unique identifier for the task
        priority: task's priority value
        arrival_time: time when the task was added to the queue
        deadline: optional deadline for the task
        """

        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __str__(self):
        """String representation of the task"""
        return f"Task ID: {self.task_id}, Priority: {self.priority}"


class MinHeapPriorityQueue:
    """
    Priority queue implementation using min-heap
    Tasks with lowest priority value are extracted first
    """

    def __init__(self):
        """
        Initialize an empty priority queue
        Use a list to store the heap
        """

        self.heap = list()
        self.task_position = {}  # Dictionary to store task positions in the heap

    def is_empty(self):
        """
        Check if the priority queue is empty
        Time complexisy: O(1)
        """

        return len(self.heap) == 0

    def parent(self, i):
        """
        Get the parent index of node at index i
        """

        return (i - 1) // 2

    def left_child(self, i):
        """
        Get the left child index of node at index i
        """

        return 2 * i + 1

    def right_child(self, i):
        """
        Get the right child index of node at index i
        """

        return 2 * i + 2

    def swap(self, i, j):
        """
        Swap two nodes in the heap
        Also update task positions
        """

        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.task_position[self.heap[i].task_id] = i
        self.task_position[self.heap[j].task_id] = j

    def sift_up(self, i):
        """
        Sift up the node at index i to maintain heap property
        """

        while (i > 0 and self.heap[i].priority < self.heap[self.parent(i)].priority):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def sift_down(self, i):
        """
        Sift down the node at index i to maintain heap property
        """

        min_index = i
        left = self.left_child(i)
        if (left < len(self.heap) and self.heap[left].priority < self.heap[min_index].priority):
            min_index = left

        right = self.right_child(i)
        if (right < len(self.heap) and self.heap[right].priority < self.heap[min_index].priority):
            min_index = right

        if (i != min_index):
            self.swap(i, min_index)
            self.sift_down(min_index)

    def insert(self, task):
        """
        Insert a new task into the priority queue
        Time complexity: O(log n) where n is the number of tasks
        """
        self.heap.append(task)
        index = len(self.heap) - 1
        self.task_position[task.task_id] = index
        self.sift_up(index)

    def extract_min(self):
        """
        Remove and return the task with the lowest priority
        Time complexity: O(log n) where n is the number of tasks
        """
        if (self.is_empty()):
            return None

        min_task = self.heap[0]
        last_task = self.heap.pop()

        if (self.heap):  # If heap is not empty after popping
            self.heap[0] = last_task
            self.task_position[last_task.task_id] = 0
            self.sift_down(0)

        del self.task_position[min_task.task_id]
        return min_task

    def decrease_key(self, task_id, new_priority):
        """
        Decrease the priority of a task
        For min-heap, decrease means the priority value becomes smaller
        Time complexity: O(log n) where n is the number of tasks
        """
        if (task_id not in self.task_position):
            return False

        index = self.task_position[task_id]
        if (new_priority >= self.heap[index].priority):
            return False  # New priority is not smaller

        self.heap[index].priority = new_priority
        self.sift_up(index)
        return True

    def increase_key(self, task_id, new_priority):
        """
        Increase the priority of a task
        For min-heap, increase means the priority value becomes larger
        Time complexity: O(log n) where n is the number of tasks
        """
        if (task_id not in self.task_position):
            return False

        index = self.task_position[task_id]
        if (new_priority <= self.heap[index].priority):
            return False  # New priority is not larger

        self.heap[index].priority = new_priority
        self.sift_down(index)
        return True


class MaxHeapPriorityQueue:
    """
    Priority queue implementation using max-heap
    Tasks with highest priority value are extracted first
    """
    def __init__(self):
        """
        Initialize an empty priority queue
        We use a list to store the heap
        """
        self.heap = []
        self.task_position = {}  # Maps task_id to its position in the heap

    def is_empty(self):
        """
        Check if the priority queue is empty
        Time complexity: O(1)
        """
        return len(self.heap) == 0

    def parent(self, i):
        """Get the parent index of node at index i"""
        return (i - 1) // 2

    def left_child(self, i):
        """Get left child index of node at index i"""
        return 2 * i + 1

    def right_child(self, i):
        """Get right child index of node at index i"""
        return 2 * i + 2

    def swap(self, i, j):
        """Swap two elements in the heap and update their positions"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.task_position[self.heap[i].task_id] = i
        self.task_position[self.heap[j].task_id] = j

    def sift_up(self, i):
        """Move a node up the heap to maintain the heap property"""
        while i > 0 and self.heap[i].priority > self.heap[self.parent(i)].priority:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def sift_down(self, i):
        """Move a node down the heap to maintain the heap property"""
        max_index = i
        left = self.left_child(i)

        if (left < len(self.heap) and self.heap[left].priority > self.heap[max_index].priority):
            max_index = left

        right = self.right_child(i)
        if (right < len(self.heap) and self.heap[right].priority > self.heap[max_index].priority):
            max_index = right

        if (i != max_index):
            self.swap(i, max_index)
            self.sift_down(max_index)

    def insert(self, task):
        """
        Insert a new task into the priority queue
        Time complexity: O(log n) where n is the number of tasks
        """
        self.heap.append(task)
        index = len(self.heap) - 1
        self.task_position[task.task_id] = index
        self.sift_up(index)

    def extract_max(self):
        """
        Remove and return the task with the highest priority
        Time complexity: O(log n) where n is the number of tasks
        """
        if (self.is_empty()):
            return None

        max_task = self.heap[0]
        last_task = self.heap.pop()

        if (self.heap):  # If heap is not empty after popping
            self.heap[0] = last_task
            self.task_position[last_task.task_id] = 0
            self.sift_down(0)

        del self.task_position[max_task.task_id]
        return max_task

    def increase_key(self, task_id, new_priority):
        """
        Increase the priority of a task
        For max-heap, increase means the priority value becomes larger
        Time complexity: O(log n) where n is the number of tasks
        """
        if (task_id not in self.task_position):
            return False

        index = self.task_position[task_id]
        if (new_priority <= self.heap[index].priority):
            return False  # New priority is not larger

        self.heap[index].priority = new_priority
        self.sift_up(index)
        return True

    def decrease_key(self, task_id, new_priority):
        """
        Decrease the priority of a task
        For max-heap, decrease means the priority value becomes smaller
        Time complexity: O(log n) where n is the number of tasks
        """
        if (task_id not in self.task_position):
            return False

        index = self.task_position[task_id]
        if (new_priority >= self.heap[index].priority):
            return False  # New priority is not smaller

        self.heap[index].priority = new_priority
        self.sift_down(index)
        return True


if __name__ == "__main__":
    # Test min-heap priority queue
    print("Testing Min-Heap Priority Queue:")
    min_pq = MinHeapPriorityQueue()

    # Insert tasks
    tasks = [
        Task(1, 5, 0),
        Task(2, 3, 0),
        Task(3, 7, 0),
        Task(4, 1, 0),
        Task(5, 9, 0),
    ]

    for task in tasks:
        min_pq.insert(task)
        print(f"Inserted: {task}")

    # Extract tasks in priority order
    print("\nExtracting tasks in priority order:")
    while not min_pq.is_empty():
        task = min_pq.extract_min()
        print(f"Extracted: {task}")

    # Test max-heap priority queue
    print("\nTesting Max-Heap Priority Queue:")
    max_pq = MaxHeapPriorityQueue()

    # Insert tasks
    for task in tasks:
        max_pq.insert(task)
        print(f"Inserted: {task}")

    # Change priority of a task
    max_pq.increase_key(3, 10)
    print("\nIncreased priority of Task 3 to 10")

    # Extract tasks in priority order
    print("\nExtracting tasks in priority order:")
    while not max_pq.is_empty():
        task = max_pq.extract_max()
        print(f"Extracted: {task}")
