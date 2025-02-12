# Heap
Array based heap data structure built from scratch-python

# Heap Implementation in Python

## Overview

This project implements a Min-Heap in Python with functionalities for inserting, deleting, and heapifying elements. It includes helper functions for tree navigation and maintaining heap properties.

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

### 4. `smol(ind, hp, ln) -> int`

Finds the index of the smaller child of a given node.

- Returns `-1` if no children exist.

### 5. `heapify(arr) -> list`

Converts an input list into a Min-Heap using an incremental approach.

- Returns the heap as a list.

### 6. `hins(a, hp)`

Inserts a new element `a` into the heap `hp`.

- Performs an upward heapify operation to maintain the heap property.

### 7. `hdel(ind, hp)`

Deletes the element at index `ind` from the heap `hp`.

- Swaps the target element with the last element and removes it.
- Performs a downward heapify operation to restore heap order.
- Prints intermediate index movements for debugging.

## Example Usage

```python
l = [2, 5, 4, 3, 7, 9, 6]
z = heapify(l)
print(z)
hins(1,z)
print(z)
hdel(2, z)
print(z)
hdel(0, z)
print(z)

```

## Future Improvements

- Implement a max-heap variant.
- Optimize `heapify()` to use a more efficient bottom-up approach.
- Add error handling for invalid indices.

## License

This project is open-source and available for modification and distribution.

