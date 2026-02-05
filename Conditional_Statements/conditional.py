
# conditional statement - these are the statements which executes a block of code on the basis of condition applied.
# 1. if
# 2. if else
# 3. if elif else
# 4. nested if else
# 5. match case

'''
if statement
Syntax
if(condition):
#block of code
'''

x =23
if(x<50):
    print("is greater.")

#age criteria
age= int(input("Enter hge to check eligibility :"))
if(age>=18):
    print("can vote.")

'''
if else 
Syntax
if(condion):
    #code
else:
    #code
'''
#indentation

x=23
if(x>50):
    print("is greater.")
else:
    print("is not greater.")

# age criteria

age= int(input("enter age: "))
if(age>=18):
    print("can vote.")
else:
    print("cannot vote.")
