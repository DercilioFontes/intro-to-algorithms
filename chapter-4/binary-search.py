def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    :param arr: List[int] - A sorted list of integers.
    :param target: int - The target value to search for.
    :return: int - The index of the target value in the array, or -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print(f"Index of {target} in the array: {result}")  # Output: Index of 5 in the array: 4

# Test cases
assert binary_search([1, 2, 3, 4, 5], 3) == 2
assert binary_search([1, 2, 3, 4, 5], 1) == 0
assert binary_search([1, 2, 3, 4, 5], 5) == 4
assert binary_search([1, 2, 3, 4, 5], 6) == -1
assert binary_search([], 1) == -1
assert binary_search([1], 1) == 0
assert binary_search([1], 2) == -1
assert binary_search([1, 2], 1) == 0
assert binary_search([1, 2], 2) == 1