st= "Hello World"
print(len(st))

st2= 'Hello World'
print(len(st))

para="""

This communication is intended solely for the person or organization to 
whom it is addressed and may be confidential and/or legally privileged. 
If you are not the intended recipient, you must not show it to anyone, copy, d
istribute, or take any action in reliance on it. If you have received this message 
in error, please inform us at  and delete this email from your system.

"""
print(len(para))


# \n - newline character , \t - tab space
fruits = "apple\nbanana\nchickoo"
print(fruits)
print("Menu:\n1.Biryani.\n2.Pizza.")
heading = "Name\tCity"
data = "Kriti\tPune"
print(heading)
print(data)
# concatination - joining of strings
first_name = "Akanksha"
last_name = "Ramane"
full_name = first_name+" "+last_name
print(full_name)



# join() - it takes all substring in an iterable(list,tuple etc.)
# and joins all together in a string, acc. to separator provided.
# syntax : "".join(iterable)
fruits = ["apple","cherry","banana","jackfruit"]
fruit_join = "-".join(fruits)
print(fruit_join)
print(type(fruit_join))    # <class 'str'>
data = ("2026","30","01")
date = "/".join(data)
print(date)
name = "akanksha"
asc_order = "".join(sorted(name))
print(asc_order)
# do for descending order.
