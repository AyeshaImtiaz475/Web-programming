#automatically called when ever a class is called 
#__init__ 
#Constructor always take the arguments 
#self parametre is a reference 

class Student:
    college_name = "ABC college" # college name is same
    #default constructor 
    def __init__(self):
        pass

    #parameteized constructors
    def __init__(self, name, marks, exp):
        print(self)    #object = self 
        self.name = name #self.name = means that every student had the different marks and name
        self.marks = marks
        self.exp = exp
        print("Adding new student in Database...")

    #method
    def welcome(self):
        print("Welcome student,", self.name)

    def get_marks(self):
        return self.marks
    
    def get_experience(self):
        return self.exp


s1 = Student("ayesha", 98, 2)
print(s1.name, s1.marks)
s2 = Student("saba", 44, 3)
print(s2.name, s2.marks)

#same name of object and same name of class then the precedence of object is greater

print(s1.get_marks())
print(s1.get_experience())




