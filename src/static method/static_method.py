class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil.")


Mobil.intro_mobil()
mobil_1 = Mobil("Jaguar")
mobil_1.intro_mobil()
