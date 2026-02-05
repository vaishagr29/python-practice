# Assignment Questions on Set (10)

# Q1. Create a set with numbers {1,2,3,4,5} and display it.
set_for_q1 = {1, 2, 3, 4, 5}
print(set_for_q1)

# Q2. Add an element 10 to a set {1,2,3}.
set_for_q2 = {1, 2, 3}
set_for_q2.add(10)
print(set_for_q2)

# Q3. Remove the element 2 from the set {1,2,3,4} using .remove().
set_for_q3 = {1, 2, 3, 4}
set_for_q3.remove(2)
print(set_for_q3)

# Q4. Try to remove an element 100 from the set {1,2,3} using .discard() and check the difference with .remove().
set_for_q4 = {1, 2, 3}
set_for_q4.discard(100)
print(set_for_q4)

# Q5. Create two sets: A = {1,2,3,4} and B = {3,4,5,6}. Find:
# - Union
# - Intersection
# - Difference
set_for_A = {1, 2, 3, 4}
set_for_B = {3, 4, 5, 6}
print(set_for_A.union(set_for_B))
print(set_for_A.intersection(set_for_B))
print(set_for_A.difference(set_for_B))

# Q6. Check whether {1,2} is a subset of {1,2,3,4}.
set_for_q6_small = {1, 2}
set_for_q6_big = {1, 2, 3, 4}
print(set_for_q6_small.issubset(set_for_q6_big))

# Q7. Check whether {1,2,3,4} is a superset of {1,2}.
set_for_q7_big = {1, 2, 3, 4}
set_for_q7_small = {1, 2}
print(set_for_q7_big.issuperset(set_for_q7_small))

# Q8. Create two sets {1,2} and {3,4} and check if they are disjoint.
set_for_q8_1 = {1, 2}
set_for_q8_2 = {3, 4}
print(set_for_q8_1.isdisjoint(set_for_q8_2))

# Q9. Convert a list [1,2,2,3,4,4,5] into a set and display unique values.
list_for_q9 = [1, 2, 2, 3, 4, 4, 5]
set_for_q9 = set(list_for_q9)
print(set_for_q9)

# Q10. Find the length of a set {10,20,30,40,50}.
set_for_q10 = {10, 20, 30, 40, 50}
print(len(set_for_q10))


# Assignment Questions on Dictionary (10)

# Q1. Create a dictionary with keys: name, age, city and assign some values. Print the dictionary.
dictionary_for_q1 = {"name": "Aman", "age": 20, "city": "Indore"}
print(dictionary_for_q1)

# Q2. Access the value of key "age" from dictionary {"name":"Akanksha", "age":25, "city":"Pune"}.
dictionary_for_q2 = {"name": "Akanksha", "age": 25, "city": "Pune"}
print(dictionary_for_q2["age"])

# Q3. Add a new key-value pair "course":"Python" in the dictionary.
dictionary_for_q3 = {"name": "Akanksha", "age": 25, "city": "Pune"}
dictionary_for_q3["course"] = "Python"
print(dictionary_for_q3)

# Q4. Update the value of "city" to "Mumbai" in dictionary {"name":"Rohan", "city":"Pune"}.
dictionary_for_q4 = {"name": "Rohan", "city": "Pune"}
dictionary_for_q4["city"] = "Mumbai"
print(dictionary_for_q4)

# Q5. Delete the key "age" from dictionary {"name":"Disha", "age":22, "city":"Nashik"}.
dictionary_for_q5 = {"name": "Disha", "age": 22, "city": "Nashik"}
del dictionary_for_q5["age"]
print(dictionary_for_q5)

# Q6. Write a program to get all the keys of dictionary {"a":1, "b":2, "c":3}.
dictionary_for_q6 = {"a": 1, "b": 2, "c": 3}
print(dictionary_for_q6.keys())

# Q7. Write a program to get all the values of dictionary {"a":1, "b":2, "c":3}.
dictionary_for_q7 = {"a": 1, "b": 2, "c": 3}
print(dictionary_for_q7.values())

# Q8. Merge two dictionaries: d1 = {"a":1, "b":2} and d2 = {"c":3, "d":4} using update method.
dictionary_for_d1 = {"a": 1, "b": 2}
dictionary_for_d2 = {"c": 3, "d": 4}
dictionary_for_d1.update(dictionary_for_d2)
print(dictionary_for_d1)

# Q9. Write a program to access the value of "fees" from the above dictionary.
student = {
    "name": "Akanksha",
    "course": {
        "name": "Python",
        "duration": "3 months",
        "fees": 10000
    }
}
print(student["course"]["fees"])

# Q10. Update the "department" of the employee from "IT" to "HR".
company = {
    "employee": {
        "id": 101,
        "name": "Rohan",
        "department": "IT"
    }
}
company["employee"]["department"] = "HR"
print(company)
