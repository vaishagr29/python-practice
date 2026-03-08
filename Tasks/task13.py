# def func(a,b=5):
#     return a*b
# print(func(3))

# def outer():
#     def inner():
#         return 5
#     return inner
# x=outer()
# print(x())

# def func(x=[]):
#     x.append(1)
#     return x
# print(func())
# print(func())

# x=10
# def fun():
#     x=20
#     return x
# print(fun(),x)


# def f():
#     yield from [1,2,3]
# # print(list(f()))

# def func():
#     return 1, 2, 3
# print(func())

nums=[1,2,3]
result=list(map(lambda x:x+2,nums))
print(result)