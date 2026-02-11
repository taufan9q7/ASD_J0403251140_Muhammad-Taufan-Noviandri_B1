# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Muhammad Taufan Noviandri
# NIM : J0403251140
# Kelas : TPL - B1
# ==========================================================

# ===============================
# Program Manajemen Stok Kantin
# ===============================

# Nama file data stok
NAMA_FILE = "stok_barang.txt"


# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Data disimpan ke dictionary.
    """
    stok_dict = {}

    try:
        # Membuka file dalam mode baca
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                # Menghilangkan spasi dan enter
                baris = baris.strip()

                # Jika baris kosong, dilewati
                if baris == "":
                    continue

                # Memisahkan data berdasarkan koma
                data = baris.split(",")

                # Validasi jumlah kolom harus 3
                if len(data) != 3:
                    continue  # Lewati baris yang formatnya salah

                kode = data[0]
                nama = data[1]

                # Mengubah stok menjadi integer
                try:
                    stok = int(data[2])
                except ValueError:
                    continue  # Jika stok bukan angka, lewati

                # Simpan ke dictionary
                stok_dict[kode] = {
                    "nama": nama,
                    "stok": stok
                }

    except FileNotFoundError:
        # Jika file tidak ditemukan
        print("File stok tidak ditemukan. Stok dimulai dari kosong.")

    return stok_dict


# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    """
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in stok_dict:
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode},{nama},{stok}\n")


# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan seluruh data stok barang.
    """
    if len(stok_dict) == 0:
        print("Stok barang kosong.")
        return

    print("\nKODE     | NAMA BARANG | STOK")
    print("-" * 30)

    for kode in stok_dict:
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<8} | {nama:<11} | {stok}")


# -------------------------------
# Fungsi: Cari barang
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode.
    """
    kode = input("Masukkan kode barang: ").strip()

    if kode in stok_dict:
        print("Barang ditemukan:")
        print("Kode :", kode)
        print("Nama :", stok_dict[kode]["nama"])
        print("Stok :", stok_dict[kode]["stok"])
    else:
        print("Barang tidak ditemukan.")


# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambahkan barang baru ke stok.
    """
    kode = input("Masukkan kode barang baru: ").strip()

    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    nama = input("Masukkan nama barang: ").strip()

    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Input stok harus berupa angka.")
        return

    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print("Barang berhasil ditambahkan.")


# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Menambah atau mengurangi stok barang.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambahkan.")

    elif pilihan == "2":
        stok_dict[kode]["stok"] -= jumlah

        # Jika stok negatif, otomatis jadi 0
        if stok_dict[kode]["stok"] < 0:
            stok_dict[kode]["stok"] = 0

        print("Stok berhasil dikurangi.")

    else:
        print("Pilihan tidak valid.")


# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data saat program dijalankan
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            # Simpan otomatis saat keluar
            simpan_stok(NAMA_FILE, stok_barang)
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Menjalankan program utama
if __name__ == "__main__":
    main()
