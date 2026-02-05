# 1check if a number is positive , even , odd or negative

n= int(input("enter num "))
if(n>0):
    if(n%2==0):
        print("num is even")
    else:
        print("num is negative")
else:
    print("num is negative")

#2write a python prog to check result 
#mark<40 ->fail, 40-70->pass,>=75 pass with distiction
n=int(input("enter marks "))
if(n>=40):
    if(n>=75):
        print("pass with disticntion")
    else:
        print("pass")
else:
    print("fail")

#3login system check username, then check password

username = input("enter username : ")
password=input("enter password : ")
if(username=="vaish@gmail.com"):
    if(password=="123"):
        print("login successfull")
    else:
        print("invalid password")
else:
    print("invalid username")

# 4. Greatest among three numbers.

a =int(input("Enter a: "))
b =int(input("Enter b: "))
c =int(input("Enter c: "))

if(a>b):
    if(a>c):
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if(b>c):
        print("b is greatest")
    else:
        print("c is greatest")

#   5. Check if a number is divisible by 2, then check divisibility by 4.
n= int(input("enter num "))

if(n%2==0):
    if(n%4==0):
        print("div by both 2 and 4")
    else:
        print("div by only 2")
else:
    if(n%4==0):
        print("div by only 4")
    else:
        print("div by nor 4 neither 3")

#   6. Find the smallest of 3 nos using nested if-else

a =int(input("Enter a: "))
b =int(input("Enter b: "))
c =int(input("Enter c: "))

if(a<b):
    if(a<c):
        print("a is smallest")
    else:
        print("c is smallest")
else:
    if(b<c):
        print("b is smallest")
    else:
        print("c is smallest")

