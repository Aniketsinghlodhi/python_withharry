  #  stings are immutable
name = "Aniketsinghlodhi"
# name[0] = "S"
# alteration isn't possible in string , we cannot do this 
a = len(name)
print(a)
print(name.upper() , name)
print(name.lower() , name)
print(name.capitalize() , name)
print(name.title() , name)

# Removing Whitespace
text = "   Hello Aniket.  "
print(text.strip())
print(text.lstrip())
print(text.rstrip())


# Finding And Replacking 
text = "Python is fun "
print(text.find("is")) # output is 7 index of first occurance
print(text.replace("fun", "Awesome"))

#Splitting And joining 
fruits = "Apple, Bananas, Pineapples, Mangoes, Dates, Plum , Grapes " 
print(fruits.split())
print(",".join(['Apple,', 'Bananas,', 'Pineapples,', 'Mangoes,', 'Dates,', 'Plum', ',', 'Grapes']))

# Checking String properties 
text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False