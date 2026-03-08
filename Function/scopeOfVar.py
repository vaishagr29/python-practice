'''
scope - it is a region in program where your variable can be accessed and modified.

2 types:

local scope(local variable) : it is defined inside function, scope is within function only. 

global scope(global variable) : it is defined outside function,

and its scope is anywhere through out program.

'''

#local variable

def local_var():
    a=67
    print("inside fun ",a)

local_var()

b=78

def global_var():
    print("inside fun ",b)
print()

global_var()
print("outdie fun ",b)