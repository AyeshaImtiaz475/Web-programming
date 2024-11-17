
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car): #inheritance
    def __init__(self,name):
        #super keyword
        super().__init__(type) #super class -> constructor -> type access 
        self.name = name
        super().start()  #calling the parent class method through super method


car1 = ToyotaCar("prius", "electric")
print(car1.type)




