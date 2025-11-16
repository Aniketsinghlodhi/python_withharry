
# print() function is used to display output to the console.
# Escape sequences are special characters used within strings to represent certain whitespace characters or to include special characters.
# Raw strings are prefixed with 'r' or 'R' and treat backslashes literally, without interpreting them as escape sequences.
# Normal strings interpret escape sequences and convert them into their corresponding special characters.
# The combination of print function, escape sequences, and raw strings allows for flexible and controlled output formatting in Python.
print("This demonstrates the difference between raw strings and normal strings in Python.") 
# we can used sep and end  to customize the output format
print("Hello", "World", sep=" - ", end="!!!\n")  # Custom separator and end
print("This is the next line after custom sep and end.")
print(r"This is a raw string: r'C:\\Users\\Name\\Documents'")  # Raw string example
print("This is a normal string: 'C:\\Users\\Name\\Documents'")  # Normal string example