def linear_search1(lsts, result):
    """Returns the index position of the target if found,
    else returns -1"""

    for i in range(0, len(lsts)):
        if lsts[i] == result:
            return i
        else:
            return -1

# end to function 1. See a other way:

def linear_search2(lst, target):
    """The code can be cleaned up a bit by using
    the enumerate function on the list."""

    for index, value, in enumerate(lst):
        if value == target:
            return index
        else:
            return -1

# end to function 2.