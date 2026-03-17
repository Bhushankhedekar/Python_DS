# List 
# fundamental data types are used to represent simple values such as numbers, characters, and boolean values.
# 1. int : used to represent whole numbers
# 2. float : used to represent decimal numbers
# 3. complex : used to represent complex numbers
# 4. bool : used to represent boolean values (True and False)
# 5. str : used to represent strings (sequence of characters)
#  all 5 fundamental data types are immutable (cannot be changed after they are created)

# collection data types are used to represent a collection of values such as lists, tuples, sets, and dictionaries.
# 1. list : used to represent a collection of values that are ordered and changeable
# 2. tuple : used to represent a collection of values that are ordered and unchangeable
# 3. set : used to represent a collection of values that are unordered and unindexed
# 4. dict : used to represent a collection of key-value pairs that are unordered and changeable


# Immutable data types are those that cannot be changed after they are created.
# when you perform any operation on an immutable data type, a new object is created in memory and the reference to that object is updated to point to the new object.

# Mutable data types are those that can be changed after they are created.
# when you perform any operation on a mutable data type, the same object is modified in memory and the reference to that object remains the same.

# p = 100.00
# print(type(p),p,id(p))

# p = 99.99
# print(type(p),p,id(p))

# s = "Bhushan"
# print(type(s),s,id(s))

# s = s+" Khedekar"
# print(type(s),s,id(s))

# what is list in python ?
# list is a collection of values that are ordered and changeable.
# List is mutable, meaning that you can change the values in a list after it is created.
# list is defined by using square brackets [] and the values are separated by commas. 
# list is mutable ,hetrogenious collection of elements where insertion order is preserved and duplicates are allowed.
# hetrogenious means that a list can contain elements of different data types.

# Q.how to create a list in python ?
# Q. how to add the data in list ?
my_list = [ ]
print(type(my_list),id(my_list))

my_list.append(10)
print(my_list,id(my_list))

my_list.append(-10)
print(my_list)

my_list.append(-10.5)
print(my_list)

my_list.append("abc")
print(my_list)

my_list.append(True)
print(my_list)

my_list.append(False)
print(my_list)

print(my_list)
print(my_list,id(my_list))

# Q.how to access the data from list?
# print(my_list[0])  # Access first element

# my_list[0]= 20 

# print(my_list[0])  # Access modified first element

# print(my_list[-1])  # Access last element

# print(my_list[2])  # Access third element

# print(my_list.__len__())

# what this following code does
my_list[0]= my_list[0]+my_list[1]
# above code adds the first element of the list with the second element of the list and assigns the result to the first element of the list.
print(my_list)

my_list[0] = "abcd"
my_list[1] = 100
print(my_list)