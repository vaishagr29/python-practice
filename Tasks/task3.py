
#classify a num as posotive negative or zero

n= int(input("enter num :"))
if(n>0):
    print("num is positive")
elif(n<0):
    print("num is negative")
else:
    print("num is zero")

#Classify a matter es positive, negative, I
# 2. Classify a character as vowel, comonent, or other.
c= input("enter num :")
vowel = "aeiouAEIOU"

if(c in vowel):
    print("char is vowel")
elif(c.isalpha and c not in vowel):
    print("char is consonant")
else:
    print("other")
# 3. Classify age into child (<13), teenager (13-19), or alt (20+).
age = int(input("enter age"))
if(age<13):
    print("is child")
elif(age>=13 and age<=19):
    print("is teenager")
else:
    print("adult")

# 4.  Check if a number is divisible by 2, 3, or neither.
n = int(input("enter num"))
if(n%2==0 and n%3==0):
    print("div by 2 and 3")
elif(n%3==0):
    print("div by 3")
elif(n%2==0):
    print("div by 2")
else:
    print("neither")
# 5.  Classify a day number (1-7) into weekday or weekend.
n = int(input("enter num"))
if(n>=1 and n<=5):
    print("weekdays")
elif(n==6 or n==7):
    print("weekends")
else:
    print("not valid")

# 6.  Classify marks into grades: A (≥90), B (≥75), C (≥50), F (<50).
n = int(input("enter num"))
if(n>=90):
    print("A")
elif(n>=75):
    print("B")
elif(n>=50):
    print("c")
else:
    print("F")
# 7. Enter a number (1-7) and print the day name. If not in range, print "Invalid".
n = int(input("Enter a number (1-7): "))
if (n==1):
    print("Monday")
elif (n==2):
    print("Tuesday")
elif (n == 3):
    print("Wednesday")
elif (n == 4):
    print("Thursday")
elif (n == 5):
    print("Friday")
elif (n == 6):
    print("Saturday")
elif (n == 7):
    print("Sunday")
else:
    print("Invalid")

# 8. Input color ("red", "yellow", "green") and print "Stop", "Get Ready", or "Go". Otherwise, print "Invalid Color".
s=str(input("enter string"))
if(s=="red"):
    print("stop")
elif(s=="yellow"):
    print("get ready")
elif(s=="green"):
    print("go")
else:
    print("invalid")

# 9. Input a year. Print "Leap Year", "Not Leap Year", or "Invalid input" (for negative years).
#     (Rule: divisible by 4 but not by 100, except divisible by 400).
n=int(input("enter year"))
if(n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print("is leap year")
elif(n<0 ):
    print("invalid")
else:
   print("not leap year")

# 10.Input two numbers and an operator (+, -, *, /). Use if-elif to perform the correct operation.
a=int(input("enter a"))
b=int(input("enter b"))
symbol=input("enter symbol")

if(symbol=="+"):
    print(a+b)
elif(symbol=="-"):
    print(a-b)
elif(symbol=="*"):
    print(a*b)
elif(symbol=="/"):
    print(a/b)
else:
    print("invalid symbol")

