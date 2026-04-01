
# =========================
# CLASSES AND OBJECTS (1–5)
# =========================

# 1. Create a class Person with attributes name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 3. Add a method display() to print the object details.
    def display(self):
        print(self.name, self.age)

# 2. Create two objects
p1 = Person("Vaishnavi", 21)
p2 = Person("Aman", 22)

p1.display()
p2.display()

# 4. Update age
p1.age = 25

# 5. Delete attribute
del p1.age


# =========================
# CONSTRUCTOR & SELF (6–10)
# =========================

# 6. Student class
class Student:
    def __init__(self, name="Unknown", marks=0):
        self.name = name
        self.marks = marks

    # 7. Print using self
    def display(self):
        print(self.name, self.marks)

    # 10. Destructor
    def __del__(self):
        print("Student object deleted")

# 8. Multiple objects
s1 = Student("A", 90)
s2 = Student("B", 80)

s1.display()
s2.display()


# =========================
# INHERITANCE (11–15)
# =========================

# 11. Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal sound")

# 12. Child class
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)   # 14. super()

    def speak(self):            # override
        print("Bark")

    # 15. Call parent method
    def parentSpeak(self):
        super().speak()

# 13. Multiple inheritance
class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass


# =========================
# POLYMORPHISM (16–20)
# =========================

# 16. Method overloading (default params)
def add(a, b=0):
    return a + b

# 17. Operator overloading
class Num:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

# 18. Method overriding
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

# 19. Function with multiple objects
def func(obj):
    obj.show()

# 20. Shapes polymorphism
class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Rectangle:
    def area(self):
        return 4 * 6


# =========================
# ABSTRACTION (21–25)
# =========================

from abc import ABC, abstractmethod

# 21. Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# 22. Circle
class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

# 23. Rectangle
class Rectangle(Shape):
    def area(self):
        return 4 * 6

# 24. Shape() → ERROR (cannot instantiate)

# 25. Multiple abstract methods
class DemoAbstract(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def display(self):
        pass


# =========================
# ENCAPSULATION (26–30)
# =========================

# 26. Private attribute
class Bank:
    def __init__(self):
        self.__balance = 0

    # 27. Getter & Setter
    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

# 28. Protected example
class Parent:
    def __init__(self):
        self._x = 10

class Child(Parent):
    def show(self):
        print(self._x)

# 29. Public attribute
obj = Parent()
obj._x = 50

# 30. Name mangling
b = Bank()
b.set_balance(1000)
print(b._Bank__balance)


# =========================
# OPERATOR OVERLOADING (31–35)
# =========================

class Demo:
    def __init__(self, x):
        self.x = x

    # 31. +
    def __add__(self, other):
        return self.x + other.x

    # 32. *
    def __mul__(self, other):
        return self.x * other.x

    # 33. str()
    def __str__(self):
        return f"Value: {self.x}"

    # 34. ==
    def __eq__(self, other):
        return self.x == other.x

    # 35. len()
    def __len__(self):
        return self.x


# =========================
# METHODS (36–40)
# =========================

class Example:
    count = 0

    def __init__(self):
        Example.count += 1

    # 38. Instance method
    def update(self, val):
        self.val = val

    # 36. Static method
    @staticmethod
    def welcome():
        print("Welcome!")

    # 37. Class method
    @classmethod
    def getCount(cls):
        print(cls.count)

# 39. Call static
Example.welcome()

# 40. Call class method
obj = Example()
Example.getCount()
obj.getCount()

# Banking system
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


# Vehicle system
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass


# Employee system
class Employee:
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        return 50000

class Developer(Employee):
    def salary(self):
        return 40000
    
#Part 2: Interview Questions (15)
    
'''
1. A class is a blueprint that defines properties and behavior of objects.
   An object is an instance of a class that represents real-world entities.

2. self refers to the current instance of the class and is used to access variables and methods.
   It helps differentiate between instance variables and local variables.

3. A constructor (__init__) is automatically called when an object is created.
   It is used to initialize object attributes with given values.

4. Inheritance allows a class to acquire properties and methods from another class.
   For example, a Dog class inheriting from Animal can reuse its features.

5. Polymorphism allows the same method to behave differently for different objects.
   For example, area() works differently for Circle and Rectangle.

6. Encapsulation is the process of hiding data and restricting direct access.
   It is implemented using private variables and getter/setter methods.

7. Abstraction hides internal implementation and shows only essential features.
   It reduces complexity and improves code maintainability.

8. Access specifiers control the visibility of class members.
   Python uses public, protected (_), and private (__) conventions.

9. Instance methods work with object data and require an object to call.
   Static methods don’t use object data, and class methods work with class-level data.

10. Operator overloading allows redefining operators for user-defined objects.
    It is used to perform operations like +, *, == on objects.

11. Method overloading means same method name with different parameters.
    Method overriding means redefining a method in a child class.

12. Abstract classes cannot be instantiated directly.
    They must be inherited and implemented in a child class.

13. Python uses naming conventions for access control instead of strict enforcement.
    Private variables use name mangling (__var) and protected use _var.

14. Multiple inheritance means inheriting from multiple parent classes.
    Multilevel inheritance means a chain of inheritance (A → B → C).

15. OOP is used in real-world systems like banking or e-commerce.
    Classes like Account, User, and Transaction model real entities.
'''

# =========================
# PART 3: OUTPUTS
# =========================

'''
    1.
    Output:
    B init

    2.
    Output:
    5

    3.
    Output:
    10

    4.
    Output:
    78.5

    5.
    Output:
    XYZ

    6.
    Output:
    B

    7.
    Output:
    10

    8.
    Output:
    Static Method

    9.
    Output:
    2

    10.
    Output:
    Object A

'''