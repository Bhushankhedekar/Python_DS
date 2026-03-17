# List datatypes
# List is a collection which is ordered and changeable. Allows duplicate members.
# List is written with square [] brackets and seperated by commas (,).
# List is a hetrogeneous data type which means it can contain different types of data.
# List is a mutable data type which means we can change the value of list after it is created.
# List is a collection of items which are separated by commas and enclosed in square brackets.  
# We can fetch data using indexing and slicing.
# example of list

# l1 = [1, "Hello", 2.5, 10+20j, True, [1, 2, 3], {"name": "John", "age": 30}, (1, 2, 3, 3, 3, 3), {1, 2, 3}]
l1 = [1,2,3,4,5,6,7,8,9]
print(l1)

# Methods to add element in list 
# 1. append() : adds an element at the end of the list
# only one element can be added at a time using append() method
# l1.append("World")
# print(l1)

# 2. insert() : adds an element at the specified position
l1.insert(-2, "Python")
print(l1)

# 3. extend() : adds the elements of a list (or any iterable), to the end of the current list
# l2 = [1, 2, 3]
# l1.extend(l2)
# print(l1)
