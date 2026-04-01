# Self
# self is a reference variable which refers to the current object of the class
# it is used to access the attributes and methods of the class
# it is used to differentiate between the local variable and the instance variable
# it is used to call the constructor of the class
class Student:
    def __init__(self, r, n):
        print("Inside class", id(self))
        self.roll = r
        self.name = n

s1 = Student(n = "ABC", r = 5)
print("From outside of class", id(s1))

s2 = Student(7, "XYZ")
print("From outside of class", id(s2))

s3 = s2
print(id(s3))