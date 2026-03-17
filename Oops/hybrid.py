class A:
    def __init__(self,a):
        self.a = a

    def displayA(self):
        
        print("This is a class A")
class B(A):
    def displayB(self,a,b):
        super().__init__(a)
        self.b=b
        print("This is a class B")
class C:
    def displayC(self,c):
        self.c=c
        print("This is a class C",self.c)
class D(C,B):
    def __init__(self,a,b,c,d):
        B._init__(self,a,b)
        C.__init__(self,c)
        self.d = d

    def displayD(self):
        print("This is a class D")


d1 = D(10,20,30,40)
d1.displayA()
d1.displayB()
d1.displayC()
d1.displayD()