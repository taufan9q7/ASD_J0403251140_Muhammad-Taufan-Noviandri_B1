# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Muhammad Taufan Noviandri
# NIM     : J0403251140
# Kelas   : TPL B1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1)
nama_file = "data_mahasiswa.txt"

def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}  # buat dictionary kosong untuk menampung data buku
    with open("buku.txt", "r", encoding="utf-8") as file:  # buka file mode baca
            for baris in file:  # baca file satu baris per satu baris
                baris = baris.strip()  # hapus spasi/enter di ujung baris
                if baris == "":
                    continue  # lewati jika baris kosong
                kode_buku, judul, harga = baris.split(",")  # pisah baris berdasarkan koma jadi 3 variabel

                # simpan ke dictionary, kode_buku = KEY, judul & harga = VALUE
                database_buku[kode_buku] = {
                    "judul": judul,
                    "harga": int(harga)  # konversi harga dari string ke integer
                }
    return database_buku  # kembalikan dictionary yang sudah terisi

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2)
# Linked List = kumpulan node yang saling terhubung: [Node1] -> [Node2] -> [Node3] -> None
class Node:
    def __init__(self, judul):
        self.judul = judul      # data yang disimpan di node ini
        self.berikut = None     # pointer ke node berikutnya, default None (belum terhubung)

class LinkedListPromosi:
    def __init__(self):
         self.head = None  # head = pintu masuk linked list, None berarti list masih kosong

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        Node_baru = Node(judul)  # buat node baru berisi judul buku

        if self.head is None:
            self.head = Node_baru  # jika list kosong, node baru langsung jadi head
        else:
            node_saat_ini = self.head  # mulai penelusuran dari head
            while node_saat_ini.berikut is not None:    # terus jalan sampai node terakhir (yang berikut = None)
                node_saat_ini = node_saat_ini.berikut
            node_saat_ini.berikut = Node_baru           # sambungkan node terakhir ke node baru

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        if self.head is None:
            print("Daftar promosi kosong.")
            return
        node_saat_ini = self.head  # mulai dari node pertama (head)
        nomor = 1
        while node_saat_ini is not None:  # loop sampai node habis (None)
            print(f"  {nomor}. {node_saat_ini.judul}")
            node_saat_ini = node_saat_ini.berikut  # pindah ke node berikutnya
            nomor += 1

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3)
# Yang pertama masuk = yang pertama dilayani, seperti antrian kasir
class AntreanKasir:
    def __init__(self):
        self.antrean = []  # list kosong sebagai wadah antrian

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue) - masuk dari belakang"""
        self.antrean.append(nama_pelanggan)  # append = tambah ke belakang list (prinsip FIFO)
        print(f"'{nama_pelanggan}' masuk antrean. Antrean: {self.antrean}")

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue) - keluar dari depan"""
        if len(self.antrean) == 0:
            print("Antrean kosong!")
        else:
            dilayani = self.antrean.pop(0)  # pop(0) = ambil dan hapus elemen paling depan (prinsip FIFO)
            print(f"Melayani: '{dilayani}'. Sisa antrean: {self.antrean}")

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4)
# Insertion Sort = seperti mengurutkan kartu, ambil satu elemen lalu sisipkan ke posisi yang benar
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan Insertion Sort.
    """
    data = list_harga.copy()  # salin list agar data asli tidak ikut berubah

    for i in range(1, len(data)):  # mulai dari elemen ke-2, elemen pertama dianggap sudah urut
        kunci = data[i]  # simpan elemen yang sedang ingin disisipkan ke posisi yang benar
        j = i - 1  # mulai bandingkan dari elemen sebelah kiri kunci
        while j >= 0 and data[j] > kunci:  # selama elemen kiri lebih besar dari kunci, geser ke kanan
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = kunci  # sisipkan kunci ke posisi yang tepat

    return data  # kembalikan list yang sudah terurut dari kecil ke besar

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)  # muat data buku dari file ke dictionary
    list_promosi = LinkedListPromosi()   # buat linked list kosong untuk promosi
    antrean_toko = AntreanKasir()        # buat antrian kosong untuk kasir
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]  # data harga transaksi

    while True:  # loop terus sampai user pilih keluar
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")  # minta input pilihan dari user

        if pilihan == '1':
            print("\n===== Katalog Buku =====")
            for kode, info in data_buku.items():  # loop setiap isi dictionary
                print(f"Kode  : {kode}")
                print(f"Judul : {info['judul']}")
                print(f"Harga : Rp {info['harga']:,}") 
                print("--------------------")
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)  # tambah buku ke linked list
            list_promosi.tampilkan_promosi()              # tampilkan semua isi linked list

        elif pilihan == '3':
            print("a. Tambah pelanggan")
            print("b. Layani pelanggan")
            sub = input("Pilih (a/b): ")  # minta input sub menu dari user

            if sub == 'a':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)   # masukkan pelanggan ke antrian
            elif sub == 'b':
                antrean_toko.layani_pelanggan()     # layani pelanggan paling depan, lalu hapus dari antrian
            else:
                print("Pilihan tidak valid!")

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)  # urutkan dengan insertion sort
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break  # keluar dari loop while

        else:
            print("Pilihan tidak valid!")  # jika input bukan angka 1-5

if __name__ == "__main__":
    main()  # jalankan program utama