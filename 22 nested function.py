# 1.Nested function
# 2.Clousers
# 3.Decorators

# 1.Nested function
# Function inside a function
# def outerfun():
#     print("Hello")
#     def innerfun():
#         data = 1234
#         print(data)
#     innerfun()
# outerfun()

# print("Hello all")
# def outer():
#     print("Start of outer dunction")

#     def inner():
#         x = 125
#         print(x)

#     inner()
#     print("End of outer function")

# print("Calling outer function")
# outer()
# print("Bye-bye")


# 2.Clousers
# Clousers are the nested function which remembers the data.
# in clouser it always [return] the inner funtion.
# def outer(x):

#     def inner(y): 
#         return x + y
    
#         def supinner(z):
#             return z
#         return supinner
    
#     return inner

# inner = outer(10)
# print(inner)
# print("12345")

# r1 = inner(30)
# print(r1)

# r2 = inner(60)
# print(r2)

# r3 = inner(90)
# print(r3)

# r4 = supinner(40)
# print(r4)

# Task
# def outer(x):

#     def inner(y):
#         return x + y

#     def supinner(z):
#         return z
    
#     def minner(w):
#         return x * w

#     return inner, supinner, minner 


# inner, supinner, minner  = outer(10)

# print(inner(30))   
# print(inner(60))  
# print(inner(90))   

# print(supinner(40))  
# print(minner(40))  
 

# 3.Decorator
# Higher order function
# It is a function which take another function as a input
# Decorators = clousers + higher order function
# Decorators is a higher order function which modify or improves 
# the functionality of a function without changing its original code
def addTwo(n1,n2):
    return n1+n2

def my_deco(fun):
    def wrapper(a,b,c):
        r = fun(a,b)
        sum = r+c
        return sum
    
    return wrapper
@my_deco
def addTwo(n1,n2):
    return n1+n2

# addTwo = my_deco(addTwo)
sum = addTwo(10,20,30)
print(sum)
