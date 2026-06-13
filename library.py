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
        print("5.Edit Buku")
        print("6.Statistik Perpustakaan")
        print("7.Keluar Perpustakaan")
        pilihan_pengguna = input("Masukkan Pilihan Anda: ").lower()
        if pilihan_pengguna not in [
            "1", "lihat buku",
            "2", "tambah buku",
            "3", "hapus buku",
            "4", "cari buku",
            "5", "edit buku",
            "6", "statistik perpustakaan",
            "7", "keluar perpustakaan"
        ]:
            print("Pilihan Tidak Valid!!")
            continue
        else:
            if pilihan_pengguna in ["7", "keluar perpustakaan"]:
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
            elif pilihan_pengguna in ["5", "edit buku"]:
                edit()
            elif pilihan_pengguna in ["6", "statistik perpustakaan"]:
                statistik_perpustakaan()





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
    while True:
        if not buku:
            print("Tidak Ada Buku Yang Ingin Dihapus!!")
            break
        else:
            try:
                hapus = int(input("Masukkan Nomor Buku Yang Anda Ingin Hapus: "))
                if 1 <= hapus <= len(buku):
                    buku.pop(hapus - 1)
                    print("YEY!! Berhasil Menghapus Buku:D")
                    time.sleep(1)
                    break
                else:
                    print("Nomor Buku Tidak Tersedia")
                    time.sleep(1)
            except ValueError:
                print("Harap Memasukkan Nomor Buku Yang Benar Yah:D")
                time.sleep(1)
                continue

"""TAMPILAN MENU UNTUK MENCARI BUKU"""
def mencari():
    cari_buku = input("Masukkan Nama Buku: ")
    ditemukan = False
    for i in range(len(buku)):
        if buku[i].lower() == cari_buku.lower():
            ditemukan = True
            print("YEY!! Buku Yang Dicari Ditemukan:D")
            print("Nomor buku", i + 1)
            break
    if not ditemukan:
        print("Buku Yang Anda Cari Tidak Ditemukan")

"""TAMPILAN MENU UNTUK MENGEDIT BUKU"""
def edit():
    while True:
        try:
            if not buku:
                print("Belum Ada Buku Yang ditambahkan")
                break
            else:
                nomor_buku_edit = int(input("Masukkan Nomor Buku Yang Anda Ingin Edit: "))
                judul_buku_edit = input("Masukkan Judul Buku Baru: ")
                if 1 <= nomor_buku_edit <= len(buku):
                    buku[nomor_buku_edit - 1] = judul_buku_edit
                    print("YEY!! Buku Berhasil Diperbarui")
                    break
                else:
                    print("Nomor Buku Tidak Tersedia")
                    continue
        except ValueError:
            print("Harap Memasukkan Nomor Buku Yang Benar!")
            continue

"""TAMPILAN MENU UNTUK MELIHAT STATISTIK PERPUSTAKAAN"""
def statistik_perpustakaan():
    print("=" * 30, "STATISTIK PERPUSTAKAAN", "=" * 30)
    print("Jumlah Buku:",len(buku))
    time.sleep(3)




"""TEMPAT PROSES DATA"""
menu_library()