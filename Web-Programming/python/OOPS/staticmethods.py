#Static methods 
#Methods that don't use the self parameter (work at class level)class Student:
#which change the behaviour of original functions


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("Harry", [99,98,97])
s1.get_avg()
s1.hello()