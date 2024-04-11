# It prevents a user from creating an object of that class 
# and compels a user to override abstract methods in a child class

#  abstract class = a class which contains one or more abstract methods  abc= abstract base class 
# abstract method = a method that has a declaration but does not have an implementation 

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You are driving the car")

class Bike(Vehicle):
    def go(self):
        print("You are riding the bike")

#vehicle = Vehicle()            #can't intantiate abstract class 
car = Car()
bike = Bike()

#vehicle.go()
car.go()
bike.go()