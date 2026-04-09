# Polymorphism
# Poly means many and morphism means forms. 
# So polymorphism means many forms. 
# In OOP, polymorphism is the ability of an object to take on many forms.
#  It allows us to use a single interface to represent different types of objects.

# class Book:
#     def __init__(self,title,price):
#         self.title = title
#         self.price = price

#     def __init__(self,title):
#         self.title = title

#     def __init__(self,price):
#         self.price = price

#     def m1(self):
#         print(000)

#     def m1(self,n1):
#         print(111,n1)
        
# # b1 = Book("Python", 500)
# # print(b1)
# b2 = Book("Python")
# print(b2)
# b3 = Book(500)
# print(b3)

class Parent:
    def Property(self):
        print(["Gold", "Land", "House"])

    def marry(self):
        print("Girl A")

class Child(Parent):
    def Property2(self):
        print(["Bike", "Car"])

    def marry(self):
        print("Girl B")

c1 = Child()
c1.Property()
c1.Property2()
c1.marry()
