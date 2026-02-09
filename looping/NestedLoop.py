'''
nested loops = loop-loop inside another loop

'''

##1. Given a list of lists, print all elements using nested for loops.

list=[[1,2],[3,4],[4,5]]

for i in list:
    for j in i:
        print(j)

## 2. Given a list [1, 2, 3], print all possible pairs (a, b) using nested for loops.

list=[1,2,3]

for i in list:
    for j in list:
        print((i,j))

##3. Given a string "abc", print all possible pairs of characters.

s="abc"

for i in s:
    for j in s:
        print((i,j))

##4. Given two lists, print all pairs (a, b) where a is from the first list and b is from the second list.

l1=[1,2,3]
l2=[4,5,6]

for i in l1:
    for j in l2:
        print((i,j))

##5. Given a list [1, 2, 3, 4], print all pairs (a, b) where both numbers are even.

l=[1,2,3,4]

for i in l:
    if(i%2==0):
        for j in l:
            if(j%2==0):
                print(i,j)





