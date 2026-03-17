
globalVar=10

def test():
    localVar=9

    return localVar

print("local variable = ",test())
print("global variable = ",globalVar)
