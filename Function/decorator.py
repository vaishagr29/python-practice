'''
Decorator - is a function but basically it modifies the behaviour of the function woithout changing anything
without chnaging your actual code it modify your original function and return the updated decorated function
'''

#decorator function

# def decorator_function(function):
#     def inner_function():
#         #additional statement - to modify
#         print("This function is decorated.")
#         function()
#     return inner_function


# #original function

# def original():
#     print("this is original function.")

# decorator = decorator_function(original)
# decorator()


'''
write a py program using decorator to perform sub of two num
the decorator should check if the num is smaller than the second num - if so, it
should swap them before performing subtraction
display the result after subtraction.
'''



def decorator(function):
    def modified(A,B):
        if (A<B):
            A,B=B,A
        output =function(A,B)
        print(output)
    return modified

#original functiond

@decorator
def subtraction(a,b):
    ans=a-b
    return ans

subtraction(7,9)

# result=decorator(subtraction)
# print(result)
# result(7,9)

