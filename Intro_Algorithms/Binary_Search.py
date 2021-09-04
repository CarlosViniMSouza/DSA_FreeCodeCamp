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