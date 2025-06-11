class Mahasiswa:  # class
    nama = ""
    umur = 0
    jurusan = ""

    def membaca(self):  # method
        print(f"{self.nama} sedang membaca buku")


mhs1 = Mahasiswa()  # instance of Mahasiswa
mhs1.nama = "Budi"  # Assigning a name to the instance
mhs1.membaca()  # Output: mahasiswa sedang membaca buku

mhs1 = Mahasiswa()  # Creating another instance of Mahasiswa
mhs1.nama = "Siti"  # Assigning a different name to the new instance
mhs1.membaca()  # Output: Siti sedang membaca buku
