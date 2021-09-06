# accessing a array:

code = [0, 4, 2, 7, 5, "XTW"]

code[3] # output: 7
code[5] # output: XTW

# List Length - To determine the number of items in a list, use the len function.

len(code) # output: 6

# List Operations

# To add to a list, use the append(x) method:

code.append(4, 6) # output: [0, 4, 2, 7, 5, "XTW", 4, 6]

# To add (or concatenate) one list to another, use extend(iterable):

code.extend([8, 4, 2]) # output: [0, 4, 2, 7, 5, "XTW", 4, 6, [8, 4, 2]]
