class Animal:
    color = ""

    def eat(self):
        print(f"{self.__class__.__name__} sedang makan")


class Cat(Animal):
    def speak(self):
        print("Meow Meow")


c1 = Cat()
c1.color = "Hitam"
c1.eat()
c1.speak()
