class StackPay:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    def deposit(self, jumlah_deposit):
        self.saldo += jumlah_deposit
        print("Deposit Berhasil!")

    def tarik_tunai(self, jumlah_tarik):
        if self.saldo >= jumlah_tarik:
            self.saldo -= jumlah_tarik
            print("Penarikan Berhasil!")
        else:
            print("Saldo tidak mencukupi untuk penarikan.")

    def cek_saldo(self):
        print(f"Nama pemilik: {self.nama}")
        print(f"Saldo saat ini: {self.saldo}")


account = None

while True:
    print("""
        == Selamat Datang di StackPay ==
            1. Buat Account
            2. Deposit
            3. Tarik Tunai
            4. Cek Saldo
            5. Keluar
        """)

    menu = int(input("Pilih menu: "))

    match menu:
        case 1:
            if account is not None:
                print("Account sudah dibuat.")
            else:
                nama = input("Masukkan nama pemilik: ")
                saldo_awal = float(input("Masukkan saldo awal: "))
                account = StackPay(nama, saldo_awal)
                print("Account berhasil dibuat.")
        case 2:
            if account is None:
                print("Buat akun terlebih dahulu.")
            else:
                jumlah_deposit = float(input("Masukkan jumlah deposit: "))
                account.deposit(jumlah_deposit)
        case 3:
            if account is None:
                print("Buat akun terlebih dahulu.")
            else:
                jumlah_tarik = float(input("Masukkan jumlah tarik tunai: "))
                account.tarik_tunai(jumlah_tarik)
        case 4:
            if account is None:
                print("Buat akun terlebih dahulu.")
            else:
                account.cek_saldo()
        case 5:
            print("Terima kasih telah menggunakan StackPay!")
            break
        case _:
            print("Menu tidak valid, silakan pilih menu yang tersedia.")
