class Mobil:
    def __init__(self, warna, merk, kecepatan):
        self.warna = warna
        self.merk = merk
        self.kecepatan = kecepatan


mobil_1 = Mobil("Merah", "Ferari", 3000)

print(mobil_1.warna)
print(mobil_1.merk)
print(mobil_1.kecepatan)
