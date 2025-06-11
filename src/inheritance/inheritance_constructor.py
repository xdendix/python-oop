class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Cat(Animal):
    # modifikasi konstruktor untuk menerima parameter tambahan
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Memanggil konstruktor kelas induk
        self.color = color


c1 = Cat("Garfield", 5, "Orange")
c1.display()
