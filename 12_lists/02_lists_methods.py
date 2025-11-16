marks = [23, 45, 76,45,99]
print(marks)
marks.append(53)# this will change the original list 
print(marks)


# List used for all examples
marks = [23, 45, 76, 45, 99]

# 1. append() -> add one item at the end of list
marks.append(88)  
# marks becomes [23, 45, 76, 45, 99, 88]

# 2. clear() -> delete/empty entire list
# marks.clear()  
# marks becomes []   ( destroys all data)

# 3. copy() -> creates a duplicate list (good for backup before changes)
backup_marks = marks.copy()  
# Now backup_marks is same as marks but independent

# 4. count() -> count how many times specific value appears
count_45 = marks.count(45)  
# shows 2 because 45 appears twice

# 5. extend() -> add multiple items at once (useful for merging lists)
marks.extend([67, 100])  
# marks becomes [23, 45, 76, 45, 99, 88, 67, 100]

# 6. index() -> find position of first occurrence
pos_76 = marks.index(76)  
# returns index of value 76 (e.g. 2)

# 7. pop() -> remove item by index (default last item) and returns it
last_mark = marks.pop()  
# removes last number (100) and stores it in last_mark

# 8. remove() -> remove first matching value
marks.remove(45)  
# removes first 45 only

# 9. reverse() -> reverse list order
marks.reverse()  
# good for reading in reverse order

# 10. sort() -> sort list ascending by default
marks.sort()  
# marks sorted smallest to highest
# marks.sort(reverse=True) -> for descending order

# 11. __add__() -> join lists using + operator (same as marks + new_list)
new_list = marks.__add__([50, 60])  
# creates a new list with combined values, original unchanged

# -----------------------------
# Quick knowledge bullets
# append -> add one value
# extend -> add multiple values
# insert -> add at specific index (not used above but good to know)
# pop -> remove by index, returns removed value
# remove -> remove by value
# clear -> empty list
# sort -> arrange list
# reverse -> flip list
# copy -> create duplicate
# __add__ -> merge lists
# count -> count occurrences
# index -> find position


marks = [23, 45, 76, 45, 99]

# insert(index, value) -> add element at a specific position
marks.insert(2, 60)  
# insert 60 at index 2
# marks: [23, 45, 60, 76, 45, 99]

# sort(key=None, reverse=False) -> we already saw basic sort
# Using key for advanced sorting (useful in real-world data)
scores = ["10", "2", "100"]
scores.sort(key=int)  
# sorts based on integer value, not string
# scores: ['2', '10', '100']

# reverse() 
# Good for LIFO operations (stack behavior)

# __contains__(value) -> checks if value exists (True/False)
found = marks.__contains__(45)  
# True because 45 is in the list

# __len__() -> internal length function (len() uses it)
length = marks.__len__()  
# same as len(marks)

# __getitem__(index) -> fetch element at index (normally we use [])
first_value = marks.__getitem__(0)  
# gets element at index 0 (23)

# __setitem__(index, value) -> change element at index (normally [])
marks.__setitem__(1, 50)  
# replaces value at index 1 with 50
# marks: [23, 50, 60, 76, 45, 99]

# __delitem__(index) -> delete element by index (like del marks[n])
marks.__delitem__(2)  
# removes value at index 2 (60 removed)

# __mul__(n) -> repeat list n times
nums = [1, 2] * 3  
# [1, 2, 1, 2, 1, 2]

# __iter__() -> used for looping internally (for iterators)
it = marks.__iter__()  
# next(it) would give first element

# __reversed__() -> reverse iterator (not modifying original)
rev = list(reversed(marks))  
# reverse view, safe for read-only actions

# __eq__(list2) -> check if lists are identical
is_equal = marks.__eq__([23, 50, 76, 45, 99])
# returns False here