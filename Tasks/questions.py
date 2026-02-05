
'''
# LIST

# 1.Create a list from user input and print the first and last element using indexing.
user_list = input("Enter elements: ").split()
print(user_list[0], user_list[-1])

# 2.Take a list of string numbers from the user and print a sublist of the first 3 elements using slicing.
string_numbers = input("Enter string numbers: ").split()
print(string_numbers[:3])

# 3.From a user-created list, print the list in reverse order using slicing.
original_list = input("Enter elements: ").split()
print(original_list[::-1])

# 5.Input a list of items from the user and use the + operator to concatenate it with another list (e.g., [100, 200]).
items = input("Enter items: ").split()
print(items + [100, 200])

# Let L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
L = [0,1,2,3,4,5,6,7,8,9]

# 7.Using a negative step, produce a list that starts at the last element and takes every 2nd element moving leftward.
# Expected o/p - [9, 7, 5, 3, 1]
print(L[::-2])

'''

# 1. Given a list of numbers, use slicing to create a new list containing only the middle elements (exclude first and last elements).
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = L[1:-1]
print(new_list)

# 2. Write a program to reverse a list using slicing.
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[-1::-1])

# 3. Given lst = [10, 20, 30, 40, 50, 60], use slicing to create:
#    a) a list of first three elements
lst = [10, 20, 30, 40, 50, 60]
first_three= lst[:3]
print(first_three)
#    b) a list of last three elements
last_three=lst[-3:]
print(last_three)

# 4. Given two lists, use list concatenation to create a new list that contains elements of both lists.
l1=[10, 20, 30]
l2=[40, 50, 60]
new_list=l1+l2
print(new_list)

# 5. Write a program to add multiple elements to an existing list using a list method.
l1=[10, 20, 30]
l2=[40, 50, 60]
l1.extend(l2)
print(l1)

# 6. Given a list, use a list method to remove a specific element from the list.
l1=[10, 20, 30]
l1.remove(20)
print(l1)

         