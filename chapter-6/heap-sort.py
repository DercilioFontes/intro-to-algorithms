def heapfy(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapfy(arr, n, largest)

def heap_sort(arr):
    """Sorts an array using the heap sort algorithm."""
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapfy(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapfy(arr, i, 0)
    return arr

# Example usage
list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = heap_sort(list)
print("Sorted array is:", sorted_list)  # Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]

# Test cases
assert heap_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
assert heap_sort([]) == []
assert heap_sort([1]) == [1]
assert heap_sort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]