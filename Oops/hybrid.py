class A:
    def displayA(self):
        print("This is a class A")
class B(A):
    def displayB(self):
        print("This is a class B")
class C:
    def displayC(self):
        print("This is a class C")
class D(C,B):
    def displayD(self):
        print("This is a class D")

        
d1 = D()
d1.displayA()
d1.displayB()
d1.displayC()
d1.displayD()