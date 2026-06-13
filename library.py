import time

buku = []


"""TAMPILAN MENU PERPUSTAKAAN"""
def menu_library():
    while True:
        print("=" * 30, "PERPUSTAKAAN SEDERHANA", "=" * 30)
        print("1.Lihat Buku")
        print("2.Tambah Buku")
        print("3.Hapus Buku")
        print("4.Cari Buku")
        print("5.Keluar Perpustakaan")
        pilihan_pengguna = input("Masukkan Pilihan Anda: ").lower()
        if pilihan_pengguna not in [
            "1", "lihat buku",
            "2", "tambah buku",
            "3", "hapus buku",
            "4", "cari buku",
            "5", "keluar perpustakaan"
        ]:
            print("Pilihan Tidak Valid!!")
            continue
        else:
            if pilihan_pengguna in ["5", "keluar perpustakaan"]:
                print("Terima Kasih Telah Menggunakan Perpustakaan Kami:D")
                time.sleep(1)
                break
            elif pilihan_pengguna in ["1", "lihat buku"]:
                lihat_buku()
            elif pilihan_pengguna in ["2", "tambah buku"]:
                tambah_buku()
            elif pilihan_pengguna in ["3", "hapus buku"]:
                hapus_buku()
            elif pilihan_pengguna in ["4", "cari buku"]:
                mencari()





"""TAMPILAN MENU UNTUK MELIHAT BUKU"""
def lihat_buku():
    if not buku:
        print("Belum Ada Buku Yang Ditambahkan")
    else:
        for i in range(len(buku)):
            print(i + 1,".", buku[i])

"""TAMPILAN MENU UNTUK MENAMBAH BUKU"""
def tambah_buku():
    nama_buku = input("Masukkan Nama Buku: ")
    print("YEY!! Berhasil Menambahkan Buku")
    time.sleep(1)
    buku.append(nama_buku)

"""TAMPILAN MENU UNTUK MENGHAPUS BUKU"""
def hapus_buku():
    if not buku:
        print("Tidak Ada Buku Yang Ingin Dihapus!!")
    else:
        hapus = int(input("Masukkan Nomor Buku Yang Anda Ingin Hapus: "))
        if 1 <= hapus <= len(buku):
            buku.pop(hapus - 1)
            print("YEY!! Berhasil Menghapus Buku")
            time.sleep(1)
        else:
            print("Nomor Buku Tidak Tersedia")
            time.sleep(1)

"""TAMPILAN MENU UNTUK MENCARI BUKU"""
def mencari():
    cari_buku = input("Masukkan Nama Buku: ")
    ditemukan = False
    for i in range(len(buku)):
        if buku[i] == cari_buku:
            ditemukan = True
            print("YEY!! Buku Yang Dicari Ditemukan:D")
            print("Nomor buku", i + 1)
            break
    if not ditemukan:
        print("Buku Yang Anda Cari Tidak Ditemukan")

"""TEMPAT PROSES DATA"""
menu_library()