# Lambda function
# Compresehension

# Lambda function
# Lambda is an anonimous function in python
# no need of def keyword to use 
# it is a one line function 
# there is a no need  of return statement in lambda 
# we can write expression in lambda function

# f1 = lambda a,b : a+b
# print((lambda a,b:a+b)(10,20))
# print((lambda a,b:a-b)(10,20))
# print((lambda a,b:a*b)(10,20))
# print((lambda a:a*a)(10))
# print((f1)(10,20))

# # greater or not
# f2 = lambda num1,num2 : num1 if num1>num2 else num2 
# print(f2(45,-90))

# # even or odd
# f3 = lambda num : "Even" if num % 2 == 0  else "Odd" 
# print(f3(4))

# # square list
# l = [10,12,45,65,89,23,44,12,23]

# square_list = list(map(lambda num : num**2,l))
# print("Original list:",l)
# print("Square list:",square_list)

# even list
# l = [10,12,45,65,89,23,44,12,23]

# even_list = list(filter(lambda num : "Even" if num%2==0 else "Odd",l))
# print("Original list:",l)
# print("Even list:",even_list)

# # uppercase list
# names = ['rohan','mahesh','karan','jivan']

# upper_list = list(map(lambda names : names.upper() , names))
# print(upper_list)

# # marks more than 75
# names = [('rohan',89),('mahesh',88),('karan',74),('jivan',70)]

# filtered_list = list(filter(lambda x: x[1] < 75, names))

# print(filtered_list)

# filter even numbers and square list

l = [10,12,45,65,89,23,44,12,23]

# filter_even = list(filter(lambda num: num % 2 == 0, l))
filter_square = list(map(lambda num : num **2,filter(lambda num: num % 2 == 0,l)))
print("Original list:",l)
# print("filter even list:",filter_even)
print("filter square list:",filter_square)






# Compresehension