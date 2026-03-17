# string is a datatype in Python used to represent text data.
# anything we write inside '',"",''' ''' is considered as string
# ''' ''' used to represent multi line string


# String formatting in Python
# 1. by using .format method
# 2 by using f" " way
# 3 older way %s

# 1. by using .format method
# name = eval(input("Enter name:"))
# rollno = eval(input("Enter roll no:"))
# marks = eval(input("Enter marks:"))
# s1= "student name is {} and roll number is {} and marks is {}".format(name,rollno,marks)
# print(s1)

# s2 = "student name is {v1} and roll number is {v2} and marks is {v3}".format(v1="xyz",v2=2,v3=85)
# print(s2)

# 2 by using f" " way
# name = "abc"
# rollno = 3
# marks = 90
# s3 = f"Student name is {name} and roll number is {rollno} and marks is {marks}"
# print(s3)

# s4 = f"{name}~~{rollno}~~{marks}"
# print(s4)

# num1=10
# num2=20
# print(f"addition of {num1} and {num2} is {num1+num2}")

# 3 older way %s
# name = "pqr"
# rollno = 4
# marks = 95
# s5 = "Student name is %s and roll number is %d and marks are %d"%(name,rollno,marks)
# print(s5)



#  Homework : displaying the roll,name and marks in tabular format 
# students = [
#     {"roll": 1, "name": "abc", "marks": 70},
#     {"roll": 2, "name": "xyz", "marks": 80}
# ]

# print("-" * 45)
# print(f"| {'roll':^10} | {'name':^15} | {'marks':^10} |")  
# # ^: This symbol tells Python to center the text.
# print("-" * 45)

# for s in students:
#     print(f"| {s['roll']:^10} | {s['name']:^15} | {s['marks']:^10} |")

