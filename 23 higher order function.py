# Higher order function
#Inbuild Higher order function
# 1.map function
# 2.filter function
# 3.reduce function

# 1.map function
# used for data mapping
# original_marks = [60,69.78,89.34,58]
# grace_marks = []
# # for i in original_marks:
# #     grace_marks.append(i+5)

# # print("grace marks:",grace_marks)
# def addFive(m):
#     return m+5

# grace_marks = list(map(addFive,original_marks)) 
# print(grace_marks)

# Task map original marks with grace marks but don't
# give grace marks to students who scores more than 90
# original_marks = [60, 69.78, 89.34, 58, 94]

# def addFive(m):
#     if m > 90:
#         return m
#     else:
#         return m + 5

# grace_marks = list(map(addFive, original_marks))
# print(grace_marks)

# 2.filter function
# It is used to filter elements from sequence as per condition
# original_marks = [60,69,91,93,78,89.34,58]
# topper_marks = []
# def topper_marks(m):
#     if m > 90:
#         return True
#     else:
#         return False
    
# topperlist = list(filter(topper_marks,original_marks))
# print("Topper marks list :",topperlist)

# Task
# original_marks = [60,69,91,93,78,89,34,58]
# odd_marks = []
# def odd_marks(m):
#     if m % 2 == 0:
#         return False
#     else:
#         return True
    
# oddlist = list(filter(odd_marks,original_marks))
# print("odd marks list:" ,oddlist)

# 3.reduce function
# Its used to reduce sequence to single elment
# from functools import reduce
# original_marks = [60,69,91,93,78,89,34,58]
# def addTwo(a,b):
#     return a+b

# res = reduce(addTwo,original_marks,initial = 0)
# print("sum of all :",res)

# res2 = reduce(addTwo,original_marks,initial = res)
# print("sum of all :",res2)

# 
original_marks = [60,69,91,93,78,89,34,58]

def get_max(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
import functools

maxnum = functools.reduce(get_max,original_marks)
print("Maximum number is :",maxnum)


def get_min(n1,n2):
    if n1<n2:
        return n1
    else:
        return n2
import functools

minnum = functools.reduce(get_min,original_marks)
print("Minimum number is :",minnum)