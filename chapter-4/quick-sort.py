def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage
print(quicksort([3, 6, 8, 10, 1, 2, 1]))
print(quicksort([1, 2, 3, 4, 5]))
print(quicksort([5, 4, 3, 2, 1]))
print(quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
print(quicksort([]))
print(quicksort([1]))
print(quicksort([1, 1, 1, 1, 1]))
print(quicksort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Test cases
assert quicksort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
assert quicksort([]) == []
assert quicksort([1]) == [1]