import calcimodule

print("Calculator:\n1.Addition.\n2.Subtraction.\n3.Product.\n4.Division.")

option = int(input("Enter an option : "))

if(option==1):
    print("Addition = ", calcimodule.add(10,9))
elif(option==2):
    print("Subtraction = ", calcimodule.sub(56,92))
elif(option==3):
    print("Product = ", calcimodule.product(8,6))
elif(option==4):
    print("Div = ", calcimodule.div(56,2))