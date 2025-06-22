class Heap:
    '''
    Class to implement a heap with general comparison function.
    '''

    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        self.heap_arr = init_array
        self.size = len(init_array)
        self.comparison_function = comparison_function

        # Heapify the initial array
        for i in range(self.size // 2, -1, -1):
            self._heapify_down(i)
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        self.size += 1
        self.heap_arr.append(value)
        self._heapify_up(self.size - 1)

    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        if self.size == 0:
            return None
        
        root = self.heap_arr[0]
        self.heap_arr[0] = self.heap_arr[self.size - 1]  # Move last element to the root
        self.heap_arr.pop()  # Remove last element
        self.size -= 1
        self._heapify_down(0)  # Restore heap property by heapifying down
        return root

    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        if self.size > 0:
            return self.heap_arr[0]
        return None

    def print(self):
        '''
        Prints the current state of the heap (as an array).
        '''
        print(self.heap_arr)

    def _heapify_up(self, index):
        '''Heapify up to restore heap property after insertion.'''
        parent = (index - 1) // 2
        if index > 0 and not self.comparison_function(self.heap_arr[parent], self.heap_arr[index]):
            self.heap_arr[parent], self.heap_arr[index] = self.heap_arr[index], self.heap_arr[parent]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        '''Heapify down to restore heap property after extraction.'''
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and not self.comparison_function(self.heap_arr[smallest], self.heap_arr[left]):
            smallest = left

        if right < self.size and not self.comparison_function(self.heap_arr[smallest], self.heap_arr[right]):
            smallest = right

        if smallest != index:
            self.heap_arr[index], self.heap_arr[smallest] = self.heap_arr[smallest], self.heap_arr[index]
            self._heapify_down(smallest)

    def heap_sort(self):
        '''Sort the heap using heap sort (in-place sorting).'''
        sorted_array = []
        original_size = self.size
        # Repeatedly extract the top element (min/max based on heap type) to sort
        for _ in range(original_size):
            sorted_array.append(self.extract())
        return sorted_array

    def is_empty(self):
        '''
        Returns True if the heap is empty, otherwise False.
        '''
        return self.size == 0
    
    def copy(self):
        '''
        Arguments:
            None
        Returns:
            Heap : A copy of the current heap
        Description:
            Creates and returns a copy of the current heap.
        Time Complexity:
            O(n) where n is the number of elements in the heap
        '''
        # Create a new heap with the same comparator and a copy of the current heap array
        return Heap(self.comparison_function, self.heap_arr.copy())
    
    def getload(self):
        total_load = 0
        for crew_member in self.heap_arr:
            total_load += crew_member.load
        return total_load


# Comparison functions for different heap types
def min_comparator(a, b):
    return a < b  # Min-Heap comparator

def max_comparator(a, b):
    return a > b  # Max-Heap comparator

def min_load(a, b):
    return a.load < b.load  # Min-heap based on crewmate load
def min_com(a, b):
    return a.total_com < b.total_com

def max_priority(a, b):
    return a.priority < b.priority  # Max-heap based on priority

def id_comparator(a, b):
    
    return a.id < b.id

def heapsort(arr):

    # Step 1: Create a min-heap based on the `id` of the treasures
    heap = Heap(id_comparator, arr.copy())

    # Step 2: Extract the elements one by one and store them in sorted order
    sorted_list = []
    while not heap.is_empty():
        sorted_list.append(heap.extract())
    
    return sorted_list
