# enumerate() Questions

# Given a list of names, print only those whose index is even along with their index.
names=["vaish","vini","ayushi","pranjal"]
for i, f in enumerate(names): 
      if(i%2)==0:
            print(i,f)
            
# Convert a list into a dictionary where index is key and value is list element, starting index from 1.
names=["vaish","vini","ayushi","pranjal"]
dict={}
for i, j in enumerate(names):
      dict[i]=j
print(dict)

# From a sentence, print each word with its position but skip words shorter than 4 letters.
sentence = "Hello, my name is V and i am a GB"
words = sentence.split()
for i, word in enumerate(words, start=1):
    if len(word) >= 4:
        print(i, word)

# Create a list of tuples (index, square_of_number) from a list of numbers.
names=[1,2,3,4,5]
result=[(i,f**2) for i, f in enumerate(names)]
print(result)
# Find the index positions where a given value appears in a list.
names=["vaish","vini","ayushi","pranjal"]
for i, f in enumerate(names): 
      print(f"index of value {f} is {i}")

# eval() Questions

# Take a mathematical expression from user input and evaluate it safely.
num=input("enter a string")
print(eval(num))

# Input a list as string (e.g. "[1,2,3]") and calculate its sum using eval().
num=input("enter a List")
lst=eval(input("enter a List"))
print(lst)
ans=sum(lst)
print(ans)

# Accept a dictionary string from user and print all keys.
# Evaluate a logical expression entered by user and print whether result is True or False.
# Build a simple calculator that evaluates operations like "10+5*2".

# zip() Questions

# Combine two lists (names and marks) into a dictionary using zip().
# From two lists of numbers, create a list containing sum of paired elements.
# Given three lists, combine them into a list of tuples but stop at shortest list.
# Unzip a list of tuples into separate lists.
# Compare two lists and print pairs where elements are equal.

