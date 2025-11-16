name = "aniketsinghlodhi" # string
print(name)
print(type(name))

roll_number = 12345      # integer 
print(roll_number)     
print(type(roll_number))

age = 21                # integer
print(age)
print(type(age))

CGPA = 9.1        # float   
print(CGPA) 
print(type(CGPA))

is_student = True    # boolean
print(is_student)
print(type(is_student))
# in python , variables are dynamically typed, so we don't need to declare the type explicitly. in python ,vairable are used to store that can be used and manipulated throughout the program. a variable is created the moment you first assign a value to it. 
# rules for naming variables in python:
# variable names can contain letters, numbers, and underscores, but they cannot start with a number. variable names are case-sensitive.
# variable names should be descriptive and meaningful to improve code readability.  
# example of invalid variable names:
# 1. 2name = "aniket"  (cannot start with a number)
# 2. name@ = "aniket"  (cannot contain special characters except underscore)
# 3. class = "student"  (cannot use reserved keywords)      
# example of valid variable names:
# 1. name_1 = "aniket"
# 2. studentName = "aniket"
# 3. _age = 21
# conventions for naming variables:
# 1. use lowercase letters and separate words with underscores (snake_case) for better readability
# 2. use descriptive names that convey the purpose of the variable
# 3. avoid using single-character variable names except for loop counters or temporary variables    
# 4. follow consistent naming conventions throughout the codebase
# 5. avoid using reserved keywords as variable names
# examples of good variable names:
# 1. student_name = "aniket"
# 2. total_marks = 95
# 3. is_enrolled = True     
# examples of bad variable names:
# 1. x = "aniket" (not descriptive)
# 2. a = 95 (not descriptive)
# 3. b = True (not descriptive) 
 

# python is a dynamically typed language, which means that you don't need to declare the type of a variable when you create it. The type is inferred based on the value assigned to the variable. You can also change the type of a variable by assigning a value of a different type to it later in the code. For example:
variable = 10          # initially an integer
print(variable)
print(type(variable))   
variable = "Hello"    # now a string
print(variable)
print(type(variable))
variable = 3.14      # now a float
print(variable)     
print(type(variable))
variable = False     # now a boolean
print(variable)
print(type(variable))
# this flexibility allows for rapid development and prototyping, but it also requires careful management of variable types to avoid runtime errors.
# on the other hand, statically typed languages like Java or C++ require you to declare the type of a variable explicitly when you create it, and the type cannot be changed later in the code. This can lead to more robust and optimized code, but it also requires more upfront planning and can slow down development.
