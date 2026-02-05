#check if a num is even or odd
n= int(input("enter num for q1:"))
if(n%2==0):
    print(f"{n} is even num.")
else:
    print(f"{n} is odd num.")

# check if a number is positive or negative

n= int(input("enter num for q2:"))
if(n>=0):
    print("num is positive")
else:
    print(" num is negative")

#check if given string is empty

s= str(input("enter a string for q3"))
if(s==""):
    print("string is empty")
else:
    print("not empty")

#check if a number is divisible by 5

n= int(input("enter num for q4"))

if(n%5==0):
    print("yes")
else:
    print("no")

# check if the first character of the string is vowel or consonent

s= str(input("enter string for q5"))
vowel="aeiouAEIOU"
if(s[0] in vowel):
    print("yes first char is vowel")
else:
    print("first char is consonent")

#Check if a number is divisible by 2 but not by 4.

n= int(input("enter num for q6"))
if(n%2==0 and n%4 != 0):
    print("num is div by 2 but not by 4")

