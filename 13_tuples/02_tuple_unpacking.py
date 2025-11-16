tu = (32,34,54,54,33)
a,b,c,d,e = tu


print(a,b,c,d,e)#outpur 32,34,54,54,33

#example 

student = ("Aniket", 19, "CSE")

# Tuple Unpacking:
# Unpacking means extracting multiple values from a tuple into individual variables.
# The number of variables MUST match the number of values in the tuple.
# Useful when handling structured data like coordinates, database rows, user info etc.
name, age, branch = student

print(name)   # Aniket
print(age)    # 19
print(branch) # CSE