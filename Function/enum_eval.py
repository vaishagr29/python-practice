''''
enumerate() - it gives couter/index to your iterable object.
used when you want both values as well as index.

Syntax :
enumerate(iterable object , start)



'''

city = ["pune","mumbai","nashik","jalna","nanded"]

for i, value in enumerate(city):
    print("index : ",i, "-","value: ",value)
print()

result =list(enumerate(city))
print("enumerate outpur: ",result)

print()

for i in enumerate(city):
    print(i)
print()

students =["pooja","Nisha","kajal","priya","dev"]

for roll_no,name in enumerate(students, start=121):
    print(f"roll no : {roll_no}, Name: {name}")

mp={"vaishnavi":21,"vini":23,"ayushi":22}
for n,items in enumerate(mp.items()):
    print(f"id:{n}, name : {items}")


# 1. Write a program using enumerate() to find the index of a specific element in a list.
# city = ["pune","mumbai","nashik","jalna","nanded"]
# c=input("enter a city")
# for i, value in enumerate(city):
#     if(value==c):
#         print("index value for C is : ",i)
# print()

# # 2. Use enumerate() to modify a list so that each element becomes a tuple of (index, value). do it
result =list(enumerate(city))
print("enumerate outpur: ",result)

# # 3. Write a program using enumerate() inside a list comprehension to create a list of (index, square of element).


expr="'A'*2"
result=eval(expr)
print(result)


# expr1=input("h")
# result1=eval(expr1)
# print(result1)
# print(type(result1))

'''
Use eval() to evaluate a variable expression where values are defined in a dictionary.

d = {'a':20,'b':3,'c':10,'d':40}

exp = "a+b-c*d"
'''

d={'a':20,'b':3,'c':10,'d':40}
exp="a+b-c*d"
result=eval(exp,d)
print(result)

'''
zip()-it combines two or more iterables element - wise into tuple
used for creating dictionary
zip(iterable, iterable2.....)
'''

list1 = ["neha","janvi","kartik","varad"]
list2=[201,202,203,204]

data=list(zip(list1,list2))
print(data)

keys =["batch1","btach2","batch3"]
values=["ds","da","ai"]
data=list(zip(keys,values))
print(data)


'''
 even keys between: 10-20     use list comprehension

odd value between: 0-10

in a dict using zip
'''



