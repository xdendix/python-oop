class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


mobil_1 = Mobil("Hitam", "Mustang", 3000)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()  # Memanggil metode tambah kecepatan

print("Setelah ditambahkan: ")
print(mobil_1.kecepatan)
