# Decorators in Python
# Decorators in Python are a powerful and expressive feature that allows you to modify or enhance functions and methods in a clean and readable way. They provide a way to wrap additional functionality around an existing function without permanently modifying it. This is often referred to as metaprogramming, where one part of the program tries to modify another part of the program at compile time.

# Decorators use Python's higher-order function capability, meaning functions can accept other functions as arguments and return new functions.

# decorators is a function that takes  a function, its create new function inside its body (wrapper) then returns that new functions 
def decorator(func):
    def wrapper():
        print(" i am about to exceute a funciotn .....")
        func()
        print("i have excute this function ....")
    return wrapper

def say_hello():
    print("Hello")

# say_hello()
decorator(say_hello())