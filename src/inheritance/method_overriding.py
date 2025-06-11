class Animal:
    def speak(self):
        print("Speak from animal")


class Cat(Animal):  # Inheriting from Animal class
    def speak(self):  # Method overriding
        print("Speak from cat")


cat_1 = Cat()
cat_1.speak()  # Output: Speak from animal
