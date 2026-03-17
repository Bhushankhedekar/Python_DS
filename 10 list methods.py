# List day 2

# List 
# -- collective datatype
# -- hectrogenious collection
# -- enclosed by [] sepratred by(,)
# -- order
# -- mutable
# -- allow Duplicates
# -- we can featch data using indexing and slicing
# -- sequence Datatype

l1 = []
# print(type(l1))

l2 = [10,20,30]
# print(l2)
# print(type(l2))

l3 = [10,20,10,10]
# print(l3)

# l4 = [10, 10.5, "Ritik", 10+20j, True ,[10,20,30],(1,2,3),{3,9,6,6,6},{1:1, 2:4}]

# print(l4)

# fetch "Ritik"
# print(l4[2])

# fetch {3,9,6}
# print(l4[-2][2])
# print(l4[-1][1])

# l5 = ["10","20","30"]

# Method to add element in list 
# 1. append
# 2. insert
# 3. extend 

# l5.append([100,200,"Name"])

# l5 = ["10","20","30"]

# l5.insert(2,[1000,2000])  # ['10', '20', 1000, '30']     # ['10', '20', [1000, 2000], '30']

# l5.extend([1000])   # ['10', '20', '30', 100, 200, 300]

# l5.insert(20, 300)

# print(l5)  

# print(l5[-1])


# l1 = [10,20,30,40]

# print(dir(l1))

# [  'reverse', 'sort']

# l1.clear()  # []

# l2 = l1.copy()
# print("l1 :  " , l1)
# print("l2 :  " ,l2)

# l3 = l1
# print("l3 :  " , l3)

# print(l1.count(10))  # 1

# print(l1.index(30))  # 2

# print(l1.index(300))   # ValueError: 300 is not in list

# print(l1.pop())  # 40

# print(l1.pop(2))  #  30

# print(l1.pop(-3))  #  20

# l1.remove(10)

# l1.remove(100) # ValueError: list.remove(x): x not in list
# print("before : ",  l1)

# l1.reverse() # [40, 30, 20, 10]

# print(reversed(l1))  # <list_reverseiterator object at 0x0000019F9BC942B0>

# print("use reversed class : ",list(reversed(l1))) # [40, 30, 20, 10]

# l2 = [1,2,3,5,1,6,4,9]
# print(sorted(l2))

# l2.sort()

# del l2[2]

# del l2 

# # print("after : ",l2)

# str1 = "RitIK"

# print(sorted(str1))

# print(list(reversed(str1)))


# l3 = []
# even_list = []
# even = 0
# for i in l2:
#     if i % 2 == 0 :
#       l3.append(i)
#       even = even + i
#       even_list.append(even)
# print(l3)
# print(even)
# print(even_list)

# 1
# 1+3 = 4
# 4 + 5 = 9 
# 9 + 7 = 16
 
# 16 + 9 = 25

# 25+11 = 36

list2 = [10, 20, 30, [40, 50, [60, 80, 90], 100, 110, 120], [112, 114, 116], 221, 226, 336]

# 1. Access First-Level Elements
print(list2[0])  # 10

# 2. What is the output of list2[0] and list2[3]?
print (list2[0])
print (list2[3])

# 3. Extract the list [40, 50, [60, 80, 90], 100, 110, 120] using indexing.
print(list2[3])

# 4. Retrieve 60, 80, and 90 from the nested list using indexing.
print(list2[5])

# 5. What is the output of list2[4][1]?
print(list2[4][1]) 

# 6. Write a statement to access the element 336.
print(list2[-1])

# 7. The last element (336).
print(list2[-1])

# 8. The second-to-last sub-list ([112, 114, 116]).
print(list2[-3])

# 9. Access 110 from the sub-list [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][4])

# 10. Retrieve the element 116 from the list [112, 114, 116].
print(list2[4][2])

# 11. Extract 40 from [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][0])	

# 12.	Write a slice to extract [30, [40, 50, [60, 80, 90], 100, 110, 120]].	
print(list2[2:4])

# 13.	Extract [100, 110, 120] from the nested sub-list [40, 50, [60, 80, 90], 100, 110, 120].
print(list2[3][3:6])	

# 14.	Write a slice to reverse the entire list2.	
print(list2[::-1])

# 15.	Reverse the list [112, 114, 116].
print(list2[4][::-1])

# 16.	Write a slice to get [60, 80, 90].
print(list2[3][2])

# 17.	From the main list, extract [10, 30, [112, 114, 116]] using slicing.
print(list2[0:3])
print(list2[4])

# 18.	Slice to extract [221, 226, 336] from the main list.
print(list2[5:])    

# 19.	Write a slice to extract [40, 50, [60, 80, 90]].
print(list2[3][0:3])

# 20.	Write a slice to get [10, 30, [112, 114, 116], 226].
print(list2[0:3])
print(list2[4])


list2[-1 : -4] 

list2[5 : 1]


# 						## List Method Practical ##

# 1. Create an empty list and use append() to add five different numbers to it. Print the final list.
list1 = []
list1.append(10)    
list1.append(20)
list1.append(30)
list1.append(40)
list1.append(50)
print(list1)

# 2. Create a list of student name  and append a new Student name  and print the length of list .
list2 = ["Ritik", "Rahul", "Rohit", "Ramesh"]
list2.append("Suresh")
print(len(list2))

# 3. Append a list [10, 20, 30] to another list and observe the result.
list3 = [1, 2, 3]
list3.append([10, 20, 30])
print(list3)

# 4. Create a list and make a copy using copy().
list4 = [1, 2, 3, 4, 5]
list5 = list4.copy()
print("list4 : ", list4)
print("list5 : ", list5)

# 5. Create a list with at least 10 elements, use clear(), and check the length of the list afterward.
list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list6.clear()
print(len(list6))

# 6. Create a nested list and clear only the inner list while keeping the outer list intact .
list7 = [1, 2, [3, 4, 5], 6, 7]
list7[2].clear()    

# 7. Given nums = [1, 2, 3, 4, 2, 2, 5, 2], find how many times 2 appears in the list.
list8 = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = list8.count(2)
print(count_2)

# 8. Create a list of words and find how many times a particular word appears.
list9 = ["apple", "banana", "cherry", "banana", "grape"]
word_count = list9.count("banana")  
print(word_count)

# 9. Create two lists, list1 in integer variable  and list2 in String variable. Use extend() to add elements of list2 to list1. Print the final result.
list1 = [1, 2, 3]
list2 = ["apple", "banana", "cherry"]
list1.extend(list2)
print(list1)

# 10. Given fruits = ['apple', 'banana', 'cherry', 'banana', 'grape'], find the index of banana.
list10 = ['apple', 'banana', 'cherry', 'banana', 'grape']
index_banana = list10.index("banana")
print(index_banana)

# 11. Insert the number 100 at the beginning of the list [10, 20, 30].
list11 = [10, 20, 30]
list11.insert(0, 100)
print(list11)

# 12. Insert 'Python' at index 2 in a list of programming languages and print the result.
list12 = ["Java", "C++", "JavaScript"]
list12.insert(2, "Python")
print(list12)

# 13. Given numbers = [5, 10, 15, 20, 25], remove and print the last element using pop().
numbers = [5, 10, 15, 20, 25]
last_element = numbers.pop()
print("Removed element:", last_element)
print("Updated list:", numbers)

# 14. Remove an element at index 2 and print both the removed element and the updated list.
numbers = [5, 10, 15, 20, 25]
remove_element = numbers.pop(2)
print("Removed element:", remove_element)
print("Updated list:", numbers)

# 15. Given colors = ['red', 'blue', 'green', 'blue', 'yellow'], remove the first occurrence of 'blue'.
colors = ['red', 'blue', 'green', 'blue', 'yellow']
colors.remove('blue')
print(colors)

# 16. Reverse the list [1, 4, 9, 16, 25] and print the result.
list16 = [1, 4, 9, 16, 25]
list16.reverse()
print(list16)

# 17. Reverse a list of words and join them to form a sentence words = ["Hello", "world", "Python"].
list17 = ["Hello", "world", "Python"]
print(" ".join(reversed(list17)))

# 18. Sort a list of numbers [10, 5, 8, 3, 1] in ascending and then in descending order.
list18 = [10, 5, 8, 3, 1]
list18.sort()
print("Ascending order:", list18)
list18.sort(reverse=True)  
print("Descending order:", list18)
list18.sort(reverse=False)
