"""
"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""
text_file = open("./18_file_handling/reading_file_example.txt")
txt = text_file.read()
# Read the whole text as string. If we want to limit the number of characters we want to read,
# we can limit it by passing "int" value to the read(number) method.
print(type(txt))
print(txt)
text_file.close()
# After opened and used the file ALWAYS close it

# Just the first 10 characters
text_file = open("./18_file_handling/reading_file_example.txt")
txt = text_file.read(10)
print(txt)
text_file.close()

# readline()
text_file = open("./18_file_handling/reading_file_example.txt")
line = text_file.readline()
print(line)
text_file.close()

# readlines() read all the text line by line and returns a list of lines
text_file = open('./18_file_handling/reading_file_example.txt')
lines = text_file.readlines()
print(type(lines))
print(lines)
text_file.close()

# After opening a file, we should close it.
# There is a new way of opening files using "with" that close the files by itself.
with open("./18_file_handling/reading_file_example.txt") as text_file:
    lines = text_file.read().splitlines()
    print(lines)

# --- Opening files for writing and updating
"""
"a" - append - will append to the end of the file, if the file does not it creates a new file.
"w" - write - will overwrite any existing content, if the file does not exist it creates.
"""
with open('./18_file_handling/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

with open('./18_file_handling/writtem_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

# --- Deleting Files ---
"""
WE use the os module
"""
import os
if os.path.exists("./18_file_handling/reading_file_example2.txt"):
    os.remove("./18_file_handling/reading_file_example2.txt")
else:
    print("The file does not exist")