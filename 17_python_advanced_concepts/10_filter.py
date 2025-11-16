# Filter
# The filter() function constructs an iterator from elements of an iterable for which a function returns True. In other words, it filters the iterable based on a condition.

# Syntax: filter(function, iterable)

# function: A function that returns True or False for each item. If None is passed, it defaults to checking if the element is True (truthy value).
# iterable: The iterable to be filtered.


# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    
a = [1, 3, 5, 234, 34, 32, 6543, 23, 2 ,5 , 6, 7 ,43]

new = list(filter(lambda x: x>9, a))
print(new) 