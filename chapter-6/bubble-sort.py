def bubble_sort(list):
    """
    Sort a list of integers using the bubble sort algorithm.

    :param list: List[int] - A list of integers to be sorted.
    :return: List[int] - The sorted list of integers.
    """
    n = len(list)
    for i in range(n):
        already_sorted = True

        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                # Swap if the element found is greater than the next element
                list[j], list[j+1] = list[j+1], list[j]
                already_sorted = False

        if already_sorted:
            break
            
    return list

# Example usage
list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(list)
print("Sorted array is:", sorted_list)  # Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]

# Test cases
assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert bubble_sort([1]) == [1]
assert bubble_sort([]) == []
assert bubble_sort([2, 1]) == [1, 2]