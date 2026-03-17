# String 
# String is a sequence of characters. It is a data type in Python that is used to represent text.
# String is a collection of characters enclosed in single quotes, double quotes or triple quotes.
# There is no char data type in python 
# s1 = 'Hello World'
# s2 = "Hello World"
# s3 = '''Hello World'''
# s4 = """Hello World"""
# print(s2)
# print(s3)
# print(s4)
# variable name of [index number] is used to access the character at that index number
# indexing is used to axxess single character from a string
# python have two indexing types i.e positive indexing and negative indexing
# positive indexing starts from 0 and goes to n-1
# negative indexing starts from -1 and goes to -n

# s1 = 'Hello World'
# # print(s1[6])
# # len() function is used to print length of string 
# print(len(s1))
# print(type(s1))
# # -1 is used to print the last character of the string
# print(len(s1)-1)
# print("s[0] = ",s1[0])
# print("s[1] = ",s1[1])
# print("s[2] = ",s1[2])
# print("s[3] = ",s1[3])
# print("s[4] = ",s1[4])
# IndexError :when the string is out of range
# print(s1[12])
# print(s1[-12])


# Task 1: accept any string from console 
# 1 display length of that string
# 2 display first and last index .
# 3 accept any index from user and display character present at that index 


a = input("Enter a string: ")
print("Length of string is:",len(a))
print("Display first index of string is:",a[0])
print("Display last index of string is:",len(a)-1)

b = input("Entter index number: ")
print("Character present at that index is :",a[int(b)])
