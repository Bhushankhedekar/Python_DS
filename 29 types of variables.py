# Types of variables
# 1. Instance variables
# 2. class/Static variables
# 3. Local variables

# 1. Instance variables
# This variables are written with self keyword
# shared copy per object is created
# class Student:
#     def __init__(self, r, n):
#         self.roll = r
#         self.naame = n
# s1 = Student(1, "ABC")

# 2. class/Static variables
# A variable which is declared inside class and outside constructor 
# is called class variable or static variable
# single copy is created and shared with all the objects of class
# it is used for memory saving purpose
# it is accessed by class name and object name both
# class name is recomended to access class variable 
# because it is shared with all the objects of class
# class Student:
#     college = "TKA"
#     def __init__(self, r, n):
#         self.roll = r
#         self.naame = n
# s2 = Student(2, "XYZ")
# print(s2.college)

# s2.college = "JBK"
# print(s2.college)

# Student.college = "Pune"
# print(Student.college)

# 3. Local variables
# Local variables is declared inside a method and used inside that method
# a local variable is used to hold the temporary data
# class Student:
#     def __init__(self, r, n):
#         self.roll = r
#         self.naame = n
#     def display(self):
#         a = 10
#         print("Local variable", a)

# Method
# Method is a function which is written inside a class
# we can pass parameters in method and it cam return some value also
# 1. instance method
# 2. class method
# 3. static method

# 1. instance method
# it is used to process instance variables and it is called by object name
# first parameter of instance method is self which is used to access the
# instance variables of class and it is used to differentiate 
# between local variable and instance variable
class Student:
    college = "TKA"
    def __init__(self, r, n):
        self.roll = r
        self.name = n

    def getRoll(self):
        return self.roll
    
    def getName(self,new):
        self.name = new

s3 = Student(3, "PQR")
print(s3.name)
print(s3.roll)

print(s3.getRoll())

print(s3.getName("Bhushan Khedekar"))
print(s3.name)

# import this


# 2. class method
# class method is used to process class variable and it is called by class name
# first parameter of class method is cls which is used to access the class variable of
# class and it is used to differentiate between local variable and class variable
# @classmethod decorator is used to declare a class method

class Student:
    college = "TKA"
    def __init__(self, r, n):
        self.roll = r
        self.name = n

    def getRoll(self):
        return self.roll
    print(Student.getRoll)

    @classmethod
    def getCollege(cls):
        return cls.college
    
    def getCollege2(self):
        return Student.college
    
s4 = Student(4, "LMN")
print(Student.getCollege())


# 3. static method
# static method is used to process the static/local variables and it is called by class name
# it is used to perform some action which is not related to instance variable and class variable
# @staticmethod decorator in used to declare a static method
class Student:
    college = "TKA"
    def __init__(self, r, n):
        self.roll = r
        self.name = n

    def getRoll(self):
        return self.roll
    print(Student.getRoll)

    @classmethod
    def getCollege(cls):
        return cls.college
    
    @staticmethod
    def getPercentage(m1,m2):
        per = 100*((m1+m2)/200)
        return per
s1 = Student(1,"Jay")
per = s1.getPercentage(80, 90)
print(per)


