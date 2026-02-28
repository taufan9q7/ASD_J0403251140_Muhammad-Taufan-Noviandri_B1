#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

#===========================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
#===========================================

# Kelas Node: Merepresentasikan satu elemen dalam linked list
class Node:
    def __init__(self, no, nama, servis):
        self.no = no           # Menyimpan nomor antrian
        self.nama = nama       # Menyimpan nama pelanggan
        self.servis = servis   # Menyimpan jenis servis
        self.next = None       # Pointer ke node berikutnya (default: None)

class QueueBengkel:
    def __init__(self):
        self.front = None      # Pointer ke elemen paling depan (untuk dequeue)
        self.rear = None       # Pointer ke elemen paling belakang (untuk enqueue)

    def is_empty(self):
        return self.front is None

    def enqueue(self, no, nama, servis):
        # 1) Buat node baru dengan data pelanggan
        node_baru = Node(no, nama, servis)
        
        # 2) Cek apakah queue kosong
        if self.is_empty():
            # Jika queue kosong, front dan rear sama-sama menunjuk ke node baru
            self.front = node_baru
            self.rear = node_baru
        else:
            # 3) Jika queue tidak kosong:
            # Hubungkan rear lama ke node baru (memasukkan di belakang)
            self.rear.next = node_baru
            # Update rear menunjuk ke node baru
            self.rear = node_baru
        
        print(f"Pelanggan {nama} dengan nomor antrian {no} telah ditambahkan.")

    # Method dequeue: Melayani dan menghapus pelanggan terdepan 
    def dequeue(self):
        # 1) Cek apakah queue kosong
        if self.is_empty():
            print("Antrian kosong, tidak ada pelanggan yang dapat dilayani.")
            return None
        
        # 2) Ambil data pelanggan paling depan (front)
        data_dilayani = self.front
        
        # 3) Simpan informasi pelanggan untuk ditampilkan
        no_terlayani = data_dilayani.no
        nama_terlayani = data_dilayani.nama
        servis_terlayani = data_dilayani.servis
        
        # 4) Geser front ke node berikutnya (mengahpus node terdepan)
        self.front = self.front.next
        
        # 5) Jika setelah geser front menjadi None, berarti queue kosong
        # maka rear juga harus di-set menjadi None
        if self.front is None:
            self.rear = None
        
        print(f"Pelanggan dilayani: No Antrian {no_terlayani}, Nama: {nama_terlayani}, Servis: {servis_terlayani}")
        return data_dilayani

    # Method tampilkan: Menampilkan seluruh antrian
    def tampilkan(self):
        # 1) Cek apakah queue kosong
        if self.is_empty():
            print("Antrian kosong.")
            return
        
        # 2) Traversal: Mulai dari front dan telusuri sampai akhir
        print("\n=== Daftar Antrian ===")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nama} - {current.servis}")
            current = current.next
            no += 1

# Fungsi main: Menu utama program
def main():
    q = QueueBengkel()  
    
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")
        pilih = input("Pilih menu: ")
        
        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)
            
        elif pilih == "2":
            q.dequeue()
            
        elif pilih == "3":
            q.tampilkan()
            
        elif pilih == "4":
            print("Terima kasih telah menggunakan sistem ini.")
            break
            
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()