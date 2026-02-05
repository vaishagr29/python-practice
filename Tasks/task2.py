'''
1. s = "apple banana mango grapes"
Split the string into a list of words.
2. s = "red,green,blue,yellow"
Split using comma (,) as separator.
3. s = "Python@@Java@@C@@C++"
Split using @@.
4. s = "name=Akanksha;course=Python;year=2025"
Split using ; and display list.
5. words = ["apple", "banana", "mango"]
Join them with , .

'''




s = "apple banana mango grapes"
list1 = s.split()
print(list1)

s = "red,green,blue,yellow"
list2 = s.split(",")
print(list2)  

s = "Python@@Java@@C@@C++"
list3 = s.split("@@")
print(list3)

s = "name=Akanksha;course=Python;year=2025"
list4 = s.split(";")
print(list4)

words = ["apple", "banana", "mango"]
join1 = ",".join(words)
print(join1)