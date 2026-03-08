'''
try-except-else

try:
    # code which may raise exception
except:
    # code which handles exception
else:
    # code executes if no error occurs

to seperate logical and normal code

'''

# Try-Except-Else-Finally 

# 9.  Ask user to enter a number. If valid integer(handle ValueError), print square inside else. Always print "Done" using finally.

try:
    num=int(input("enter a num"))
except ValueError as v:
    print(v)
else:
    print(num**2)
finally:
    print("done")



# 10. Take a string and check if it is a palindrome. If input is not a string (like list), handle TypeError.
def isPalindrome(word):
    return word == word[::-1]

try:
    s=input("enter a string")
except TypeError as t:
    print(t)
else:
    print(isPalindrome(s))
finally:
    print("done")

# 11. Input two numbers, divide them. If no error, print "Successful Division" in else. Always print "Program Completed" in finally.





