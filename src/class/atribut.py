class Mobil:
    warna = "Merah"


mobil_1 = Mobil()
print("mobil 1 = " + mobil_1.warna)

mobil_2 = Mobil()
print("mobil 2 = " + mobil_2.warna)

# mengubah atribut kelas
Mobil.warna = "Hitam"

print("mobil 1 = " + mobil_1.warna)
print("mobil 2 = " + mobil_2.warna)
