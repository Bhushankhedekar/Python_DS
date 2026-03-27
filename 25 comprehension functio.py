# sorted function
# Zip function
# comprehension function

# sorted function
# sorted function is used to sort the collective data types(list,dict,string etc)
# l1 = [23, 44 ,65, 98, 90, 23, 34, 64, 21, 12]
# # sorted_list = sorted(l,reverse = False)
# sorted_list = sorted(l,reverse = True)
# sorted_list = sorted(l,key = None, reverse = False)


# names = {'jivan': 70, 'karan': 74, 'mahesh': 88, 'rohan': 89}
# sorted_names = sorted(names.items(),key = lambda x:x[1],reverse = False)
# print(sorted_names)

# sorted_dict = dict(sorted_names)
# print(sorted_dict)

# roll = [1, 2, 3, 4, 5, 6]
# names = ['a', 'b', 'c', 'd', 'e','f']


# Zip function
# zip_sort =  dict(zip(roll,names))
# print(zip_sort)

# zip_sort =  list(zip(roll,names))
# print(zip_sort)

# zip_sort =  tuple(zip(roll,names))
# print(zip_sort)

# l2 = ["karna","rohan","mahesh","jivan"]
# sorted_l2 = sorted(l2,key = lambda x: len(x),reverse = True)
# print(sorted_l2)

# sorted_l2 = sorted(l2,key = lambda x:x [3],reverse = True)
# print(sorted_l2)


# comprehension function
# 1.List comprehension
# l = [10,12,45,65,89,23,44,12,23]

# square_list = list(map(lambda num : num**2,l))
# print("Original list:",l)
# print("Square list:",square_list)

# # print square of numbers
# square_list = [i*i for i in l]
# print("Square list using comprehension:",square_list)

# # print odd numbers from list
# square_list = [i for i in l if i %2 == 1]
# print("odd list using comprehension:",square_list)

# print even at even place
# even_list = ["Even" if i %2 ==0 else i for i in l]
# print(even_list)

# 2.Dictionary comprehension
# d = {1:1, 2:3, 5:6, 6:8}
# cube_list = {i:(i**3)for i in d}
# print(cube_list)

l = [[10,12],[45,65],[89,23,44],[12,23]]

flat_list = [num for sublist in l for num in sublist]

print(flat_list)

# Homework
# l1 = [1,2]
# l2 = ["a","b"]
#result = [(1,"a"),(1,"b"),(2,"a"),(2,"b")]


l1 = [1,2]
l2 = ["a","b"]

result = {(i, j) for i in l1 for j in l2}
print(result)

# l1 = [1,2]
# l2 = ["a","b"]

# result = [(i, j) for i in l1 for j in l2]

# print(result)