def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(f"Sorted array: {sorted_arr}")  # Output: Sorted array: [11, 12, 22, 25, 34, 64, 90]

# Test cases
assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert bubble_sort([1]) == [1]  # Single element
assert bubble_sort([]) == []  # Empty list