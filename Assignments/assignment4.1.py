# Break questions

# 1.	Write a program to print numbers from 1 to 10, but stop when the number is 5.

for i in range(1,11):
    if(i==5):
        break
    else:
        print(i,end=" ")
print()
# 2.	Use a while loop to keep printing numbers starting from 1, and stop when the number reaches 7.
i=1
while(i<7):
    print(i,end=" ")
    i=i+1
print()
# 3.	Iterate over a list [10, 20, 30, 40, 50] and stop the loop when you find 30.
list =[10, 20, 30, 40, 50]
for i in list:
    if(i==30):
        break
    else:
        print(i, end=" ")
print()
# 4.	Print characters of the string "PYTHON", stop when the character is "T".
s="PYTHON"
for i in s:
    if(i=="T"):
        break
    else:
        print(i,end=" ")
print()
# 5.	Take numbers from the user repeatedly and stop when they enter a negative number.
while(True):
    i=int(input("enter a num"))
    if(i<0):
        break
    else:
        print(i, end=" ")
print()
# 6.	Iterate through a list of names and stop when you find "John".
l=["vaish","vini","sam","jhon","mick"]
for i in l:
    if(i=="jhon"):
        break
    else:
        print(i,end=" ")
print()
# 7.	Traverse a list of words and stop when you find a word longer than 8 characters.
l=["vaish","vini","sam","jhon","vaishnavi","mick"]
for i in l:
    if(len(i)>=8):
        break
    else:
        print(i, end=" ")
print()
# 8.	Iterate over a string and stop once you find a space " ".
s="vaishn avi"
for i in s:
    if(i==" "):
        break
    else:
        print(i, end=" ")
print()
# 9.	From a string, stop at the first uppercase letter.
s="vaishN avi"
for i in s:
    if(i.isupper):
        break
    else:
        print(i,end=" ")
print()
# 10.	From a dictionary of student scores, stop when a score is less than 35.
d={"vaish": 90,"vini":70,"sam":75,"jhon":35,"mick":34}

for value in d:
    if(d[value]<35):
        break
    else:
        print(d[value],end=" ")
print()
# Continue questions


# 1.Print numbers from 1 to 10, but skip printing the number 5.

for i in range(1,11):
    if i == 5:
        continue
    else:
        print(i, end=" ")
print()

# 2.Print numbers from 1 to 20, skipping odd numbers.
for i in range(1,21):
    if i%2:
        continue
    else:
        print(i, end=" ")
print()
# 3.Print numbers from 1 to 20, skipping even numbers.
for i in range(1,21):
    if i%2:
        print(i, end=" ")
    else:
        continue
print()
# 4.Print numbers 1–30, but skip those divisible by 3.
for i in range(1,11):
    if i%3:
        continue
    else:
        print(i, end=" ")
print()

# 5.Iterate through a string "HELLO WORLD" and skip spaces.
s="HELLO WORLD"
for i in s:
    if i==" ":
        continue
    else:
        print(i, end="")
print()

# 6.Print fruits from a list but skip "apple".
l = ["apple", "banana", "mango", "orange"]
for i in l:
    if i=="apple":
        continue
    print(i, end=" ")

# 7.From a list of numbers, skip multiples of 5.
nums = [1,20,10,4,5,6,15,9]
for i in nums:
    if i%5==0:
        continue
    print(i,end=" ")
# 8.Iterate through a string and skip letters "x" and "y".
s="tuvwxyz"
for i in s:
    if(i=="x" or i=="y"):
        continue
    else:
        print(i,end=" ")
print()
# 9.Print dictionary items but skip keys starting with "A".
d = {"Banana":45,"Mango":65,"Apple":35,"Orange":75}
for key in d:
    if (key[0]=="A"):
        continue
    print(key, d[key],end=" ")