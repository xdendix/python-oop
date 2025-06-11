class Car:
    def __init__(self, wheels):  # Constructor with parameter
        self.wheels = wheels  # Assigning the parameter to an instance variable
        print(f"Jumlah roda: {self.wheels}")  # This will print the number of wheels when a Car object is created


car1 = Car(4)  # This will call the constructor with 4 wheels
