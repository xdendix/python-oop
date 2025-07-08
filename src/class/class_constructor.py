class Mobil:
    # atribut instance
    def __init__(self):
        self.warna = "Merah"


mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# mengubah atribut instance
mobil_1.warna = "Hitam"

print(mobil_1.warna)
print(mobil_2.warna)
