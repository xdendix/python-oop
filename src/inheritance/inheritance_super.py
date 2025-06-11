class Animal:
    color = "Orange"  # Atribut kelas

    def sleep(self):  # Method sleep pada kelas Animal
        print(f"{self.__class__.__name__} sedang tidur")  # Menggunakan __class__.__name__ untuk mendapatkan nama kelas


class Cat(Animal):  # Kelas Cat mewarisi dari kelas Animal
    def display(self):  # Method display pada kelas Cat
        super().sleep()  # Memanggil method sleep dari kelas Animal
        print(f"Cat berwarna {self.color}")  # Akses atribut kelas dari kelas induk


animal_1 = Cat()  # Membuat objek dari kelas Cat
animal_1.display()  # Output: Cat sedang tidur dan Cat berwarna Orange
