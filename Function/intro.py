'''

function - it is a block of code which executes a certain task only when it is called.
Synyax : 
def function_name(parameter):    # variable assigned during function definition
    # block of code
    return expression           # return - it ends the function execution and returns
                                    a value to the function
function_name(argument)         # value assigned during function call 
use of function:
reusability of code.
to maintain proper sturcture.
2 types of function 
1. user defined function - function created by user
2. inbuilt function - predefined function 
    examples : print() , len() , input() 
    
4 types of user defined function
1. non-parameterized non-return type.
2. parameterized non-return type.
3. non-parameterized return type.
4. parameterized return type.

'''

'''1. non-parameterized non-return type.

syntax :

def Function_name():
block of code

function_name()
'''

# 1. write a function to display hello world.
def display():
    print("Hello World !")
display()
print()
# 2. Write a function to print your name.
def display():
    print("Vaishnavi Agrawal")
display()
print()
# 3. Write a function to print numbers from 1 to 10.
def display():
    for i in range(1,11):
        print(i,end=" ")
display()
print()

# 4. Write a function to print all even numbers from 1 to 20.
def display():
    for i in range(1,21):
        if(i%2==0):
            print(i,end=" ")
display()
print()

# 5. Write a function to print the first 5 odd numbers.
def display():
    for i in range(1,10):
        if(i%2!=0):
            print(i,end=" ")
display()
print()

'''2. parameterized non-return type.

syntax :

def Function_name(argument):
block of code

function_name()
'''

# 1. Write a function that takes a name as a parameter and prints "Hello <name>".
def display(name):
    print(f"Hello {name} !")

display(input("enter name "))
print()
# 2. Write a function that takes a number as a parameter and prints whether it is even or odd.
def display(n):
        if(n%2==0):
            print("num is even ")
        else:
             print("num is odd")

display(int(input("enter num ")))
print()

# 3. Write a function that takes two numbers as parameters and prints their sum.
def display(n,m):
        print("sum = ",n+m)
display(int(input("enter num ")),int(input("enter num ")))
print()

# 4. Write a function that takes a string as a parameter and prints its length.
def display(str):
        print("len of string is : ",len(str))
display(input("enter String "))
print()

# 5. Write a function that takes a number n as a parameter and prints the first n natural numbers.
def display(n):
     i=1
     while(i<n+1):
          print(i,end=" ")
          i+=1
display(int(input("enter num ")))
print()

#6 sqare of all even numbers in a given list

def sqr_of_even_num(lst):
     for i in lst:
            if i%2==0:
                 print(i**2,end=" ")

num_lst=[1,2,3,4,5,6,7,8,9]
sqr_of_even_num(num_lst)
print()


#7 Write  function to display frequency count of an element in given list

def freq_count(lst):
     cnt=0
     for fruit in lst:
          if(fruit =="apple"):
               cnt+=1
     print(f"apple is repeating {cnt} time !")

fruits=["apple","apple","mango","apple"]
freq_count(fruits)
print()

#8 write a funtion to display freq count of letter in given string

def freq_cnt_of_letter(s,l):
     cnt=0
     for i in s:
          if(i==l):
               cnt+=1
     print(f"freq of {l} is {cnt}")
s="i love python"
freq_cnt_of_letter(s,input("enter letter "))
print()


# 1.      Write a function that accepts a number and prints its factorial.
def factorial(n):
     ans=1
     for i in range(1,n+1):
            ans*=i
     print(f"factorial of {n} is {ans}")
factorial(int(input("enter num ")))

# 2.      Write a function that accepts a string and prints its reverse.
def reverse_of_str(s):
     
     ans=s[::-1]
     print(f"reversed string {ans}")

reverse_of_str(input("enter String "))


# 3.      Write a function that takes a number and prints whether it is even or odd.
def even_odd(n):
        if(n%2==0):
            print("num is even ")
        else:
             print("num is odd")

even_odd(int(input("enter num ")))
print()


# 4.      Write a function that takes a list of numbers and prints only the even ones.
def even_num(lst):
     for i in lst:
            if i%2==0:
                 print(i,end=" ")

num_lst=[1,2,3,4,5,6,7,8,9]
even_num(num_lst)
print()

# 5.      Write a function that accepts a number and prints its multiplication table.
def num_multiplication(n):
     ans=1
     for i in range(1,11):
            print(f"{n} X {i} = {n*i}")
num_multiplication(int(input("enter num ")))


# 1. Write a function that returns your name.
# 2. Write a function which returns addition of two numbers
# 3. Write a function that returns the sum of numbers from 1 to 10.

# 1.      Write a function that takes two numbers and returns their sum.
# 2.      Write a function that accepts two numbers and returns the greater number.
# 3.      Write a function that takes a string and returns its length.
# 4.      Write a function that takes a number and returns whether it is even or odd.
# Write a function that accepts two numbers and returns their product.
# 4. parameterized return type. 
# syntax : 
# def function_name(parameter):
#     # block of code
#     return expression
    
# var_name = function_name(argument)
# print(var_name)
# def function_name():
#     # block of code
#     return expression
    
# var_name = function_name()
# print(var_name)