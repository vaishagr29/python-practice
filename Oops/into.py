# Object Oriented Programming

# its a programming structure which uses classes and objects

# # focuses on structure

# OOPs principles : 

# 1. class

# 2. object

# 3. Encapsulation

# 4. Inheritance

# 5. Polymorphism

# 6. Abstraction

# 1. class - blueprint/template of an object

#     it is collection of data members and member functions

# 2. object - instance of a class




# create a class
class Myclass:
    x=7

#create an object
obj = Myclass()
print(obj.x)

'''
Syntax :
class classname:
#constructor - function which is called when an object is created.
#use - to declare instance variables
def __init__(self):
    # data members/instnace variables /attributes

# member functions/instance methods/methods
def function_name(self):
   # code

# create an object
obj = classname() -> constructor is called here

#self parameter - this defines intance variables, and also used to access data members and member functions through out class.


'''


# Create a class to calculate area of circle

class Area0fCircle:
    def __init__(self):
        self.radius = 5
    # data member
    # member function
    def AOC(self):
        print("Area of circle",3.14*self.radius*self.radius)

aoc= Area0fCircle()
aoc.AOC()

# parameterized constructor

class AreaOfCircle:
    def __init__(self, r):
        self.radius = r

    def AOC(self):
        print("Area of circle:", 3.14 * self.radius * self.radius)


aoc1 = AreaOfCircle(10)
aoc1.AOC()

aoc2 = AreaOfCircle(6)
aoc2.AOC()

# create a class students for students information

class Students:
    #constructor
    def __init__(self,name,age,marks1,marks2):
        self.s_name=name
        self.s_age=age
        self.s_marks1=marks1
        self.s_marks2=marks2

    def displayInfo(self):
        print("student name : ", self.s_name)
        print("student age: ", self.s_age)
        print("student mark1: ", self.s_marks1)
        print("student mark2: ", self.s_marks2)

    def total_marks(self):
        total = self.s_marks1 + self.s_marks2
        print("total marks = ",total)
        
s1=Students("Deepti",21,78,91)
print("---------Student-1 details ad bellow")
s1.displayInfo()
s1.total_marks()

s2 = Students("Vaish",23,95,98)
print("---------Student-2 details ad bellow")
s2.displayInfo()
s2.total_marks()

class Employee:
    def __init__(self):
        self.emp_name=""
        self.emp_id=0
        self.emp_rating=0.0

    def AcceptData(self):
        self.emp_name=input("enter emp name ")
        self.emp_id=int(input("enter emp id "))
        self.emp_rating=int(input("enter emp rating out of 10 "))

    def DisplayData(self):
        print("emp name :",self.emp_name)
        print("emp id :",self.emp_id)
        print("emp rating out of 10 :",self.emp_rating)

e1 = Employee()
print("---------Enter Emplyee details below---------")
e1.AcceptData()
print("----------Employee Details is shown below:-----")
e1.DisplayData()

