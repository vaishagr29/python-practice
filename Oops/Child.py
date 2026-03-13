class Father:
    def __init__(self,fname):
        self.fname=fname

    def Father_info(self):
        print("This is Father class ",self.fname)
class Mother:
    def __init__(self,mname):
        self.mname=mname

    def Mother_info(self):
        print("This is Mother class ",self.mname)

class Child(Mother,Father):
    def __init__(self, cname, mname, fname):
        super().__init__(mname)
        Father.__init__(self, fname)
        self.cname = cname
    def child_info(self):
        print("This is child class ",self.cname)


c= Child("Ganesh", "Parvati", "Shiv")
c.child_info()
c.Father_info()
c.Mother_info()