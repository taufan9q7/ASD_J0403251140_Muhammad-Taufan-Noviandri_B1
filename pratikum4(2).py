# ==========================================================
# Nama : Muhammad Taufan Noviandri
# NIM : J0403251140
# Kelas : TPL - B1
# ==========================================================

#===================================================
# Implementasi Dasar : Queue    
#===================================================

# Membuat class Node
class Node:
    def __init__(self, data):  # konstruktor
        self.data = data       # menyimpan nilai/data
        self.next = None       # pointer ke node berikutnya


# Queue dengan 2 pointer: front dan rear
class QueueLL:
    def __init__(self):
        self.front = None  # node paling depan
        self.rear = None   # node paling belakang

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        # menambah data ke rear (belakang)
        nodeBaru = Node(data)

        # jika queue kosong
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
        else:
            # rear lama menunjuk ke node baru
            self.rear.next = nodeBaru
            # rear pindah ke node baru
            self.rear = nodeBaru

    def dequeue(self):
        # menghapus data dari front (depan)
        if self.is_empty():
            print('Queue kosong, tidak bisa dequeue')
            return None
        
        # 1) lihat data yang paling depan
        data_terhapus = self.front.data  
        # 2) geser front ke node berikutnya
        self.front = self.front.next

        # 3) jika setelah geser front menjadi None, berarti queue kosong, 
        # maka rear juga harus None
        if self.front is None:
            self.rear = None
        return data_terhapus
    
    def tampilkan(self):
        current = self.front
        print('Front -> ', end='')

        while current is not None:
            print(current.data, end=' -> ')
            current = current.next

        print('None (Rear di node terakhir)')


# Instansiasi objek QueueLL
q = QueueLL()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')

q.tampilkan()
q.dequeue()
q.tampilkan()
