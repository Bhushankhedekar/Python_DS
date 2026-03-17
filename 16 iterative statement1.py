# For loop
# if we know the number of iteration in advance then we use for loop
# for i in range(1,6):
#     print(i)

# for i in range(23,67,2):
#     print(i)

num = 7
is_prime = True

# We check divisors from 2 up to num (not including num)
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

# Final decision using if-else
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# num = 7
# count = 0
# for i in range(1, num+1):
#     if num % == 0:
#         count +=1;
# if coun == 2:
#     print(num,"Is prime")
# else:
#     print(num,"Not prime")

# Loops
# str = "welcome python"
# s = str.split()
# print(s)
# s.reverse()
# print(s)

#1. WAP to check string palindrom using for loop 
str = "nayan"
rev_str = ""
for i in str:
    rev_str = i + rev_str
if str == rev_str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#2. WAP to check string palindrom using indexing 
str = "nayan"
rev_str = ""
for i in range(len(str)-1, -1, -1):
    rev_str = rev_str + str[i]  
if str == rev_str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# str = "Bhushan Khedekar"
# if str == str[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# WAP to check digit palindrom by using for loop
# num = input("Enter a number: ")
# num = 121
# rev_num = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     rev_num = rev_num * 10 + digit
#     temp //= 10
# if num == rev_num:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")

# WAP to check armstrong number by using for loop
# num = 153
# order = len(str(num))
# sum = 0
# temp = num
# for i in range(temp):
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10
# if num == sum:
#     print("The number is an Armstrong number.")
# else:
#     print("The number is not an Armstrong number.")


# num = int(input("Enter a number: "))
# order = len(str(num))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10
# if num == sum:
#     print("The number is an Armstrong number.")
# else:
#     print("The number is not an Armstrong number.")

# Typecasting
# typecasting means converting one data type to another data type.
# typecasting is done by using built-in functions like int(), float(), str(), etc.
# Types of typecasting
# 1. implicit typecasting
# types of implicit typecasting
# 1. int to float
# 2. int to complex
# 3. float to complex
# 4. bool to int
# 5. bool to float
# 6. bool to complex
# 7. str to int
# 8. str to float
# 9. str to complex
# implicit typecasting is done by python automatically when we perform operations on different data types.
# when we perform any operation on two different data types, python automatically converts the lower data type
# example:
# a = 10
# b = 20.5
# c = a + b
# print(c)

# 2. explicit typecasting
# types of explicit typecasting
# 1. float to int
# 2. complex to int
# 3. complex to float
# 4. int to str
# explicit typecasting is done by the programmer by using built-in functions like int(), float(), str(), etc.

# example:
# a = 10
# b = 20.5
# c = a + b
# c = int(c)
# print(c)