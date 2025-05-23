def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    """Merges two sorted arrays into one sorted array."""
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from both halves
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Example usage
list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = merge_sort(list)
print("Sorted array is:", sorted_list)  # Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]

# Test cases
assert merge_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
assert merge_sort([]) == []
assert merge_sort([1]) == [1]
assert merge_sort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]