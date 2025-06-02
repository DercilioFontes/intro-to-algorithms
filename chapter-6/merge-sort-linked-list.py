class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sort_linked_list(head):
    """Sorts a linked list using the merge sort algorithm."""
    if head is None or head.next is None:
        return head

    # Split the linked list into two halves
    mid = get_middle(head)
    mid_next = mid.next
    mid.next = None  # Split the list

    # Recursively sort both halves
    left_sorted = merge_sort_linked_list(head)
    right_sorted = merge_sort_linked_list(mid_next)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def get_middle(head):
    """Finds the middle node of the linked list."""
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    """Merges two sorted linked lists into one sorted linked list."""
    if left is None:
        return right
    if right is None:
        return left

    if left.data < right.data:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result

# # Example usage
linked_list = Node(4)
linked_list.next = Node(2)
linked_list.next.next = Node(1)
linked_list.next.next.next = Node(3)
sorted_linked_list = merge_sort_linked_list(linked_list)
print("Sorted linked list is:", end=" ")

def print_linked_list(head):
    """Helper function to print the linked list."""
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
print_linked_list(sorted_linked_list)
