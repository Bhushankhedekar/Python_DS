# Arguments
# arguments are the data /valuew pass to the function
# Types
# 1.positional arguments
# 2.keyword
# 3.default
# 4.arbitary(variable length args)
    # a.positional
    # b.keyword

# parameters 
# parameters are the type of data that has to be pass

# 1.positional arguments
# def subTwo(n1, n2):
#     return n1 - n2

# a = 10
# b = 20
# result1 = subTwo(a, b) 
# result2 = subTwo(b, a)  
# print(result1)
# print(result2)

# print(subTwo(a, b))   

# 2.keyword
# def subTwo(n1, n2):
#     return n1 - n2

# a = 10
# b = 20
# r1 = subTwo(n2 = a, n1 = b) 
# r2 = subTwo(n1 = a, n2 = b) 
# print(r1)
# print(r2) 

# # 3.default
# # Default arguments must be at last in function defination
# def remp(eid,enm,sal,dept,c_name="TCS"):
#     # here "TCS" is default argument
#     print(eid,enm,sal,dept,c_name)

# remp(101,"abc",20000,"QA")
# remp(101,"pqr",25000,"QA","HCL")

# 4.arbitary(variable length args)
    # a.positional
# def addTwo(*args):
#     print(args)
#     print()
#     return sum(args)  # Use built-in sum()

# print(addTwo(10, 20,30,40))  

    # b.keyword
def addition(**kwargs):
    print(kwargs,type(kwargs))
    print(kwargs.get(1))
    print(kwargs.keys())

addition(a=10, b=20, c=30)   