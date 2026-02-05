


#1.Create a list of 5 cities and print the third city using positive indexing and the last city using negative indexing.
city = ["mumbai","delhi","pune","nagpur","nashik"]
print("third city:",city[2]) 
print("last city:",city[-1]) 

#2.Write a program to create a list of first 10 odd numbers using manual entry.

first_ten_odds =[]
first_ten_odds.append(1)
first_ten_odds.append(3)
first_ten_odds.append(5)
first_ten_odds.append(7)
first_ten_odds.append(9)
first_ten_odds.append(11)
first_ten_odds.append(13)
first_ten_odds.append(15)
first_ten_odds.append(17)
first_ten_odds.append(19)
print("first ten odds:", first_ten_odds)

#OR

first_ten_odds1 =[1,3,5,7,9,11,13,15,17,19]
print("first ten odds:", first_ten_odds1)


#3.Given a list nums = [2, 4, 6, 8, 10], access and print the second-last element using negative indexing.

nums = [2, 4, 6, 8, 10]
sec_last=nums[-2]
print(sec_last)


#4.Concatenate the two lists a = [1,2,3] and b = [4,5,6] and print the result.
a = [1,2,3] 

b = [4,5,6]

concated_list =a+b
print(concated_list)

#OR

a.extend(b)
print(a)



#5.Create a nested list and print a specific element (for example: from [1, [2,3,[4,5]], 6] print 5).

nested_list =[1, [2,3,[4,5]], 6]
print(nested_list[1][2][1])

'''

#Slicing & Indexing

1.Given colors = ["red","blue","green","yellow","black","white"],

	print ["green","yellow"] using positive slicing.

	print ["white","black"] using negative slicing.

    '''
colors = ["red","blue","green","yellow","black","white"]
print(colors[2:4])
print(colors[-1:-3:-1])


#2.Create a list of first 15 even numbers and use slicing to display only numbers from 8 to 16.

first_15_even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
print(first_15_even[3:8])


#3.Write a program to reverse a list using slicing.

colors = ["red","blue","green","yellow","black","white"]
print(colors[::-1])

#4.From the list nums = [100,200,300,400,500,600], extract [300,400,500] using slicing.
nums = [100,200,300,400,500,600]
print(nums[2:5])

#5.Given x = [1,2,3,4,5,6,7,8,9], print only the odd numbers using step slicing.

x = [1,2,3,4,5,6,7,8,9]
print(x[::2])



#Mutability & Modification

#1.Create a list marks = [45, 56, 78, 89, 90]. Modify the second element to 60 and the last element to 95.

marks = [45, 56, 78, 89, 90]
length=len(marks)
marks[1]=60
marks[length-1]=95
print(marks)


#2.Replace the middle three elements of [10,20,30,40,50] with [25,35,45].

list=[10,20,30,40,50]
list[1:4] = [25,35,45]
print(list)

#List Methods

#1.Create a list of names and add three new names using append().

names=[]
names.append("Vaish")
names.append("vaishnavi")
names.append("vaishu")
print(names)

#2.Create two lists of numbers and merge them using extend().
a = [1,2,3] 

b = [4,5,6]

a.extend(b)
print(a)

#3.Insert "Python" at the 2nd position in the list ["Java","C++","C","Go"].
list= ["Java","C++","C","Go"]
list.insert(1,"Python")
print(list)

#4.Write a program to delete the element 500 from the list [100,200,300,400,500,600] using remove().

list =[100,200,300,400,500,600]
list.remove(500)
print(list)

#5.Create a list [10,20,30,40,50], use pop() to delete the last element, and display the modified list.

list =[10,20,30,40,50]
length= len(list)
list.pop(-1)
print(list)


#6.Write a program to sort the list letters = ['d','a','z','c','b'] in ascending order and then in descending order.

letters = ['d','a','z','c','b']
letters.sort()
print(letters)
letters.sort(reverse=True)
print(letters)


'''
7.Create a list of numbers and display:

	Sum of all elements

	Maximum element

	Minimum element

'''
list =[10,20,30,40,50]
sum_of_list = sum(list)
max_element =max(list)
min_element =min(list)

print("sum :",sum_of_list,"\nmax element :",max_element,"\nmin element :",min_element)


#TUPLE QUESTIONS

#1. Create a tuple with 5 integers and print its length.
tup=(1,2,3,4,5)
print(len(tup))

#2. Create a tuple with 5 strings and print the second last element using negative indexing.

tup=("hi","hello","hey","woof","meow")
print(tup[-2])

#From the tuple (10,20,30,40,50), access elements from index 1 to 3 (inclusive of start, exclusive of end).
t = (10, 20, 30, 40, 50)
print(t[1:3])

#4. Create a tuple ("a","b","c") and concatenate it with ("d","e").

tup1 = ("a", "b", "c")
tup2 = ("d", "e")
print(tup1 + tup2)

#5. Create a tuple (100,). Print its type and explain why comma is important.

t = (100,)
print(type(t))
#If we don’t use a comma, Python thinks (100) is just a normal number written inside brackets, not a tuple.

#6. Create a tuple (1,2,3,4,5) and extract the last three elements using slicing.

t = (1, 2, 3, 4, 5)
print(t[-3:])


#7. Create a nested tuple (1, (2,3), (4,5,6)) and access 5.

t = (1, (2,3), (4,5,6))
print(t[2][1])


#8. Swap two variables a=10 and b=20 using tuple unpacking.

a = 10
b = 20
(a, b) = (b, a)
print(a, b)


#9. Create a tuple with duplicate values (5,5,5,10,20) and use count() to find how many times 5 appears.

tup = (5, 5, 5, 10, 20)
print(tup.count(5))


#10. Use the tuple (2,4,6,8,10) and check the index of element 8.

tup = (2, 4, 6, 8, 10)
print(tup.index(8))


#11. Demonstrate tuple packing.

person = ("vaishnavi", 21, "indore")
print(person)


#12. Demonstrate tuple unpacking.

person = ("vaishnavi", 21, "indore")
name, age, city = person
print(name, age, city)


#13. Create a tuple (1 to 10) and extract every second element using slicing.

t = (1,2,3,4,5,6,7,8,9,10)
print(t[1::2])


#14. Create a tuple (1,2,3,4,5) and reverse it using slicing.

t = (1,2,3,4,5)
print(t[::-1])


