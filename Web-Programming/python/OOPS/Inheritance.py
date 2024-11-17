#When one class(child/derived) derives the properties & methods of another class 

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car): #inheritance
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("perius")

print(car1.start())
print(car1.stop())
print(car1.color)


