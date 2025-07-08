class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def into_mobil(cls):
        print("Ini adalah metode dari kelas Mobil.")


Mobil.into_mobil()
mobil_1 = Mobil("Jaguar")
mobil_1.into_mobil()
