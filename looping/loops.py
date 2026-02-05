'''
Docstring for looping.loops

looping - to repeat a block of code muliple times till a certain condition is met.
use - to repeat a code and to iterate over a sequence
Types : 
for loop - it executes a block of code repeatedly till a fixed number of times.
use - it is used when the number iterations is known(fixed/sequence based)
Syntax : 
for i in range():
    # block of code
    
range() - sequence of numbers
i - iterator
while loop - it executes a block of code repeatedly till the condition is True
use - its is used when the number of iterations in unknown(condition based)
Syntax : 
i = 0       # start/initialization
while(condition):
    # code
    increment/decrement



'''
#range()
#syntax : range(start, stop, step) - stop is excluded

numbers = range(1,11)
print(list(numbers))

#display 1-10
for i in range(1,11):
    print(i,end=" ")

print()
# display even number from 0-20
for i in range(0,21,2):
    print(i, end=" ")
print()
#if not intialize start by default it eill start from zero

for i in range(11):
    print(i)

print()

#display hi 5 times

for i in range(5):
    print("hi")
print()