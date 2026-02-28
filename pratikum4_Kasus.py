#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

#===========================================================
# Studi kasus : sistem antrian di layanan akademik
# implementasi dengan Queue =>
# Enqueue : memindahkan pointer rear (nambah data baru di belakang)
# Dequeue : memindahkan pointer front (hapus data di depan) 
# Front -> A -> B -> C -> Rear
#=========================================================

#  1) Medefinisikan class Node (unit dasar dari linked list)
# Node = satu elemen antrian yang menyimpan data mahasiswa
class Node:
    def __init__(self, nim, nama): # Konstruktor untuk inisialisasi node
        self.nim = nim   # Menyimpan NIM mahasiswa
        self.nama = nama # Menyimpan Nama Mahasiswa
        self.next = None # Pointer ke node berikutnya (default None = belum terhubung)

# 2) Mendefinisikan queue, terdiri dari front dan rear
# front = mahasiswa paling depan (akan dilayani dulu)
# rear  = mahasiswa paling belakang (yang terakhir masuk)
class queueAkademik:
    def __init__(self):
        self.front = None # Awal antrian
        self.rear = None  # Akhir antrian

    def is_empty(self):
        #Ketika queue kosong maka front = rear = none
        return self.front is None
    
    #Menambahkan data baru ke bagian belakang (rear)
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)  # membuat node baru berisi data mahasiswa

        #Jika data baru masuk daru queue yang kosong maka data baru = front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru   # rear lama menunjuk ke node baru
        self.rear = nodeBaru        # rear berpindah ke node baru

    # Menghapus dara paling depan (memberikan layanan akademik)
    def dequeue(self):                        
        if self.is_empty():
            print("Antrian Kosong. Tidak ada Mahasiswa yang dilayani")
            return None

        #lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        #jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None
    
        return node_dilayani  # mengembalikan data mahasiswa yang sudah dilayani

    def tampilkan(self):
        print("Daftar Antrian Mahasiswa (Front > Rear): ")
        current = self.front
        no = 1

        # menelusuri linked list dari depan ke belakang
        while current is not None:
            print(f"{no}. {current.nim} {current.nama}")
            current = current.next
            no += 1

#Program utama 
def main():
       
    #instantiasi queue
    q = queueAkademik()

    while True:
        print("====== SIstem Antrian Akademik =======")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih Menu (1-4): ").strip()
        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()

            q.enqueue(nim, nama)  # menambah mahasiswa ke antrian
            print("Mahasiswa berhasil ditambahkan ke antrian.")

        elif pilihan == "2":
            dilayani = q.dequeue()  # melayani mahasiswa paling depan
            if dilayani:
                print(f"Mahasiswa yang dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()  # menampilkan isi antrian saat ini

        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break    
        else:
            print("Pilihan tidak valid. Silakan coba lagi 1-4.")

#penanda untuk menjalankan program utama
if __name__ == "__main__":
    main()