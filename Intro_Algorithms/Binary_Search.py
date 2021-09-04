# Iterative Binary Search:

def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        checkup = (first + last) // 2

        if list[checkup] == target:
            return checkup
        elif list[checkup] < target:
            first = checkup + 1
        else:
            last = checkup - 1

    return -1

# end to function (mode: iterative)

# Recursive Search Engine:

def recursive_search_engine(list, target, start = 0, end=None):
    # structure if's:
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_search_engine(list, target, start, mid-1)
        else:
            return recursive_search_engine(list, target, mid+1, end)

# end to function (mode: recursive)