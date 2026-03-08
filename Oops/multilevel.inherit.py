'''
multilevel - one child class inherits from parent class, parent class inherits from grand parent

GP -> P ->c

'''

class GrnadParent:
    def show_gp(self):
        print("This is GrnadParent class.")

class Parent(GrnadParent):
    def show_parent(self):
        print(" This is Parent class.")

class Child(Parent):
    def show_child(self):
        print("This is Child class.")


c=Child()
c.show_child()
c.show_gp()
c.show_parent()


#example :- 

class Student:
    def __init__(self,name):
        self.name= name
    def studentInfo(self):
        print("student name :", self.name)

class Exam(Student):
    def __init__(self,name,mark1,mark2,mark3):
        super().__init__(name)
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3

    def total_marks(self):
        total = self.mark1+self.mark2+self.mark3
        return total

#child 

class Result(Exam):
    def __init__(self, name, mark1, mark2, mark3):
        super().__init__(name,mark1, mark2, mark3)
    
    def result(self):
        total=super().total_marks()
        avg=total/3
        if(avg>=75):
            print("student is passed with distinction")
        elif(avg>=40 and avg<75):
            print("student is passed")
        else:
            print("student is failed")

s1=Result("vaish",10,20,35)
s1.studentInfo()
print(s1.total_marks())
s1.result()

