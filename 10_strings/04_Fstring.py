#Using .format() Method
#The .format() method allows inserting values into placeholders {}:
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# # We can also specify positional and keyword arguments:
print("{1} is learning {0}".format("Python", "Alice"))  # Output: Alice is learning Python

#f-Strings (Formatted String Literals)
#Introduced in Python 3.6, f-strings are the most concise and readable way to format strings:

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

#Using Expressions in f-Strings
#You can perform calculations directly inside f-strings:
x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}")
#Formatting Numbers
pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")