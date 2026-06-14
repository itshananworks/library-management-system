import time




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
                lihat_buku(buku)
            elif pilihan_pengguna in ["2", "tambah buku"]:
                tambah_buku(buku)
            elif pilihan_pengguna in ["3", "hapus buku"]:
                hapus_buku(buku)
            elif pilihan_pengguna in ["4", "cari buku"]:
                mencari(buku)
            elif pilihan_pengguna in ["5", "edit buku"]:
                edit(buku)
            elif pilihan_pengguna in ["6", "statistik perpustakaan"]:
                statistik_perpustakaan(buku)



"""TEMPAT UNTUK MEMBUAT FILE BUKU"""
def simpan_buku(buku):
    file = open("data_buku.txt", "w")
    for judul in buku:
        file.write(judul + "\n")
    file.close()



def muat_buku():
    buku = []
    try:
        file = open("data_buku.txt", "r")
        for baris in file:
            buku.append(baris.strip())
        file.close()
    except FileNotFoundError:
        pass
    return buku

buku = muat_buku()

"""TEMPAT UNTUK MASUKKAN NOMOR BUKU"""
def input_nomor():
    try:
        nomor = int(input("Masukkan Nomor Buku: "))
        return nomor
    except ValueError:
        return None

"""TEMPAT UNTUK MEMASUKKAN JUDUL/NAMA BUKU"""
def input_judul_atau_nama_buku():
    nama_atau_judul = input("Masukkan Judul Buku/Nama Buku: ")
    return nama_atau_judul


"""TAMPILAN MENU UNTUK MELIHAT BUKU"""
def lihat_buku(buku):
    if not buku:
        print("Belum Ada Buku Yang Ditambahkan")
    else:
        for i in range(len(buku)):
            print(i + 1,".", buku[i])

"""TAMPILAN MENU UNTUK MENAMBAH BUKU"""
def tambah_buku(buku):
    nama_buku = input_judul_atau_nama_buku()
    buku.append(nama_buku)
    simpan_buku(buku)
    print("YEY!! Berhasil Menambahkan Buku")
    time.sleep(1)

"""TAMPILAN MENU UNTUK MENGHAPUS BUKU"""
def hapus_buku(buku):
    while True:
        if not buku:
            print("Tidak Ada Buku Yang Ingin Dihapus!!")
            time.sleep(1)
            break
        hapus = input_nomor()
        if hapus is None:
            print("Harap Memasukkan Nomor Buku Yang Benar Yah:D")
            time.sleep(1)
            continue
        if 1 <= hapus <= len(buku):
            buku.pop(hapus - 1)
            simpan_buku(buku)
            print("YEY!! Berhasil Menghapus Buku:D")
            time.sleep(1)
            break
        else:
            print("Nomor Buku Tidak Tersedia")

"""TAMPILAN MENU UNTUK MENCARI BUKU"""
def mencari(buku):
    cari_buku = input_judul_atau_nama_buku()
    ditemukan = False
    for i in range(len(buku)):
        if buku[i].lower() == cari_buku.lower():
            ditemukan = True
            print("YEY!! Buku Yang Dicari Ditemukan:D")
            print("Nomor buku", i + 1)
            break
    if not ditemukan:
        print("Buku Yang Anda Cari Tidak Ditemukan")
        time.sleep(1)

"""TAMPILAN MENU UNTUK MENGEDIT BUKU"""
def edit(buku):
    while True:
            if not buku:
                print("Belum Ada Buku Yang ditambahkan")
                time.sleep(1)
                break
            nomor_buku_edit = input_nomor()
            if nomor_buku_edit is None:
                print("Nomor Buku Tidak Tersedia, Harap Memasukkan Nomor Buku Yang Benar Yah:D")
                time.sleep(1)
                continue
            if 1 <= nomor_buku_edit <= len(buku):
                judul_buku_edit = input_judul_atau_nama_buku()
                buku[nomor_buku_edit - 1] = judul_buku_edit
                simpan_buku(buku)
                print("YEY!! Buku Berhasil Diperbarui:D")
                time.sleep(1)
                break
            else:
                print("Nomor Buku Tidak Tersedia!")

"""TAMPILAN MENU UNTUK MELIHAT STATISTIK PERPUSTAKAAN"""
def statistik_perpustakaan(buku):
    print("=" * 30, "STATISTIK PERPUSTAKAAN", "=" * 30)
    print("Jumlah Buku:",len(buku))
    time.sleep(3)




"""TEMPAT PROSES DATA"""
menu_library()