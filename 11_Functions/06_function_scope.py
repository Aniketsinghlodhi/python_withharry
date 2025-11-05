def sum (a,b):
    # a and b are local variables 
    c = a+b
    z = 1 # its create a local variable called z which is destroyed itself after this function return 
    return c 

def greet():
    z = 32 # its local variable in greet 
    print("hello ")
z = 8 # here z is a global variable 
print(sum(4,5))
print (z) 

# Variable Scope and Docstrings
# In Python, variables have scope (where they can be accessed) and lifetime (how long they exist). Variables are created when a function is called and destroyed when it returns. Understanding scope helps avoid unintended errors and improves code organization.

# Types of Scope in Python
# Local Scope (inside a function) – Variables declared inside a function are accessible only within that function.
# Global Scope (accessible everywhere) – Variables declared outside any function can be used throughout the program.
