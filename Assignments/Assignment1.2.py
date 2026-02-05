#1.Take your name as input and print:
#	o/p - Hello, <name>! Welcome to Python.
name = "Vaishnavi"
print("Hello,", name, "! Welcome to Python.")


#2.Take your age as input and print:
#	o/p - You are <age> years old. Next year, you will be <age+1>.
age = 21
print("You are", age, "years old. Next year, you will be", age+1)


#3.Take length and width as input and print:
#	o/p - The area of rectangle with length <length> and width <width> is <area>.
length = 10
width = 5
area = length * width
print("The area of rectangle with length", length, "and width", width, "is", area)


#4.Take radius as input and print:
#	o/p - The circumference of a circle with radius <r> is <2 * 3.14 * r>.
r = 7
print("The circumference of a circle with radius", r, "is", 2*3.14*r)


#5.Take first name and last name as input and print:
#	o/p - Your full name is <firstname lastname>.
fname = "Vaishnavi"
lname = "Agrawal"
print("Your full name is", fname, lname)


#6.Take principal, rate, and time as input and print:
#	o/p - Simple Interest for principal <P>, rate <R>% and time <T> years is <SI>.
P = 1000
R = 5
T = 2
SI = (P*R*T)/100
print("Simple Interest for principal", P, ", rate", R, "% and time", T, "years is", SI)


#7.Take Celsius as input and print:
#	o/p - <C>°C is equal to <F>°F.
#(Formula: F = (C*9/5) + 32)
C = 25
F = (C*9/5) + 32
print(C, "°C is equal to", F, "°F")


#8.Take marks in 5 subjects as input and print:
#	o/p - You scored <percentage>% in total.
m1,m2,m3,m4,m5 = 80,85,90,75,70
total = m1+m2+m3+m4+m5
percentage = total/5
print("You scored", percentage, "% in total")


#9.Take item name, quantity, and price per unit as input and print:
#	o/p - The total cost for <quantity> <itemname>(s) at Rs.<price> each is Rs.<total>.
itemname = "Pen"
quantity = 5
price = 10
total = quantity * price
print("The total cost for", quantity, itemname, "(s) at Rs.", price, "each is Rs.", total)


#10.Take a number as input and print:
#	o/p - The square of <n> is <n**2> and the cube is <n**3>.
n = 4
print("The square of", n, "is", n**2, "and the cube is", n**3)


#11.Take a number as a string input and convert it into an integer. Print its square.
num = "5"
n = int(num)
print(n*n)


#12.Take an integer input and convert it to float. Print both values.
x = 10
y = float(x)
print(x, y)


#13.Take a decimal number input and convert it into an integer. Print both values.
x = 12.5
y = int(x)
print(x, y)


#14.Take a number as input and convert it into a string. Print "The number is <num>" using f-string.
num = 25
num_str = str(num)
print("The number is", num_str)


#15.Take two numbers as string input. Convert them into integers and print their sum.
a = "10"
b = "20"
print(int(a) + int(b))


#16. Create a variable name with your name and print:
#My name is <name>
name = "Vaishnavi"
print("My name is", name)


#17. Store your age in a variable and print:
#I am <age> years old.
age = 21
print("I am", age, "years old")


#18. Store two numbers in variables a and b. Print their sum.
a = 10
b = 20
print(a+b)


#19. Store the value of π = 3.14159 in a variable and print:
#Value of π is 3.14159
pi = 3.14159
print("Value of π is", pi)


#20. Create a variable country with your country name and print:
#I live in <country>
country = "India"
print("I live in", country)


#21. Store two strings in variables and print them together as a sentence.
s1 = "I love"
s2 = " Python"
print(s1 + s2)


#22. Store marks of 3 subjects in variables and print the total.
m1,m2,m3 = 70,80,90
print(m1+m2+m3)


#23. Assign True to a variable and print its type using type().
x = True
print(type(x))


#24. Store a float number in a variable and print:
#The number is <value>.
num = 12.5
print("The number is", num)
