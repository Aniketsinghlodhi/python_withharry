def add(a,b):
    x = a+b
    return x
    
a = add(4,5)
print(a)

# Positional Arguments
def add(a, b): # here a and b are parameter and 5 and 3 arguments
    return a + b

print(add(5, 3))  # Output: 8


# Default Arguments
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!


# Keyword Arguments
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Bob")