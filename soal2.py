# Fungsi untuk menginput data barang
def tambah_barang(inventaris):
    nama_barang = input("Masukkan nama barang: ")
    kode_barang = input("Masukkan kode barang: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    inventaris.append({"nama": nama_barang, "kode": kode_barang, "jumlah": jumlah_barang})
    print("Barang berhasil ditambahkan!")

# Fungsi untuk menampilkan semua barang
def tampilkan_barang(inventaris):
    print("Daftar Barang:")
    for barang in inventaris:
        print(f"Nama: {barang['nama']}, Kode: {barang['kode']}, Jumlah: {barang['jumlah']}")

# Fungsi untuk mencari barang berdasarkan kode
def cari_barang(inventaris, kode):
    for barang in inventaris:
        if barang['kode'] == kode:
            print(f"Nama: {barang['nama']}, Kode: {barang['kode']}, Jumlah: {barang['jumlah']}")
            return
    print("Barang tidak ditemukan!")

# Fungsi untuk menghapus barang berdasarkan kode
def hapus_barang(inventaris, kode):
    for barang in inventaris:
        if barang['kode'] == kode:
            inventaris.remove(barang)
            print("Barang berhasil dihapus!")
            return
    print("Barang tidak ditemukan!")

# Main program
inventaris = []

while True:
    print("=== Aplikasi Inventaris Barang ===")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Cari Barang")
    print("4. Hapus Barang")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == "1":
        tambah_barang(inventaris)
    elif pilihan == "2":
        tampilkan_barang(inventaris)
    elif pilihan == "3":
        kode_barang = input("Masukkan kode barang yang ingin dicari: ")
        cari_barang(inventaris, kode_barang)
    elif pilihan == "4":
        kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
        hapus_barang(inventaris, kode_barang)
    elif pilihan == "5":
        break
    else:
        print("Pilihan tidak valid!")

print("Terima kasih telah menggunakan aplikasi ini!")