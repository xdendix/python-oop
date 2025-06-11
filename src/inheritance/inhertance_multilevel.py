class Animal:
    def eat(self):
        print(f"{self.__class__.__name__} sedang makan")


class Omnivora(Animal):
    def hunting(self):
        print(f"{self.__class__.__name__} sedang berburu")


class Tiger(Omnivora):
    pass


t1 = Tiger()
t1.hunting()
t1.eat()
