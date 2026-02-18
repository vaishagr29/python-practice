# List comprehension
# 1. Write a list comprehension to create a list of numbers from 1 to 10.
l=[n for n in range(1,11)]
print(l)
print("\n")
# 2. Write a list comprehension to create a list of even numbers between 1 and 20.
l=[n for n in range(1,21) if(n%2==0)]
print(l)
print("\n")
 
# 3. Write a list comprehension to create a list of squares of numbers from 1 to 10.
l=[n**2 for n in range(1,11)]
print(l)
print("\n")
 
# 4. Write a list comprehension to create a list of cubes of numbers from 1 to 5.
l=[n**3 for n in range(1,6)]
print(l)
print("\n")
 
# 5. Write a list comprehension to create a list of all characters in the string "Python".
s="Python"
l=[n for n in s]
print(l)
 
# 6. Write a list comprehension to create a list of vowels from the string "education".
s = "education"
l = [ch for ch in s if ch in "aeiouAEIOU"]
print(l)
print("\n")
 
# 7. Write a list comprehension to create a list of numbers between 1 and 30 that are divisible by 3.
l = [n for n in range(1,31) if n % 3 == 0]
print(l)
print("\n")

# 8. Write a list comprehension to create a list of the first letters of each word in ["apple", "banana", "cherry"].
words = ["apple", "banana", "cherry"]
l = [word[0] for word in words]
print(l)
print("\n")

# 9. Write a list comprehension to create a list of numbers from 1 to 10, but store "Even" for even numbers and "Odd" for odd numbers.
l = ["Even" if n % 2 == 0 else "Odd" for n in range(1,11)]
print(l)
print("\n")

# 10. Write a list comprehension to create a list of squares for only even numbers between 1 and 20.

l = [n**2 for n in range(1,21) if n % 2 == 0]
print(l)

# 13. Create a dictionary mapping numbers to their squares (1 to 10).
d={n:n**2 for n in range(1,11)}

# 14. Reverse keys and values of a dictionary using comprehension.
d={'a':1,'b':2,'c':3}
new_d={b:a for a,b in d.items()}
print(new_d)

# 15. Create a dictionary from two lists: one list of keys and another list of values.
l_key=["a","b","c","d"]
l_value=[1,2,3,4]

d={l_key[a]:l_value[a] for a in range(len(l_key))}
print(d)

# 16. Filter a dictionary to keep only items where value is even.
d={'a':1,'b':2,'c':3}
even_d={b:a for a,b in d.items() if(b%2==0)}
print(even_d)

# 17. Convert a list of tuples into a dictionary using comprehension.
t = [("a", 1), ("b", 2), ("c", 3)]
d = {k: v for k, v in t}
print(d)

# 18. Given a word, count frequency of each character using dictionary comprehension.
s = "banana"
d = {i: s.count(i) for i in s}
print(d)

# 19. Map each word in a sentence to its length.
s="List comp is powerfull".split()
d={n:len(n) for n in s }
print(d)

# 20. Create a dictionary of items and their prices with discount applied using comprehension.
