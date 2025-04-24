def sum_elements(elements):
    """
    Calculate the sum of all elements in the given list.

    :param elements: List of numbers to sum
    :return: Sum of the elements
    """
    total = 0
    for element in elements:
        total += element
    return total
# Example usage
elements = [1, 2, 3, 4, 5]
result = sum_elements(elements)
print(f"Sum of elements: {result}")  # Output: Sum of elements: 15
# Test cases
assert sum_elements([1, 2, 3, 4, 5]) == 15
assert sum_elements([-1, -2, -3]) == -6
assert sum_elements([0, 0, 0]) == 0
assert sum_elements([1]) == 1
assert sum_elements([]) == 0  # Empty list