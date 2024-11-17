#del keyword 
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("ayesha")
print(s1.name)
print("Del keyword came")
del s1
print(s1) # name 's1' is not defined because del keyword was deleted
print("Deleted the student name")
print(s1.name)