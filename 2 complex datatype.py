# complex data type
# complex data type is used to represent complex numbers
# for mathemetical calculations we need complex data type
# image, video processing
# 1.Decimal numbers 
# base 10 system
# 0-9 

#  Note :> python internally converts binary,octal,hexadecimal to decimal before performing any operations

# 2. binary number system 
# 0 and 1 only
# 0b is used to represent binary numbers
# v = 0b1010101010 
# print(v)
# print(type(v))

# inbuild functions are 
# int() is used to convert a string to an integer
# oct() is used to convert a decimal number to an octal number
# hex() is used to convert a decimal number to a hexadecimal number

# def binary_conversion(d):
#     return bin(d)

# d = 19
# res = binary_conversion(d)
# print(res)

# d = 19
# res = bin(d)
# print(res)
# print(type(res))
# r1 = bin(d)
# r2 = bin(6)
# print(r1 + r2)

# octal number system
# 0-7 only
# 0o is used to represent octal numbers
# base 8
# v = 0o1234
# print(v)
# print(type(v))

# hexadecimal number system
# 0-9 and A-F only
# 0x is used to represent hexadecimal numbers
# base 16
# v = 0xface
# print(v)
# print(type(v))

# int function is used to convert a string to an integer
# it takes two arguments, the first argument is the string to be converted and the second argument is the base of the number system

# int()
# i1 = int("0b1" , 2)
# i2 = int("0o1234" , 8)
# i3 = int("0xface" , 16)
# i4 = i1+i2+i3
# print(i1)
# print(i2)
# print(i3)
# print(i4)

# r5 = bin(i2)
# print(r5)

# Note :> real part can be int or float imaginary part can be decimal or float but the imaginary part must end with j or J
# c = 0b1010 + 20.5j
# c2 = -20.5 + 0b1010
# print(c)
# print(c2)

# complex () is used to convert a string to a complex number
# c3 = complex(0b1010 + 20.5j)
# print(c3)

# c4 = complex(0o1234,0xface)
# print(c4)


# Homework 
# 1. accept decimal numbers from console and convert that into binary ,octal, hexadecimal numbers
# eval function is used to evaluate the expression and return the result
a = eval(input("Enter a decimal number: "))
# bin(),oct(),hex() are used to convert a decimal number to binary, octal and hexadecimal numbers respectively
b = bin(a)
c = oct(a)
d = hex(a)
print("Binary representation: ", b)
print("Octal representation: ", c)
print("Hexadecimal representation: ", d)


# 2. accept binary , octal and hexadecimal numbers from console and convert that into decimal numbers
# input is used to take input from the user .
b1 = input("Enter a binary number: ")
b2 = input("Enter an octal number: ")
b3 = input("Enter a hexadecimal number: ")

# after taking input from user/ consol we have to convert it into decimal number using int() function and specifying the base of the number system
# d1, d2, d3 is used to display the decimal representation of binary, octal and hexadecimal numbers respectively.
d1 = int(b1, 2)
d2 = int(b2, 8)
d3 = int(b3, 16)
print("Decimal representation of binary number: ", d1)
print("Decimal representation of octal number: ", d2)
print("Decimal representation of hexadecimal number: ", d3)
