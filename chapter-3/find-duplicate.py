def find_duplicates(arr):
    """
    Find duplicates in the given array.

    :param arr: List of elements to search
    :return: first duplicate element found in the array
    """
    seen = set()
    for value in arr:
        if value in seen:
            return value
        seen.add(value)
    return None

# Example usage
arr = [1, 2, 3, 4, 5, 1, 2]
result = find_duplicates(arr)
print(f"Duplicate elements: {result}")  # Output: Duplicate elements: [1, 2]

# Test cases
assert find_duplicates([1, 2, 3, 4, 5, 1, 2]) == 1
assert find_duplicates([1, 2, 3, 4, 5]) == None
assert find_duplicates([1, 1, 1, 1]) == 1
assert find_duplicates([1, 2, 3, 4, 5, 6]) == None
assert find_duplicates([]) == None  # Empty list