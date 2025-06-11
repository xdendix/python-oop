class Karyawan:
    def __init__(self, nama, umur, posisi):
        self.nama = nama
        self.umur = umur
        self.posisi = posisi

    def lihat_data(self):
        print(f"""
        Nama: {self.nama}
        Umur: {self.umur}
        Posisi: {self.posisi}
        """)


class KaryawanTetap(Karyawan):
    asuransi_pensiun = ""


class KaryawanKontrak(Karyawan):
    durasi_kontrak = 0


class KaryawanOutsourcing:
    vendor = ""


karyawan_kontrak = KaryawanKontrak("Dendi", 30, "Programmer")
karyawan_kontrak.lihat_data()
