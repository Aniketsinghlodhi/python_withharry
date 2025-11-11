# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function definition. The order is important: *args must come before **kwargs. You can also include regular positional and keyword parameters.

def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, jack=34, jill=32, marie=31)