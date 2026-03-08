'''
inheritance - accesing parent class properties in chhild class
reuse of structure / Building relation between classes

types :
single inherit.
multiple inherit.
multilevel inherit.
herarchical inherit.
hybrid inherit.

'''
'''
# single inheritance - one child class is inheriting properties of one parent class

p -> c
Parent class/ Base class
Child class/Derived class

'''

class Parent:
    def show_parent(self):
        print("This is parent class.")

# child class
class Child(Parent):
    def show_child(self):
        print("This is child class.")

c=Child()
c.show_parent()
c.show_child()


# claculate total salary of emplyee

class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    def displayInfo(self):
        print(f"Emp name : {self.name}, Emp salary : {self.salary}")

class BonusCalculation(Employee):
    #super() - it allows to access properties and parent class constructor in child class

    def __init__(self, name, salary, bonus_percent):
        super().__init__(name, salary)
        self.emp_bonus_percent = bonus_percent

    def total_salary(self):
        total = self.salary + (self.salary * self.emp_bonus_percent/100)
        print("Total salary : ",total)

# create object of child class

e1 = BonusCalculation("disha",45000,8)
#e1.displayInfo()
e1.total_salary()

