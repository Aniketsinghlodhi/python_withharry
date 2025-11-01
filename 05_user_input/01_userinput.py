# The input() function allows you to take input from the keyboard.  by default, it takes input as a string. you can also convert the input to other data types as needed.
# Example 1: Taking string input
name = input("Enter your name: ")
print("Hello, " + name + "!")   


# Example 2: Taking integer input
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")    

# Example 3: Taking float input
height = float(input("Enter your height in meters: "))
print("You are " + str(height) + " meters tall.")   

# Example 4: Taking multiple inputs
x, y = map(int, input("Enter two numbers separated by space: ").split())
print("The sum of the two numbers is: " + str(x + y))

# Example 5: Taking list input
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
print("The numbers you entered are: " + str(numbers))

# Example 6: Taking boolean input
bool_input = input("Enter True or False: ")
bool_value = bool_input.lower() in ['true', '1', 't', 'yes']
print("The boolean value is: " + str(bool_value))   

# Example 7: Taking character input
char = input("Enter a single character: ")[0]
print("You entered the character: " + char)     
# Example 8: Taking input with a default value
default_value = input("Enter something (or press Enter to use default 'Hello'): ") or "Hello"
print("You entered: " + default_value)

# Example 9: Taking password input (input will not be displayed on the screen)
import getpass
password = getpass.getpass("Enter your password: ")
print("Password entered successfully.") 

# Example 10: Taking input in a loop until a valid integer is entered
while True:
    try:
        number = int(input("Enter a valid integer: "))
        print("You entered the integer: " + str(number))
        break
    except ValueError:
        print("That's not a valid integer. Please try again.")


            
            
            
# Example 11: Taking input with a prompt message
prompt = "Please enter your favorite color: "
favorite_color = input(prompt)
print("Your favorite color is: " + favorite_color)      

# Example 12: Taking input and stripping whitespace
whitespace_input = input("Enter something with extra spaces: ")
stripped_input = whitespace_input.strip()
print("You entered: '" + stripped_input + "' without extra spaces.")    

# Example 13: Taking input and converting to uppercase
upper_input = input("Enter something: ")
uppercased = upper_input.upper()
print("You entered in uppercase: " + uppercased)    

# Example 14: Taking input and converting to lowercase  
lower_input = input("Enter something: ")
lowercased = lower_input.lower()
print("You entered in lowercase: " + lowercased)

# Example 15: Taking input and calculating its length
length_input = input("Enter something: ")
length = len(length_input)
print("The length of the input is: " + str(length)) 

# Example 16: Taking input and reversing the string
reverse_input = input("Enter something: ")
reversed_string = reverse_input[::-1]
print("The reversed input is: " + reversed_string)  

# Example 17: Taking input and checking if it's a digit
digit_input = input("Enter something: ")
is_digit = digit_input.isdigit()
print("Is the input a digit? " + str(is_digit)) 

# Example 18: Taking input and checking if it's alphabetic
alpha_input = input("Enter something: ")
is_alpha = alpha_input.isalpha()
print("Is the input alphabetic? " + str(is_alpha))  

# Example 19: Taking input and checking if it's alphanumeric
alnum_input = input("Enter something: ")
is_alnum = alnum_input.isalnum()    
print("Is the input alphanumeric? " + str(is_alnum))

# Example 20: Taking input and formatting it    
format_input = input("Enter your first and last name separated by space: ")
first_name, last_name = format_input.split()
formatted_name = "First Name: {}, Last Name: {}".format(first_name, last_name)
print(formatted_name)

# Example 21: Taking input and joining a list of strings
string_list_input = input("Enter multiple words separated by space: ")
string_list = string_list_input.split()
joined_string = "-".join(string_list)
print("Joined string: " + joined_string)        

# Example 22: Taking input and finding the maximum value
max_input = list(map(int, input("Enter a list of numbers separated by space: ").split()))
max_value = max(max_input)
print("The maximum value is: " + str(max_value))    

# Example 23: Taking input and finding the minimum value
min_input = list(map(int, input("Enter a list of numbers separated by space: ").split()))
min_value = min(min_input)
print("The minimum value is: " + str(min_value))            

# Example 24: Taking input and calculating the average
avg_input = list(map(int, input("Enter a list of numbers separated by space: ").split()))
average = sum(avg_input) / len(avg_input)       
print("The average is: " + str(average))    

# Example 25: Taking input and sorting a list of numbers
sort_input = list(map(int, input("Enter a list of numbers separated by space: ").split()))
sorted_list = sorted(sort_input)
print("The sorted list is: " + str(sorted_list))    

# Example 26: Taking input and removing duplicates from a list  
dup_input = list(map(int, input("Enter a list of numbers separated by space: ").split()))
unique_list = list(set(dup_input))
print("The list without duplicates is: " + str(unique_list))    

# Example 27: Taking input and counting occurrences of an element
count_input = list(map(int, input("Enter a list of numbers separated by space: ").split()))
element = int(input("Enter the element to count: "))
count = count_input.count(element)
print("The element " + str(element) + " occurs " + str(count) + " times.")

# Example 28: Taking input and finding the index of an element
index_input = list(map(int, input("Enter a list of numbers separated by space: ").split()))
element_index = int(input("Enter the element to find its index: "))
if element_index in index_input:
    index = index_input.index(element_index)
    print("The index of element " + str(element_index) + " is: " + str(index))
else:
    print("Element not found in the list.")


# Example 29: Taking input and checking if a substring exists
substring_input = input("Enter a string: ")
substring = input("Enter a substring to search for: ")
exists = substring in substring_input
print("Does the substring exist? " + str(exists))   


# Example 30: Taking input and replacing a substring
replace_input = input("Enter a string: ")
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring: ")
replaced_string = replace_input.replace(old_substring, new_substring)
print("The modified string is: " + replaced_string) 

# Example 31: Taking input and splitting a string into a list
split_input = input("Enter a string with words separated by commas: ")      
split_list = split_input.split(",")
print("The list of words is: " + str(split_list))   

# Example 32: Taking input and joining a list into a string
join_list_input = input("Enter multiple words separated by space: ")
join_list = join_list_input.split()
joined_string = " ".join(join_list)         
print("The joined string is: " + joined_string) 


# Example 33: Taking input and checking if it's empty   
empty_input = input("Enter something (or press Enter to leave it empty): ")
is_empty = empty_input == ""
print("Is the input empty? " + str(is_empty))       
# Example 34: Taking input and converting to title case
title_input = input("Enter something: ")
title_cased = title_input.title()
print("You entered in title case: " + title_cased)                          

# Example 35: Taking input and checking if it starts with a specific prefix
prefix_input = input("Enter something: ")
prefix = input("Enter the prefix to check: ")       
starts_with = prefix_input.startswith(prefix)
print("Does the input start with the prefix? " + str(starts_with))  





