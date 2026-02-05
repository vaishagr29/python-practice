    # 1.print the even elements
print("q1\n")
list=[1,2,3,4,5,6,7,8]
for i in list:
    if(i%2==0):
        print(i)

    # 2.print the even indexed elements
print("\n")
list=[1,2,3,4,5,6,7,8]
for i in range(len(list)):
    if(i%2==0):
        print(list[i])
print("\n")
    # 3.print the no not divisible by 5 from list l=[1,2,3,5,15,10,4]
l=[1,2,3,5,15,10,4]
for i in range(len(l)):
    if(l[i]%5!=0):
        print(l[i])
print("\n")

    # 4.print the no divisible by 3 from list l=[1,2,3,5,6,10,9]
l=[1,2,3,5,6,10,9]
for i in range(len(l)):
    if(l[i]%3==0):
        print(l[i])
print("\n")

    # 5.print the elements of list which are not s l=['a','z','s','x','p']
l=['a','z','s','x','p']
for i in range(len(l)):
    if(l[i]!='s'):
        print(l[i])
print("\n")

    # 6.create a list from user without using split() method.

list =[]
for i in range(5):
    list.append(input("enter num"))

print(list)
print("\n")

    # 7.Write a Python program to separate even numbers from the list  # l = [1,2,3,4,5,6,7,8] and print them in different list.
l=[1,2,3,4,5,6,7,8,10,9,12]
list =[]
for i in range(len(l)):
    if(l[i]%2==0):
        list.append(l[i])
print(list)
print("\n")

    # 8.Write a Python program to separate even and odd numbers from the list 
    #     l = [1,2,3,4,5,6,7,8] and print them in two different lists.
l = [1,2,3,4,5,6,7,8]
list_even =[]
list_odd =[]
for i in range(len(l)):
    if(l[i]%2==0):
        list_even.append(l[i])
    else:
        list_odd.append(l[i])
print(list_even)
print("\n")
print(list_odd)

    # 9.Write a Python program to separate elements at even and odd indices from the list 
    #     fruits = ["apple", "banana", "cherry", "date", "fig", "grape"] and print them in two lists.

l = ["apple", "banana", "cherry", "date", "fig", "grape"]
list_even =[]
list_odd =[]
for i in range(len(l)):
    if(i%2==0):
        list_even.append(l[i])
    else:
        list_odd.append(l[i])
print(list_even)
print("\n")
print(list_odd)
print("\n")

    # 10.Count number of elements in a list without using length function(len()).
l = [1,2,3,4,5,6,7,8]
cnt=0
for i in l:
    cnt+=1
print(cnt)
print()

    # 11.Frequency count of an element in a list.
l = ["python","ml","ds","da","python","python","da"]
for i in range(len(l)):
    cnt=0
    for j in range(i,len(l)):
        if(l[j]==l[i]):
            cnt+=1
    print(f"{l[i]} is apearing {cnt} times")
print()
# 12.Find the maximum number from a given list.
l = [1,2,3,4,5,6,7,8]
maxi=-1
for i in l:
    if(i>maxi):
        maxi=i
print(maxi)
print()

    # 13.Given a string "programming", use a for loop to count how many vowels are in the string. 

string= "programming"
cnt=0
for n in string:
    if(n in "aeiouAEIOU"):
        cnt+=1
print(cnt)
print()

    # 14. Traverse a list of numbers and print "large" if a number is greater than 50, "small" otherwise.
l = [10,20,30,40,50,60,70,80]
for i in range(len(l)):
    if(l[i]>50):
        print("large")
    else:
        print("small")
print("\n")

    # 15. Traverse a string and print "Uppercase" for uppercase letters, "Lowercase" for lowercase letters.

s="NoNcHaLaNtLy"
for i in s:
    if(i.isupper()):
        print("uppercase")
    else:
        print("lowercase")