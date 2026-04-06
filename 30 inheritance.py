# OOP Pillrers
# 1.Inheritance
# 2.Encapsulation
# 3.Polymorphism
# 4.Abstaction

# 1.Inheritance
# inheritance is the process of acquiring the properties 
# and behaviour of parent class by child class.
# Ex.
# class Parent:
#     def m1(self):
#         print('this is m1 method of parent class')

# class Child(Parent):
#     def m2(self):
#         print("this is m2 method of child class")
#         c1 = Child()
#         c1.m1()

# types of inheritance
# 1 simple/single 
# in this inheritance there is only one parent class and one child class
# class Parent:
#     def m1(self):
#         property = ["cash", "car", "house"]
#         print(property)

# class Child(Parent):
#     def m2(self):
#         prop = ["bike", "cash"]
#         print(prop)

# # jay = Child()
# # jay.m1()
# # jay.m2()

# jay = Parent()
# jay.m1()
# # jay.m2()


# 2 multilevel
# multilevel inheritance is the process of acquiring the properties 
# and behaviour of parent class by child class and then child class
# becomes parent class for another child class
class Parent:
    def m1(self):
        property = ["cash", "car", "house"]
        print(property)

class Child(Parent):
    def m2(self):
        prop = ["bike", "cash"]
        print(prop)

class GrandChild(Child):
    def m3(self):
        prop = ["cycle", "cash"]
        print(prop)
gc = GrandChild()
gc.m1()
gc.m2()
gc.m3()


# 3 hierarchical
# hierarchical inheritance is the process of acquiring the properties
# and behaviour of parent class by more than instance of child class
# one parent and multiple childs of inheritance 
class Parent:
    def m1(self):
        Property = ["cash", "car", "house"]
        print(Property)

class Child1(Parent):
    def m2(self):
        Prop = ["bike", "cash"]
        print(Prop)

class Child2(Parent):
    def m3(self):
        Prop2 = ["cycle", "cash"]
        print(Prop2) 

c1 = Child1()
c1.m1()
c1.m2()

c2 = Child2()
c2.m1()
c2.m3()


# 4 multiple
# multiple inheritance is the process of acquiring the properties 
# and behaviour of more than one parent class by child class
# method resolution order (MRO) is the order in which the methods are called in multiple inheritance
class Parent1:
    def m1(self):
        Property = ["Cash", "car", "bike"]
        print(Property)

class Parent2:
    def m2(self):
        Prop = ["cycle", "cash"]
        print(Prop)

class Child(Parent1, Parent2):
    def m3(self):
        Prop2 = ["House", "cash"]
        print(Prop2)

c = Child()
c.m1()
c.m2()
c.m3()

# print(Child.__mro__())
# print(Parent1.__mro__())

# 5 hybrid
# hybrid inheritance is the process of acquiring the properties 
# and behaviour of more than one parent class by child class and 
# then child class becomes parent class for another child class
class Parent1:
    def m1(self):
        Property = ["cash", "car", "bike"]
        print(Property)

class Parent2:
    def m2(self):
        Prop = ["cycle", "cash"]
        print(Prop)

class Child1(Parent1, Parent2):
    def m3(self):
        Prop2 = ["House", "cash"]
        print(Prop2)

class Child2(Child1):
    def m4(self):
        Prop3 = ["Land", "cash"]
        print(Prop3)

c2 = Child2()
c2.m1()
c2.m2()
c2.m3()
c2.m4()


# 6 cyclic
# cyclic inheritance is the process of acquiring 
# the properties of parent class by child class and then 
# child class becomes parnet class for another child class and 
# then child class becomes parent class for first child class
# class Parent1:
#     def m1(self):
#         Property = ["cash", "car", "bike"]
#         print(Property)

# class Parent2(Parent1):
#     def m2(self):
#         Prop = ["cycle", "cash"]
#         print(Prop)

# class Child(Parent2):
#     def m3(self):
#         Prop2 = ["house", "cash"]
#         print(Prop2)

# c = Child()
# c.m1()
# c.m2()
# c.m3()
