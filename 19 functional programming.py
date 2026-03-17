# Types of programming
# 1.Sequential 
# 2.functional
# 3.OOP

# 2.Functional Programming
# TASK 1
# def addTwo(num1,num2,num3):
#     res = num1+num2+num3
#     print(f"Addition of {num1},{num2} and {num3} =" ,res)
# addTwo(5,20,40)

# TASK 2
# def gmail(id,passw):
#     id =(id)
#     passw =(passw)
#     print(f"ID and Passw is {id} and {passw} = ",id,passw)
# gmail("abc123",134)

# TASK 3
# num = int(input("Enter a number: "))
# def cube(num):
#     print("Cube of a number is =", num**3)
# cube(num)

# TASK 4
# def square_list(lst):
#     for i in lst:
#         print(i*i)

# # Given list
# lst = [1, 2, 3, 4, 5]

# square_list(lst)


# HOMEWORK
# Star Triangle
def pattern_triangle(n):
    for i in range(1, n+1):
        print("*" * i)
pattern_triangle(5)


# Pyramid
def pattern_pyramid(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "*"*(2*i-1))
pattern_pyramid(5)

#Prime Number Check
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
print(is_prime(7))


# Even / Odd Check
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(10))


# Palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))


# Reverse String
def reverse_string(s):
    return s[::-1]
print(reverse_string("python"))


# Table Printing
def print_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)
print_table(5)