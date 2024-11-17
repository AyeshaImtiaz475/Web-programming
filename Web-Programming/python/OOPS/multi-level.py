# Multi-level inheritance

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car): #inheritance
    def __init__(self,name):
        self.name = name

class Fortuner(ToyotaCar): #inheritance
    def __init_(self,type): #type of car
        self.type = type

car1 = Fortuner("diesel")
car1.start()
car1.stop()