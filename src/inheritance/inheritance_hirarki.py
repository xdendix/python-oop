class Animal:
    def eat(self):
        print(f"{self.__class__.__name__} sedang makan")


class Cat(Animal):
    pass


class Dog(Animal):
    pass


animal1 = Cat()
animal2 = Dog()

animal1.eat()
animal2.eat()
