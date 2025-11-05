
# A tuple in Python is an ordered, immutable collection used to store fixed data like coordinates, records, or configuration values. Because tuples cannot be changed once created, they are faster, memory-efficient, and safer for constant data compared to lists. Tuples allow indexing, slicing, iteration, packing & unpacking, concatenation, repetition, and membership tests. They support only two built-in methods: .count() to count occurrences of a value and .index() to find the position of a value. Other operations come from Python functions and operators such as len(), min(), max(), sum(), in, +, and *. Tuples are ideal when you want secure, fixed, and high-performance data storage.


# Tuple Example (Immutable collection)
marks = (23, 45, 76, 45, 99)

# Access element by index
print(marks[2])         # 76

# Slice tuple
print(marks[1:4])       # (45, 76, 45)

# Count occurrences of a value
print(marks.count(45))  # 2

# Get index of first occurrence
print(marks.index(76))  # 2

# Tuple length
print(len(marks))       # 5

# Check membership
print(45 in marks)      # True

# Concatenate tuples
new_marks = marks + (88, 100)
print(new_marks)        # (23, 45, 76, 45, 99, 88, 100)

# Repeat tuple elements
print(marks * 2)        # (23, 45, 76, 45, 99, 23, 45, 76, 45, 99)

# Tuple packing (grouping data)
student = ("Aniket", 19, "CSE")

# Tuple unpacking (assign each value to variable)
name, age, branch = student
print(name, age, branch)  # Aniket 19 CSE