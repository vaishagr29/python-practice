# # comprehension - it is compact way of iterating over a sequence in single line of expression.
# # list comprehension - [expression for i in range() if(condition)]
# # set comprehension - {expression for i in range() if(condition)}
# # dictionary comprehension - {key_expre. : value_expre. for i in range() if(condition)}
# # generator expression - (expression for i in range() if(condition))


# 1. create list of marks greater than 50 from given list
marks=[20,56,17,82,91,45,76,44]

new_marks_list =[m for m in marks if(m>50)]
print("List of marks>50 : ", new_marks_list)

# 2. to generate list of squares from 1-10
sqr=[n**2 for n in range(1,11)]
print("list of sqr of numbers : ",sqr)

# 3. Create a list of words from a sentence "List comprehensions are powerful" that have length greater than 4.
words="List comprehensions are powerful".split()
word_list=[word for word in words if(len(word)>4)]
print(word_list)

# 4. Use list comprehension to create a list of tuples (number, square) for numbers 1 to 5.
l=[(i,i*i) for i in range(1,6)]
print(l)

# 5. Create a list comprehension to convert all strings in a list to uppercase.
l=["vaishnavi","agrawal"]
new_l=[i.upper() for i in l]
print(new_l)


print("set copmprehension \n")

# 1. Write a set comprehension to label numbers as even or odd.
data=[20,56,17,82,91,45,76,44]

labeled_num ={str(n)+"-even" if (n%2==0) else str(n)+"-odd" for n in data}
print(labeled_num)

# 2. Create a set comprehension to generate squares of numbers from 1 to 15, excluding multiples of 5.
s1={n**2 for n in range(1,16) if(n%5 !=0)}
print(s1)

# 3. Create a set comprehension to find unique vowels in a given sentence.
words="List comprehensions are powerful"
unique ={n for n in words if n in "aeiouAEIOU"}
print(unique)


print("dictinary comprehension \n")

#write a dict comprehension to create a dictionary of numbers and their squaRES FROM 0-4

d1={n:n**2 for n in range(0,5)}
print(d1)

#write a dict comprehension to filter only even values from a dictionary.
d1={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
d={a:b for a,b in d1.items() if(b%2==0)}
print(d)

# Use dictionary comprehension to swap keys and values in a given dictionary.
d={'a':1,'b':2,'c':3}
new_d={b:a for a,b in d.items()}
print(new_d)

# generator expression -- it is lazy execution

#display tuple of cubes of number

tup_cubes =(n**3 for n in range(2,11))
print(tuple(tup_cubes))

#display list of cubes of number.

list_cubes=(n**3 for n in range(2,11))
print(list(list_cubes))