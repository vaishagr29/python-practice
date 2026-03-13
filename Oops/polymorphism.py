class Calculator:
    def add(self,a,b=0,c=0):
        return a+b+c

cal = Calculator()
print(cal.add(2))
print(cal.add(2,3))
print(cal.add(2,2,2))

# class Calculator:
#     def add(elf,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
    
# c=Calculator
# print(c.add(10,20))
# print(c.add(10,10,10))
