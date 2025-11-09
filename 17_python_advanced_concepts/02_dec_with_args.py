
# Decorators themselves can also accept arguments. This requires another level of nesting: an outer function that takes the decorator's arguments and returns the actual decorator function.

def repeat(n):
    def decorator(func):
        def  wrapper(a):
            for i in range (n):
                
                func(a)
        return wrapper
    return decorator


@repeat(7)
def say_hello(a):
    print(f"hello!{a}")

    '''
    it replaces the function say_hello with this 
    def decorator(func):
        def  wrapper(a):
            for i in range (n):
                func(a)
        return wrapper
    
    '''

say_hello("Aniketsingh")
