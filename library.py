import time

buku = []

while True:
    print("=" * 15, "PERPUSTAKAAN SEDERHANA", "=" * 15)
    print("1.Lihat Buku")
    print("2.Tambah Buku")
    print("3.Hapus Buku")
    print("4.Keluar Perpustakaan")
    pilihan_pengguna = input("Masukkan Pilihan Anda: ").lower()
    if pilihan_pengguna not in [
        "1", "lihat buku",
        "2", "tambah buku",
        "3", "hapus buku",
        "4", "keluar perpustakaan"
    ]:
        print("Pilihan Tidak Valid, Harap Memasukkan Pilihan Yang Valid!!")
        continue
    else:
        if pilihan_pengguna in [
            "4", "keluar perpustakaan"
        ]:
            print("Terima Kasih Telah Memakai Perpustakaan Kami:D")
            time.sleep(2)
            break
        elif pilihan_pengguna in [
            "1", "lihat buku"
        ]:
            if not buku :
                print("Belum Ada Buku Yang Ditambahkan")
            else:
                for i in range(len(buku)) :
                    print(i + 1,".", buku[i])
        elif pilihan_pengguna in [
            "2", "tambah buku"
        ]:
            tambah_buku = input("Masukkan Nama Buku: ")
            buku.append(tambah_buku)
            print("YEY! Berhasil Menambahkan Buku:D")
            time.sleep(2)
        elif pilihan_pengguna in [
            "3", "hapus buku"
        ]:
            if not buku :
                print("Tidak Ada Buku Yang Ingin Dihapus")
            else:
                hapus_buku = int(input("Masukkan Nomor Buku Yang Anda Ingin Hapus: "))
                if 1 <= hapus_buku <= len(buku) :
                    buku.pop(hapus_buku - 1)
                    print("YEY!! Buku Berhasil Dihapus:D")
                    time.sleep(1)
                else:
                    print("Nomor Buku Tidak Tersedia")
                    time.sleep(1)