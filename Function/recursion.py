'''
recursion - it is a technique where a function calls itself to do a task

def func(parameter):
    if():
      return value
    else:
      return func(modified parameter)

'''

#factorial of a number using recursion

def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

#sum of digits

def sumDigits(n):
    if n==0:
        return 0
    else:
        return n%10+sumDigits(n//10)

print(sumDigits(123))

#nested function
#to calculate area of shapes

def areaOfShapes():
    print("this func displays area of circle and rectangle")

    def AreaOfCircle(r):
        print("area of circle = ",3.14*r*r)

    def AreaOfRec(l,b):
        print("area of rec = ",l*b)
    AreaOfCircle(5)
    AreaOfRec(9,8)

areaOfShapes()