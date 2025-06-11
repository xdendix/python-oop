class Omnivora:  # This class represents omnivorous animals
    def eat(self):  # This method simulates eating behavior
        print(f"{self.__class__.__name__} sedang makan")  # Prints the class name and action


class Carnovira:  # This class represents carnivorous animals
    def hunting(self):  # This method simulates hunting behavior
        print(f"{self.__class__.__name__} sedang berburu")  # Prints the class name and action


class Beruang(Omnivora, Carnovira):  # This class represents a bear, which is both omnivorous and carnivorous
    pass  # This class inherits from both Omnivora and Carnovira


beruang1 = Beruang()  # Create an instance of Beruang
beruang1.hunting()  # Call the hunting method from the Carnovira class
beruang1.eat()  # Call the eat method from the Omnivora class
