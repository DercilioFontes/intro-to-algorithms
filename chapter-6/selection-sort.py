def selection_sort(arr):
    """
    Perform selection sort on the given list.

    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        # Test against elements after i to find the smallest
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)  # Output: Sorted array: [11, 12, 22, 25, 64]

# Test cases
assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]
assert selection_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert selection_sort([1]) == [1]
assert selection_sort([]) == []
assert selection_sort([2, 1]) == [1, 2]
