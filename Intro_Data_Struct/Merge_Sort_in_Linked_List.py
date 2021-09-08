def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sub-lists containing a single node
    - Repeatedly merge the sub-lists to produce sorted sub-lists until one remains

    Returns a sorted linked list

    Takes O(n log n) time
    Takes O(n) space
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sub-lists
    Takes O(log n) time
    """
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half

    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = linked_list()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right, linked_list):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    Takes O(n) space
    Runs in O(n) time
    """

    merged = linked_list()
    merged.add(0)
    current = merged.head
    left_head = left.head
    right_head = right.head

    while left_head or right_head:

        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node

        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:

            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node

            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    head = merged.head.next_node
    merged.head = head

    return merged