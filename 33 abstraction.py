# Abstraction
# Abstraction is the process of hiding the implementation 
# details and showing only the functionality to the user. 
# It helps to reduce complexity and allows the programmer 
# to focus on interactions at a higher level.
# NON abstract class / concrete class
# @abstractmethod is used to declare a method as abstract method.
from abc import ABC, abstractmethod
class Demo(ABC):
    def m1(self):
        print(111)

    @abstractmethod
    def m2(self,a,b):
        pass

class Example(Demo):
    def m2(self, a):
        print(a)

e = Example()
e.m1()
e.m2(222)

# Interface is a collection of abstract methods.
