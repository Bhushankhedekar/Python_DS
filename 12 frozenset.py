# Frozenset
# A frozenset is an immutable version of a set. 
# It is a built-in data type in Python that represents an unordered collection of unique elements. 
# Once a frozenset is created, its elements cannot be modified, added, or removed.
# frozenset is created by using the frozenset() function
s1 = frozenset([1, 2, 3, 4, 5])
print("Frozenset: ", s1)

# Range function
# The range() function is used to generate a sequence of numbers.
# The range() function takes three parameters: start, stop, and step.
# 1. start: The starting number of the sequence (inclusive). Default is 0.
# 2. stop: The ending number of the sequence (exclusive).
# 3. step: The difference between each number in the sequence. Default is 1.    
# range() function returns a range object which is an iterable.
# range() function is commonly used in for loops to iterate over a sequence of numbers.
# Example of range() function
for i in range(5):
    print(i)

# None function
# The None function is a built-in function in Python that represents the absence of a value or a null value.
# None is often used to indicate that a variable has no value or that a function does not return anything.
# Exmple 
def my_function():
    print("This function does not return anything.")    
result = my_function()
print("The result of the function is:", result)


# Iterate a tuple ,list and string using range function
t1 = (1, 2, 3, 4, 5)
for i in range(len(t1)):
    print(t1[i])

l1 = [1, 2, 3, 4, 5]
for i in range(len(l1)):
    print(l1[i])

s1 = "Hello World"
for i in range (len(s1)):
    print("Index:", i, "Element", s1[i])



# Dictionary level 0
# Dictionary of int and string
# A dictionary is a collection of key-value pairs. It is a built-in data type in Python that is used to store data in a structured way.
# A dictionary is created by using curly braces {} and key-value pairs are separated by a colon
# Example of dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print("Dictionary: ", my_dict)

# key function ()
print("Keys: ", list(my_dict.keys()))

# values function ()
print("Values: ", list(my_dict.values()))

# items function
print("Items: ", list(my_dict.items()))

# create a dictionary of a movies name ,year, casts names and genere and iteration over dictionary
movies = {
    "3 Idiots":{
        "year": 2009,
        "cast":["amir khan", "R. Madhavan", "sharman joshi ","kaeena kapoor"]
    },
    "Bahubali":{
        "year":2015,
        "cast":["prabhas", "rana daggubati", "anushka shetty", "tanabbaah"]
    },
    "Dangal":{
        "year":2016,
        "cast":["amir khan", "sakshi tanwar", "fatima", "sana shaikh", "sanya malhotra"]
    }
}
# for movie in movies:
#     print("Movie:", movies)
#     print("Year:",movies[movie]["year"])
#     print("Cast:",movies[movie]["cast"])
#     print()

# print(movies.keys())

# print(movies.values())

# print(movies.items())

# print(movies.get("3 Idiots"))

# for k,v in movies:
#     for n in v:
#         if n =="amir khan":
#             count = count + 1
#             for s in n:
#                 if s == "a":
#                     count = count + 1
#                     print(k)