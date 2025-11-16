print("hello Aniket , how are you? \n I hope you are doing well.") # Example of newline escape sequence
print("This is the first line.\nThis is the second line.")
print("This is a tabbed line.\tSee the space before 'See'?") # Example of tab escape sequence
# Including quotes within strings using escape sequences    

print("He said, \"Python is awesome!\"")# Using backslash to escape double quotes
print('She replied, \'Indeed, it is great!\'')# Using backslash to escape single quotes

print('It\'s a beautiful day!')  # Using backslash to escape single quote within single-quoted string
print("He said, \"It's a beautiful day!\"")  # Using backslash to escape double quotes within double-quoted string
# Using backslash to include special characters called escape sequences and used to represent certain whitespace characters within strings.
print("This is a backslash: \\") # Backslash example
print("This is a double quote: \"")  # Double quote example
print('This is a single quote: \'')  # Single quote example
print("First Line\nSecond Line")  # Newline example             
print("First Line\rSecond Line")  # Carriage return example
print("Column1\tColumn2\tColumn3")  # Tab example
print("This is a form feed character:\fSee the space before 'See'?")
print("This is a vertical tab character:\vSee the space before 'See'?")
print("This is a bell character:\a")  # Bell/alert character     
print("This is a backspace character: ABC\bD")  # Backspace example
print("This is a null character:\0See the space before 'See'?")  # Null character example   



# print statement automatically print space between multiple arguments
print("Hello", "World", "from", "Python!")  # Outputs: Hello World

# You can customize the separator using the 'sep' parameter
print("Hello", "World", "from", "Python!", sep="-")  # Outputs: Hello-World-from-Python!

# You can customize the end character using the 'end' parameter
print("Hello, World!", end="***")  # Outputs: Hello, World!
print("This is the next line after custom end.")

# Combining 'sep' and 'end' parameters
print("Python", "is", "fun!", sep=" | ", end=" <END>\n")  # Outputs: Python | is | fun! <END>
print("This is the next line after custom sep and end.")    
print("Escape sequences allow you to include special characters in strings.")
print("They help format text and include characters that are otherwise hard to type.")
print("Common escape sequences include:")
print("\\n for newline")
print("\\t for tab")
print("\\' for single quote")
print('\\" for double quote')
print("\\\\ for backslash")
print("Using escape sequences can enhance the readability and formatting of your output.")
print("You can also use escape sequences in combination with print function parameters like sep and end.")
print("This allows for even more control over how your output is displayed.")       
print("Happy coding with Python!")
print("This is a raw string where escape sequences are not processed: r\"Hello\\nWorld\"")  # Raw string example
print(r"This is another raw string: r'C:\\Users\\Name\\Documents'")
print(r"Raw strings treat backslashes literally: r'Line1\nLine2\tTabbed'")
print("Normal string with escape sequences: \"Hello\\nWorld\"")  # Normal string
print("Another normal string: 'C:\\Users\\Name\\Documents'")  # Normal string   
print("Normal strings process escape sequences: \"Line1\nLine2\tTabbed\"")  # Normal string with escape sequences   
print("Mixing raw and normal strings:")
print("Raw part: r'Path\\to\\file' and Normal part:" )
print("Path\\to\\file'")  # Normal stringPath\to\file'")  # Normal string
# print("This shows how raw strings and normal strings handle backslashes differently.")Path\to\file'")  # Normal string
print("This shows how raw strings and normal strings handle backslashes differently.")      
print(r"Raw string: r'Hello\\nWorld'")  # Raw string
print("Normal string: \"Hello\\nWorld\"")  # Normal string with escape sequences
print("In the raw string, the backslash and 'n' are treated literally.")

print("In the normal string, the backslash and 'n' create a newline.")
# print("This demonstrates the difference between raw strings and normal strings in Python.")Path\to\file'")  # Normal string
print("This shows how raw strings and normal strings handle backslashes differently.")
print(r"Raw string: r'Hello\\nWorld'")  # Raw string
print("Normal string: \"Hello\\nWorld\"")  # Normal string with escape sequences
print("In the raw string, the backslash and 'n' are treated literally.")
print("In the normal string, the backslash and 'n' create a newline.")
print("This demonstrates the difference between raw strings and normal strings in Python.")


print("Mixing raw and normal strings:")
print("Raw part: r'Path\\to\\file' and Normal part:" ) 
print("Path\\to\\file'")  # Normal string
print("Path\\to\\file'")  # Normal string
print("This shows how raw strings and normal strings handle backslashes differently.")  
print("This shows how raw strings and normal strings handle backslashes differently.")
print(r"Raw string: r'Hello\\nWorld'")  # Raw string
print("Normal string: \"Hello\\nWorld\"")  # Normal string with escape sequences
print("In the raw string, the backslash and 'n' are treated literally.")
print("In the normal string, the backslash and 'n' create a newline.")
