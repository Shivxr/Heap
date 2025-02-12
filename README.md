# Heap
Array based heap data structure built from scratch-python

# Heap Implementation in Python

## Overview

This project implements both **Min-Heap** and **Max-Heap** in Python with functionalities for inserting, deleting, and heapifying elements. It includes helper functions for tree navigation and maintaining heap properties.

## Functions

### 1. `parent(ind) -> int`

Returns the parent index of a given node in the heap.

- Returns `-1` if the node is the root.

### 2. `left(ind, ln) -> int`

Returns the left child index of a given node.

- Returns `-1` if the left child does not exist.

### 3. `right(ind, ln) -> int`

Returns the right child index of a given node.

- Returns `-1` if the right child does not exist.

### 4. `smol(ind, hp, ln) -> int` (Min-Heap)

Finds the index of the smaller child of a given node.

- Returns `-1` if no children exist.

### 5. `lar(ind, hp, ln) -> int` (Max-Heap)

Finds the index of the larger child of a given node.

- Returns `-1` if no children exist.

### 6. `heapify(arr) -> list`

Converts an input list into a Min-Heap or Max-Heap using an incremental approach.

- Returns the heap as a list.

### 7. `hins(a, hp)`

Inserts a new element `a` into the heap `hp`.

- Performs an upward heapify operation to maintain the heap property.

### 8. `hdel(ind, hp)`

Deletes the element at index `ind` from the heap `hp`.

- Swaps the target element with the last element and removes it.
- Performs a downward heapify operation to restore heap order.
- Prints intermediate index movements for debugging.

## Example Usage

### Min-Heap Example:
```python
from min_heap import heapify,hins,hdel

l = [2, 5, 4, 3, 7, 9, 6]
z = heapify(l)
print(z)
hins(1, z)
print(z)
hdel(2, z)
print(z)
hdel(0, z)
print(z)
```

### Max-Heap Example:
```python
from max_heap import heapify,hins,hdel

l = [2, 5, 4, 3, 7, 9, 6]
z = heapify(l)
print(z)
hins(10, z)
print(z)
hdel(2, z)
print(z)
```

## Future Improvements

- Optimize `heapify()` to use a more efficient bottom-up approach.
- Add error handling for invalid indices.
- Implement additional heap operations like `peek()` and `heap_sort()`.

## License

This project is open-source and available for modification and distribution.

