# FILTER() QUESTIONS

 

# 1. Filter numbers divisible by 3 from a list.
num=[1,2,3,4,5,6,7,8]
ans=list(filter(lambda n: n%3==0,num))
print(ans)

# 2. Filter words that contain letter 'e'.
words=["apple","banana","grape","kiwi","melon"]
ans=list(filter(lambda n: 'e' in n,words))
print(ans)
# 3. Filter students whose marks are above 75 from a list.
marks=[65,80,90,72,88,70]
ans=list(filter(lambda n: n>75,marks))
print(ans)
# 4. Filter words whose length is more than 4.
words=["cat","tiger","lion","horse","dog"]
ans=list(filter(lambda n: len(n)>4,words))
print(ans)

# 5. Filter negative numbers from a list.
num=[2,-3,4,-1,6,-5]
ans=list(filter(lambda n: n<0,num))
print(ans)
 

 

 

# MAP() QUESTIONS

 

# 1. Convert temperatures from Celsius list to Fahrenheit.
temp=[0,10,20,30,40]
ans=list(map(lambda n:(n*9/5)+32,temp))
print(ans)
# 2. Multiply each number in list by 5.
temp=[0,10,20,30,40]
ans=list(map(lambda n:(n*5),temp))
print(ans)
# 3. Convert list of strings into their lengths.
words=["apple","cat","banana","kiwi"]
ans=list(map(lambda n:len(n),words))
print(ans)

# 4. Convert list of strings into integers.
nums=["1","2","3","4","5"]
ans=list(map(lambda n:int(n),nums))
print(ans)

# 5. Find length of each word in a list.
words=["dog","tiger","elephant","fox"]
ans=list(map(lambda n:len(n),words))
print(ans)
 

 

 

# REDUCE() QUESTIONS

 

# 1. Find the factorial of a number using reduce().


# 2. Find the largest string in list based on length.

# 3. Find total sum of squares of numbers.

# 4. Find minimum number from list.

# 5. Concatenate all strings in a list into one string.




