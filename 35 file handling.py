# File handling
# File handling is used to create, read, update, delete [CRUD] operation of a data.
# file handling is used to store data peranently in a memory.

# Modes in file handling
# x mode : create a new file

# r mode : read data from file "File must be present at the location"
# read()
# readline()
# readlines()
# r+ : read data first and then write

# w : to write data into file "if file is not present it will create a file and write in it"
# write()
# writelines()
# w+ : write data first then read

# a mode : write data into file, it will add data at the last in file.
# "if file is not present it will create a file and write in it"
# a+ : append into file then read 


# for binary files(image, video, audio, pdf) all the operations are same 
# rb mode : read data from file "File must be present at the location"
# read()
# readline()
# readlines()
# rb+ : read data first and then write

# wb : to write data into file "if file is not present it will create a file and write in it"
# write()
# writelines()
# wb+ : write data first then read

# a mode : write data into file, it will add data at the last in file.
# "if file is not present it will create a file and write in it"
# ab+ : append into file then read 

# fd = open("data.txt", "x")
# fd = open("data.txt", "r")


# READ METHOD()
# import os
# print(os.getcwd())

# try:
#     fd = open("data.txt", "r")
#     data = fd.read()

# except FileNotFoundError:
#     print("file not found")

# else:
#     print("file open successfully")
#     print(data)
#     for i in data:
#         print(i)


# LINE METHOD()
# try:
#     fd = open("data.txt", "r")
#     line = fd.readline()

# except FileNotFoundError:
#     print("file not found")

# else:
#     print("file open successfully")
#     print(line)
#     for i in line:
#         print(i)
# finally:
#     print("This block will alway execute")
#     if 'fd' in locals():
#         fd.close()
#     print("file closed")

# try:
#     with open("data.txt", "r") as fd:
#         lines = fd.readline()
#         for line in line:
#             print(line)
# except FileNotFoundError:
#     print("file not found")


# LINES METHOD()
# try:
#     fd = open("data.txt", "r")
#     lines = fd.readlines()

# except FileNotFoundError:
#     print("file not found")

# else:
#     print("file open successfully")
#     print(lines)
#     for i in lines:
#         print(i)
# finally:
#     print("This block will alway execute")
#     if 'fd' in locals():
#         fd.close()
#     print("file closed")

# try:
#     with open("data.txt", "r") as fd:
#         lines = fd.readline()
#         for line in lines:
#             print(line)
# except FileNotFoundError:
#     print("file not found")


# WITH OPEN METHOD
# try:
#     with open("db.txt", "w") as fd:
#         fd.write("This is text file.\n")


# except Exception as e:
#     print(f"An error occured: {e}")


# APPEND METHOD()
# try:
#     with open("db.txt", "a") as fd:
#         fd.write("This is text file.\n")


# except Exception as e:
#     print(f"An error occured: {e}")


# 
# filename = input("Enter filename: ")
# mode = input("Enter mode r/w/a: ")


# try:
#     fd = open("filename", "mode")
#     data = fd.read()

# except FileNotFoundError:
#     print("file not found")

# else:
#     print("file open successfully")
#     print(data)
#     for i in data:
#         print(i)

# finally:
#     print("This block will alway execute")
#     if 'fd' in locals():
#         fd.close()
#     print("file closed")


# create 2 file and copy content of one file into another file 
# Step 1: Create and write to source file
with open("file1.txt", "w") as f1:
    f1.write("Hello, this is a sample text.\nWelcome to Python file handling.")

# Step 2 & 3: Read from file1 and write to file2
with open("file1.txt", "r") as f1, open("file2.txt", "w") as f2:
    content = f1.read()
    f2.write(content)

print("Content copied successfully!")