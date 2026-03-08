'''

exception handling
exception it is an event which occurs during program execution, and disrupts the normal flow of execution.
this event is handled by exception handling which avoids the exception and ensures that program runs smoothly

Syntax :
try:
   #code which may raise an error
except:
   #which handles exception - (error message)

'''

# x=24
# print(x)

# print(a)

# print(x)

x=25
print(x)

try:
    print(a)
except:
    print("Error")

print(x)

print()

# causes zero division error
try:
    div = 19/0
    print(div)
except:
    print("Cannot divide by zero.")

# inbuilt exceptions

try:
    n=int(input("enter numerator: "))
    d= int(input("enter denominator : "))
    div = n/d

except ZeroDivisionError as ze:
    print("error : ",ze)

try:
    y = 78
    print(a)
except NameError as ne:
    print("Error: ",ne)


print("------value error--------")
try:
    value = int(input("Enter a number: "))
    print (value)
except ValueError as ve:
    print("Error: ",ve)
I
print("-----index error-------")
lst = [20,30,40,50]
try:
    index = int(input("Enter an index : "))
    print(lst[index])
except IndexError as ie:
    print("Error: ",ie)

#when eror is not known.

try:
    div = 19/0
    print(div)
except Exception as e:
    print("Error : ",e)


data=[20,30,40,50,60]
try:
    index=int(input("enter an index : "))
    print(data[index])
except IndexError as ie:
    print("error: ",ie)
except ValueError as ve:
    print("error: ",ve)
except NameError as ne:
    print("error: ",ne)
    