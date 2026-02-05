# 1. Write a program to add two numbers entered by the user.
a=int(input("enter num a"))
b=int(input("enter num b"))
print(f" sum of a and b is : {a+b}")

# 2. Find the remainder when 29 is divided by 5.
print(f" remainder is : {29%5}")

# 3. Calculate the square of a number using the ** operator.
n = int(input("enter the num for squaring it: "))
print(f"square of the number is {n**2}")

# 4. Use floor division (//) to divide 17 by 4.
print(f"floor of 17 by 4 is {17//4}")

# 5. Multiply two numbers and print the result.
a=int(input("enter num a"))
b=int(input("enter num b"))
print(f" multiple of a and b is : {a*b}")

# 2. Relational (Comparison) Operators
# ------------------------------------
# 1. Check if two given numbers are equal or not.
a=int(input("enter num a"))
b=int(input("enter num b"))
print(f"Check if two given numbers are equal or not. {a==b}")

# 2. Write a program to check if 45 is greater than 20.
print(f"Write a program to check if 45 is greater than 20.{45>20}")

# 3. Compare two strings "apple" and "banana" using <.
print(f"Compare two strings apple and banana using < {"apple"<"bannana"} ")

# 4. Check if a number is less than or equal to 100.
a=int(input("enter num a"))
print(f"Check if a number is less than or equal to 100 {a<=100}")

# 5. Test if 10 != 15 and display the result.
print(f"result for Test if 10 != 15 is {10!=15}")

# 3. Logical Operators
# --------------------

# 1. Check if a number is between 10 and 50 using and.

s = int(input("enter num n"))
print(f"result of checking number btw 10-50 is {n>=10 and n<=50}")

# 2. Write a program to check if a number is either less than 0 or greater than 100 using or.
a=int(input("enter num a"))
print(f"if a number is less then zero or greater than 100 {a<0 or a>100}")

# 3. Use not to invert the result of a boolean expression.
a=10
print(f"Use not to invert the result of a boolean expression. {not(a>5)}")

# 4. Evaluate: (5 > 3) and (10 < 20).
print(f"Evaluate: (5 > 3) and (10 < 20). {5>3 and 10<20}")

# 5. Evaluate: (7 == 7) or (8 < 5).
print(f"Evaluate: (7 == 7) or (8 < 5).. {7 == 7 or 8<5}")

# 4. Assignment Operators
# -----------------------
# 1. Assign the value 25 to a variable and print it.
a=25
print(f"Assign the value 25 to a variable and print it : {a}")

# 2. Use += to add 10 to a variable.
a=2
a+=10
print(f"Assign the value 25 to a variable and print it : {a}")

# 3. Subtract 5 from a variable using -=.
a=10
a-=5
print(f"Subtract 5 from a variable using -=. : {a}")

# 4. Multiply a variable by 3 using *=.
a=10
a*=3
print(f"Multiply a variable by 3 using *=. : {a}")

# 5. Divide a variable by 2 using /= and print the result.
a=10
a/=2
print(f"divide a variable by 2 using /= and print the result: {a}")

# 5. Bitwise Operators
# --------------------
# 1. Find the result of 6 & 3.
print(f" Find the result of 6 & 3. {6&3}")

# 2. Find the result of 6 | 3.
print(f" Find the result of 6 | 3. {6|3}")

# 3. Find the result of 6 ^ 3.
print(f" Find the result of 6 ^ 3. {6^3}")

# 4. Perform left shift on 5 by 2 bits (5 << 2).
print(f" Perform left shift on 5 by 2 bits (5 << 2). {5<<2}")

# 5. Perform right shift on 16 by 3 bits (16 >> 3).
print(f" Perform right shift on 16 by 3 bits (16 >> 3). {16>>3}")

# 6. Identity Operators
# ---------------------
# 1. Check if two lists [1,2,3] and [1,2,3] are the same object using is.
l1=[1,2,3]
l2=[1,2,3]
print(l1 is l2)

# 2. Compare two variables referring to the same list with is.
l1=[1,2,3]
l2=l1
print(l1 is l2)

# 3. Check if two tuples (1,2) and (1,2) are not the same object.
t1=(1,2,3)
t2=(1,2,3)
print(t1 is not t2)

# 4. Create two variables pointing to the same string and check with is.
s1="vaishnavi"
s2=s1
print(s1 is s2)

# 5. Verify if a copied list is different from the original list using is not.
l1=[1,2,3]
l2=l1.copy()
print(l1 is not l2)

# 7. Membership Operators
# -----------------------
# 1. Check if the number 5 exists in the list [1,2,3,4,5].
lst = [1, 2, 3, 4, 5]
print(5 in lst)

# 2. Verify if "a" is in the string "apple".
s="apple"
print("a" in s)

# 3. Check if "dog" is not in the list ["cat", "cow", "goat"].

l = ["cat", "cow", "goat"]
print("dog" not in l)

# 4. Write a program to see if 10 is in the tuple (15,18,10,89).
t = (15,18,10,89)
print(10 in t)

# 5. Check if "Python" is not in the list ["Java", "C++", "Ruby"].
l = ["Java", "C++", "Ruby"]
print("Python" not in l)

# 8. Combination of operators.
# ---------------------------
# 1. For x = 20, y = 10, print (x - y == 10) and (x / y == 2).
x = 20
y = 10
print((x - y == 10) and (x / y == 2))

# 2. For a = 18, b = 9, print (a // b == 2) and (a % b == 0).
a = 18
b = 9
print((a // b == 2) and (a % b == 0)) 

# 3. For m = 7, n = 3, print (m * n == 21) or (m + n == 12).
m = 7
n = 3
print((m * n == 21) or (m + n == 12))

# 4. For p = 16, q = 4, print (p / q == 4) and (p ** q == 256).
p = 16
q = 4
print((p / q == 4) and (p ** q == 256))

# 5. For x = 25, y = 5, print (x % y == 0) and not (x < y).
x = 25
y = 5
print((x % y == 0) and not (x < y)) 

# 6. For a = 11, b = 2, print (a // b == 5) and (a % b == 1).
a = 11
b = 2
print((a // b == 5) and (a % b == 1))

# 7. For p = 7, q = 14, print (p * 2 == q) and (q % p == 0).
p = 7
q = 14
print((p * 2 == q) and (q % p == 0))

# 8. For a = 12, b = 6, print (a / b == 2) and (a % b == 0).
a = 12
b = 6
print((a / b == 2) and (a % b == 0))

# 9. For x = 9, y = 3, print (x > y) and (x % y == 0).
x = 9
y = 3
print((x > y) and (x % y == 0))  

# 10. For m = 5, n = 25, print (n / m == 5) or (m * m == n).
m = 5
n = 25
print((n / m == 5) or (m * m == n))

# 11. For p = 8, q = 2, print (p ** q == 64) and (p / q == 4).
p = 8
q = 2
print((p ** q == 64) and (p / q == 4))

# 12. For a = 15, b = 4, print (a // b == 3) and not (a % b == 0).
a = 15
b = 4
print((a // b == 3) and not (a % b == 0))

# For example ,do like below.
# # For p = 7, q = 14, print (p * 2 == q) and (q % p == 0)

# p = 7
# q = 14
# print(p * 2 == q)  # 7 * 2 == 14 = T
# print(q % p == 0)  # 14 % 7 == 0 = T
# print("Q - ",(p * 2 == q) and (q % p == 0))   # T and T = T

# 9. Membership + Logical
# -----------------------

# 1. For s = "developer", print 'd' in s.
s = "developer"
print('d' in s) 

# 2. For s = "programming", print 'x' not in s.
s = "programming"
print('x' not in s)    

# 3. For lst = [2, 4, 6, 8, 10], print 6 in lst.
lst = [2, 4, 6, 8, 10]
print(6 in lst)   

# 4. For lst = [100, 200, 300], print 150 not in lst.
lst = [100, 200, 300]
print(150 not in lst)

# 5. For d = {"x": 10, "y": 20}, print 'z' not in d.
d = {"x": 10, "y": 20}
print('z' not in d)

# 6. For s = "datastructure", print "struct" in s.
s = "datastructure"
print("struct" in s)  

# 7. For s = "computerscience", print ("science" in s and "math" not in s).
s = "computerscience"
print("science" in s and "math" not in s)

# 8. For s = "informationtechnology", print ("tech" in s and "IT" not in s).
s = "informationtechnology"
print("tech" in s and "IT" not in s)

# 9. For s = "machinevision", take "vision" from user and check if it is in s.
s = "machinevision"
word = input("Enter word: ")
print(word in s)

# 10. For s = "natural language processing", print ("language" in s and "speech" not in s).
s = "natural language processing"
print("language" in s and "speech" not in s)

# Tuple Packing and Unpacking Questions.

# 1. Pack 3 numbers (10, 20, 30) into a tuple and unpack them into variables a, b, c. Print each variable.
t = (10, 20, 30)   # packing
a, b, c = t       # unpacking
print(a)
print(b)
print(c)

# 2. Pack values "apple", "banana", "cherry", "mango" into a tuple and use extended unpacking to assign the first value to x, the last value to y, and the middle values to a list named rest. Print x, rest, y.
t=("apple","banana","cherry","mango")
x,*rest, y=t
print(x)
print(rest)
print(y)

# 3. Given a tuple (5, 10, 15, 20, 25), unpack the first two values into variables a, b and the remaining values into a list using *. Print all.
t=(5, 10, 15, 20, 25)
a,b,*rest=t
print(a)
print(b)
print(rest)

# 4. Take a tuple (100, 200, 300, 400) and unpack it into variables w, x, y, z. Then print the sum of all unpacked variables.
t = (100, 200, 300, 400)
w, x, y, z = t
print(w + x + y + z)

# 5. Given tuple ("Python", "Java", "C", "C++", "Go"), use extended unpacking to store the first element in lang1, the last element in lang2, and the rest in others. Print lang1, lang2, and others.
t = ("Python", "Java", "C", "C++", "Go")
lang1, *others, lang2 = t
print(lang1)
print(lang2)
print(others)
