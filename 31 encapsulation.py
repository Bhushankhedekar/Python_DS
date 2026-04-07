# Encapsulation
# Encapsulation is the process of hiding the
# data and behaviour of a class from outside world.
# binding data and behaviour together is called encapsulation.
# we can acheive encapsulation by making all attributes private 
# and providing public getter and setter methods to access and 
# modify the private attributes. 
# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def display(self):
#         return self.__age,self.__name
    
#     def getAge(self):
#         return self.__age

#     def getName(self):
#         return self.__name
    
#     def setAge(self):
#         self.__age = self.setAge
    
#     def setName(self):
#         self.__name = self.setName

# s1 = Student("Kiran", 20)
# # print(s1.display())


# print(s1.getAge())
# print(s1.getName())

# # print(s1.setAge(20))
# # print(s1.setName("Nayan"))
# # print(s1.display())

# 
# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def getAge(self,pin):
#         if pin == 1234:
#             return self.__age
#         else:
#             return 0
        
#     def getName(self):
#         return self.__name
    
#     def setAge(self,na):
#         self.__age = na

#     def setName(self,na):
#         self.__name = na

# s1 = Student("Kiran", 20)
# print(s1.getAge(1234))
# print(s1.getName())

# print(s1.setAge(100))
# print(s1.getAge(1234))

class Player:
    def __init__(self, jn, name, runs, wickets, tname):
        self.__jn = jn
        self.__name = name
        self.__runs = runs
        self.__wickets = wickets
        self.__tname = tname

    def getJN(self):
        return self.__jn
    
    def getName(self):
        return self.__name
    
    def getRuns(self):
        return self.__runs
    
    def getWickets(self):
        return self.__wickets
    
    def getTname(self):
        return self.__tname
    
    # def setJN(self, jn):
    #     self.__jn = jn

    # def setName(self, name):
    #     self.__name = name

    # def setRuns(self, runs):
    #     self.__runs = runs

    # def setWickets(self, wickets):
    #     self.__wickets = wickets

    # def setTname(self, tname):
    #     self.__tname = tname

p1 = Player(7, "Virat Kolhi", 12000, 200, "India")
print(p1.getJN())
print(p1.getName())
print(p1.getRuns())
print(p1.getWickets())
print(p1.getTname())