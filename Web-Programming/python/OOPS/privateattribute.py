class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #make the attribute account password private
        #it can be access within the class but cannot be access outside the class

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")
print(acc1.acc_no)
#print(acc1.__acc_pass)
print(acc1.reset_pass())


#new class
class Person:
    __name = "anonymous" #if we make the attribute private then within class methods can used them but cannot used outside class

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())
