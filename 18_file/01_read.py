# Read, Write, and Append Files
# Python provides several modes for opening files:

# 'r' (Read mode): Opens the file for reading. This is the default mode. If the file doesn't exist, you'll get an error.
# 'w' (Write mode): Opens the file for writing. If the file exists, its contents will be overwritten. If the file doesn't exist, a new file will be created.
# 'a' (Append mode): Opens the file for appending. Data will be added to the end of the file. If the file doesn't exist, a new file will be created.

try:
    file = open("my_file.txt", "r")  # Open in read mode
    content = file.read()  # Read the entire file content
    print(content)
    file.close()  # Close the file
except FileNotFoundError:
    print("File not found.")


# Reading line by line
try:
    file = open("my_file.txt", "r")
    for line in file: # Efficient for large files
        print(line.strip()) # Remove newline characters
    file.close()
except FileNotFoundError:
    print("File not found.")
