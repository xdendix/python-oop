from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Cat(Animal):
    def speak(self):
        print("Meow Meow")

    def eat(self):
        print("Nyam Nyam")


class Dog(Animal):
    def speak(self):
        print("Guk Guk")

    def eat(self):
        print("Nyam Nyam Nyam")
