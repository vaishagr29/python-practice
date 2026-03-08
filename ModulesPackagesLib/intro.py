'''
Modules -  it is .py file which contains classes , functions, variables
which can be imported and used in another files
use - reusability , to main structure
'''

#custom module


# inbuilt modules
# os -interact with operating system
# math -numerical computation
import math
print("Square root of num: ", math.sqrt(49))
print("Factorial of number: ", math.factorial(5))
print("Power of num: ",math.pow(4,2))
print("pI value: ", math.pi)

'''
 
.randint() - returns any integer between given range.

.random() - gives any float value in the range [0.0, 1.0)

.choice() - picks one random item from list.

.shuffle() - changes the order of elements randomly

.sample() - do it

'''
import random
value = random.randint(10,61)
print(value)
data = random.random()
print(data)


data = random.random()
print(data)
data = ["red", "green","pink","yellow", "orange"]
value = random.choice(data)
print (value)
random.shuffle(data)
print(data)
# import time
# current time
import time
print("Current time: ",time.ctime())
# to pause the execution
print("Program is being paused.")
time.sleep(6)
print("Hello, I am back!!")

start_time = time.time()
total = sum(range(100000))
end_time = time.time()
print("Execution time = ", end_time-start_time)