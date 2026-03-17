# Pattern printing 
# star fill square
# N = 5
# for r in range(1,N+1):
#     for c in range(1,N+1):
#         print("*",end = " ")
#     print()
# # * * * * * 
# * * * * * 
# * * * * *
# * * * * *
# * * * * *

# print(msg,end = \n,sep = " ")

# star right angle triangle
# N = 5
# for r in range(1,N+1):
#     for c in range(1,r+1):
#         print("*",end = " ")
#     print()
# *
# * *
# * * *
# * * * *
# * * * * *

# numbers right angle triangle
# N = 5
# for r in range(1,N+1):
#     for c in range(1,r+1):
#         print(c,end = " ")
#     print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# same numbers in row  right angle triangle
# N = 5
# for r in range(1,N+1):
#     for c in range(1,r+1):
#         print(r,end = " ")
#     print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# star right angle triangle
N = 5
for r in range(N,0,-1):
    for c in range(1,r+1):
        print("*",end = " ")
    print()

# * * * * *
# * * * *
# * * *
# * *
# *

# star hollow square
   
# *****
# *   *
# *   *
# *   *
# *****

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Cross
n = 5

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pyramaid
n = 5

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

# right side right angle triangle
n = 5

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


















str1 = input("Enter string ")
if str1 == str1[::-1]:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")   
    