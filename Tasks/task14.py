# Create a class Arithmetic having a constructor for variables and 3 functions

class Arithmetic:
    def __init__(self,a,b):
        self.var1=a
        self.var2=b
    def Addition(self):
        total=self.var1+self.var2
        print("Addition of a and b is : ",total)
    def Subtraction(self):
        total=self.var1-self.var2
        print("subtraction of a and b is : ",total)
    def Division(self):
        total=self.var1//self.var2
        print("division  of a and b is : ",total)

obj1=Arithmetic(8,4)
obj1.Addition()
obj1.Subtraction()
obj1.Division()


# for add,sub,div and create 2 objects of a class Arithmetic.



# Write a Python program to create a class Book.

# Requirements:

# - Data members: title, author, price

# - Method accept() → take values from user

# - Method display() → print book details

# - Create object and call methods

class Book:

    def __init__(self):
        self.title=""
        self.author=""
        self.price=0
    def Accept(self):
        title=input("enter the title of book")
        author=input("enter the author of book")
        price=int(input("enter the price"))
        
    def Display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)


obj1 = Book()
obj1.Accept()
obj1.Display()



 
'''
Write a Python program to create a class Rectangle.

Requirements:

- Constructor should take length and width

- Method area() → returns area

- Method perimeter() → returns perimeter

- Create object and print area and perimeter

'''
class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length*self.width

    def Perimeter(self):
        return 2*(self.length+self.width)

obj1 = Rectangle(22,33)
print("Area of rectangle:", obj1.Area())
print("Perimeter of rectangle:", obj1.Perimeter())





