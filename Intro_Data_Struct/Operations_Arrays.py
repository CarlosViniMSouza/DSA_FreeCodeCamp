# accessing a array:

code = [0, 4, 2, 7, 5, "XTW"]

code[3] # output: 7
code[5] # output: XTW

# List Length - To determine the number of items in a list, use the len function.

len(code) # output: 6

# List Operations

# To add to a list, use the append(x) method:

code.append(4) # output: [0, 4, 2, 7, 5, "XTW", 4]

# To add (or concatenate) one list to another, use extend(iterable):

code.extend([8, 4, 2]) # output: [0, 4, 2, 7, 5, "XTW", 4, [8, 4, 2]]

# To insert an item into a list at a given position. Here the value 11 is inserted at index position 10:

code.insert(8, "AGT") # output: [0, 4, 2, 7, 5, "XTW", 4, "AGT", [8, 4, 2]]

# Use the remove(x) method to remove an item from a list.remove() takes a value as an argument and removes the first element in the list that matches the argument:

code.remove("XTW") # output: [0, 4, 2, 7, 5, 4, "AGT", [8, 4, 2]]

# Searching for the position of an element in a list is possible using the index(x):

code.index(4) # output: 5

# List Membership - Use the in and not in operators to test for membership in a list.

if 5 in code: print(True)
# output: True

if 10 in code: print(True)
# output: False
