'''
Problem Statement: School Management System

A School Management System needs to store information about a student's parents and the student.

A Father class stores the father's details.
A Mother class stores the mother's details.
A Child class should inherit information from both Father and Mother and also store the child’s details.
The system should:

Store the father's name.
Store the mother's name.
Store the child's name.
Display all the information using different methods.

'''
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

'''

Problem Statement: Smart Device System

A company is designing a Smart Device System.

A Camera class provides camera features.
A MusicPlayer class provides music playing features.
A SmartPhone class should inherit features from both Camera and MusicPlayer.
The system should allow the smartphone to:

Take photos using camera functionality.
Play music using music player functionality.
Store the smartphone model name.
Since the SmartPhone needs features from both Camera and MusicPlayer, we use multiple inheritance.


'''

class Camera:
    def __init__(self,c):
        pass
    def Take_photo():
        print("Photo has been taken")

class MusicPlayer:
    def __init__(self):
        pass
    def Play_audio():
        print("audio Played")


class SmartPhone(Camera, MusicPlayer):
    def __init__(self):
        pass
    def Take_photo():




