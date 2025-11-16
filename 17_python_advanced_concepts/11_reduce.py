# Reduce
# The reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value. reduce is not a built-in function; it must be imported from the functools module.

# Syntax: reduce(function, iterable[, initializer])

# function: A function that takes two arguments.
# iterable: The iterable to be reduced.
# initializer (optional): If provided, it's placed before the items of the iterable in the calculation and serves as a default when the iterable is empty.



from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
#         [3, 3, 4, 5, 6]
#         [6, 4, 5, 6]
#         [10, 5, 6]
#         [15, 6]
#         [21]

def sum(a, b):
    return a + b 

c = reduce(sum, numbers)
print(c)