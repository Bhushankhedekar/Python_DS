# Homework 
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
