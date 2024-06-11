transaksi = []

def tambah_transaksi(tipe, jumlah):
    transaksi.append((tipe, jumlah))

def tampilkan_transaksi():
    for tipe, jumlah in transaksi:
        print(f"Tipe: {tipe}, Jumlah: {jumlah}")

def hitung_total_pemasukan():
    total_pemasukan = sum(jumlah for tipe, jumlah in transaksi if tipe == 'pemasukan')
    print(f"Total Pemasukan: {total_pemasukan}")

def hitung_total_pengeluaran():
    total_pengeluaran = sum(jumlah for tipe, jumlah in transaksi if tipe == 'pengeluaran')
    print(f"Total Pengeluaran: {total_pengeluaran}")

def hitung_saldo_akhir():
    total_pemasukan = sum(jumlah for tipe, jumlah in transaksi if tipe == 'pemasukan')
    total_pengeluaran = sum(jumlah for tipe, jumlah in transaksi if tipe == 'pengeluaran')
    saldo_akhir = total_pemasukan - total_pengeluaran
    print(f"Saldo Akhir: {saldo_akhir}")

tambah_transaksi('pemasukan', 1000000)
tambah_transaksi('pengeluaran', 500000)
tambah_transaksi('pengeluaran', 200000)
tampilkan_transaksi()
hitung_total_pemasukan()
hitung_total_pengeluaran()
hitung_saldo_akhir()
def menu():
    while True:
        print("=== MENU ===")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Semua Transaksi")
        print("3. Hitung Total Pemasukan")
        print("4. Hitung Total Pengeluaran")
        print("5. Hitung Saldo Akhir")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            tipe = input("Masukkan tipe transaksi (pemasukan/pengeluaran): ")
            jumlah = int(input("Masukkan jumlah transaksi: "))
            tambah_transaksi(tipe, jumlah)
        elif pilihan == '2':
            tampilkan_transaksi()
        elif pilihan == '3':
            hitung_total_pemasukan()
        elif pilihan == '4':
            hitung_total_pengeluaran()
        elif pilihan == '5':
            hitung_saldo_akhir()
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()