# ## non parameterized non return type 

# def void():
#     print("Non parameterized non return typed")

# ## parameterized non return type

# def paraNonRetType(a,b):
#     print("this is non return typed",a+b)

# ## non parameterized return typed
# def funcc():
#     return f"HELLO WORLD !!"

# ##parameterized return type
# #has parameters and returns a value
# def func(a,b):
#     return a+b


# void()
# paraNonRetType(5,6)
# print(funcc())
# print(func(5,3))

# def func(name="guest"):
#     print("Hello ", name)
# func()
# func("codenera")

# def func(a,b):
#     print("Hello ", a-b)
# func(b=2,a=4)

# def func(*a):
#     print(a)
# func(1,2,3)

def func(**a):
    pass
    print(a)
func(a=1,b=2,c=3)