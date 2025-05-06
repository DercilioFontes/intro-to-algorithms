def linear_search(arr, target):
    """
    Perform a linear search on the given array to find the target value.

    :param arr: List of elements to search
    :param target: Value to search for
    :return: Index of the target value in the array, or -1 if not found
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

    # Alternative implementation using a for loop
    # for i in range(len(arr)):
    #     if arr[i] == target:
    #         return i
    # return -1

# Example usage
arr = [1, 2, 3, 4, 5]
target = 3
result = linear_search(arr, target)
print(f"Element {target} found at index: {result}")  # Output: Element 3 found at index: 2

# Test cases
assert linear_search([1, 2, 3, 4, 5], 3) == 2
assert linear_search([1, 2, 3, 4, 5], 6) == -1
assert linear_search([], 1) == -1 # Empty array
assert linear_search([1], 1) == 0 # Single element array
assert linear_search([1], 2) == -1 # Single element array not found
assert linear_search([1, 2, 3, 4, 5], 1) == 0 # First element