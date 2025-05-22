def insertion_sort(arr):
    """
    Perform insertion sort on the given array.

    :param arr: List of elements to be sorted
    :return: Sorted list of elements
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

# Example usage
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)  # Output: Sorted array: [5, 6, 11, 12, 13]

# Test cases
assert insertion_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]
assert insertion_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert insertion_sort([1]) == [1]
assert insertion_sort([]) == []
assert insertion_sort([2, 1]) == [1, 2]