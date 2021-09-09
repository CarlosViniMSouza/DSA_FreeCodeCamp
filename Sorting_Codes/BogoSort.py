import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def is_sorted(values):

    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
        return True

# The bogosort function will also take the list
# of values it's working with as a parameter.
