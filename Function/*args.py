def multiply(rgss,*args):
    product = 1

    for i in args:
        product = product * i

    print(args,"\n",rgss)
    return product

print(multiply(8,1,2,3,4,5,6))

# def mul(**args):
#     pro=1
#     for i in args:
#         pro = pro * i

#     print(args)
#     return pro
# print(mul(a=1,b=2))