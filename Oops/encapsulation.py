'''encapsulation wrapping up of your data members and member functions in single unit.
3
intro.py File handling
4
hiding of your data
'''
def _init__(self, name, id, location):
    self._emp_name= name
    self._emp_id = id
    self._location = location

# def displayInfo(self):

# print(self._emp_name, self._emp_id,self._location)

# setter and getter method to modify and access private data member outside class

def set_name(self, Name):
    self._emp_name = Name

def set_id(self, Id):
    self._emp_id = Id