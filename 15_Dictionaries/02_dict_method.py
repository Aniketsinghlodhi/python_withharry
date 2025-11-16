
my_dict = {
    "name": "Aniket",
    "age": 20,
    "course": "B.Tech CSE",
    "skills": ["Python", "Blockchain", "AI"]
}

# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# my_dict.clear() # empties dicrtionaries 
# my_dict.pop("age") # Removes "age" keys 
# print(my_dict)

# Accessing Dictionary Elements
# Access using key
print(my_dict["name"])   # Output: Aniket

# Using get() method (safe)
print(my_dict.get("age"))  # Output: 20
print(my_dict.get("city", "Not Found"))  # Avoids KeyError

# Adding & Updating Elements
# Add a new key-value pair
my_dict["city"] = "Sagar"

# Update existing value
my_dict["age"] = 21

print(my_dict)

# Removing Elements
# pop() → Removes key and returns its value
my_dict.pop("age")

# popitem() → Removes the last inserted item
my_dict.popitem()

# del → Delete a specific key
del my_dict["course"]

# clear() → Remove all items
my_dict.clear()

print(my_dict)