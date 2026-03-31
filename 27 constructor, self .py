# Constructor

# Constructor
# it is a special method which is used to initialize the object of class
# it is denoted by __init__() method
class Player:
    def __init__(self, jn, pn, run, tn, wk):
        self.jersey_no = jn
        self.p_name = pn
        self.runs = run
        self.team_name = tn
        self.wickets = wk

p1 = Player(18, "Virat Kohli", 75, "India", 2)
print(p1.jersey_no)
print(p1.p_name)
print(p1.runs)
print(p1.team_name)
print(p1.wickets)

p2 = Player(20, "Rohit Sharma", 56, "India", 3)
print(p2.jersey_no)
print(p2.p_name)
print(p2.runs)
print(p2.team_name)
print(p2.wickets)

p3 = Player(20, "rahul", 72, "India", 4)
print(p3.jersey_no)
print(p3.p_name)
print(p3.runs)
print(p3.team_name)
print(p3.wickets)

p4 = Player(7, "MS Dhoni", 45, "India", 1)
print(p4.jersey_no)
print(p4.p_name)
print(p4.runs)
print(p4.team_name)
print(p4.wickets)

p5 = Player(45, "Ravindra Jadeja", 34, "India", 4)
print(p5.jersey_no)
print(p5.p_name)
print(p5.runs)
print(p5.team_name)
print(p5.wickets)


# Homework
# 1.Difference betweeen method and function
# mthod: it is a function which is defined inside the class and it is used to perform some action on the object of class
# function: it is a block of code which is used to perform some action and it is

# 2.create 5 classes of your choice and write minimum 2 attributes and 1 method in each class
# 1 car
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
c1 = Car("Toyota","Camry")
print(c1.make)

# 2 bike
class Bike:
    def __init__(self,brand, type):
        self.brand = brand
        self.type = type
b1 = Bike("Honda", "Sport")

# 3 mobile
class Mobile:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
m1 = Mobile("Aple", "iphone 12")

# 4 laptop
class Laptop:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
l1 = Laptop("Dell", "XPS 13")

# 5 watch
class Watch:
    def __init__(self, brand, type):
        self.brand = brand
        self.type = type
w1 = Watch("Rolex", "Luxury")

# 3. create IPL 2026 11 players and their 1 team
# mi_team = []
# mi_team.append(p1)
class Player:
    def __init__(self, jn, pn, run, tn, wk):
        self.jersey_no = jn
        self.p_name = pn
        self.runs = run
        self.wickets = wk
        mi_team = []
        mi_team.append(self)

p1 = Player(18, "Virat Kohli", 75, "India", 2)
p2 = Player(20, "Rohit Sharma", 56, "India", 3)
p3 = Player(20, "rahul", 72, "India", 4)
p4 = Player(7, "MS Dhoni", 45, "India", 1)  
p5 = Player(45, "Ravindra Jadeja", 34, "India", 4)
p6 = Player(10, "Hardik Pandya", 50, "India", 2)
p7 = Player(9, "Jasprit Bumrah", 20, "India", 5)
p8 = Player(11, "Yuzvendra Chahal", 15, "India", 3)
p9 = Player(12, "Ravichandran Ashwin", 30, "India", 4)
p10 = Player(13, "Shikhar Dhawan", 40, "India", 1)
p11 = Player(14, "KL Rahul", 60, "India", 2) 
