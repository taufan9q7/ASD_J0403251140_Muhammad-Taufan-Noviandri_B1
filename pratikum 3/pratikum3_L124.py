# ================================== 
# Nama  : Muhammad Taufan Noviandri
# NIM   : J0403251140
# Kelas : TPL - B1
# ==================================

# ========== Tugas Pratikum pertemuan 3 (Latihan 1,2,4) ==========

# Membuat Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Membuat Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Menampilkan isi linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# ========================================
# LATIHAN 1
# Menghapus node berdasarkan nilai tertentu
# ============================================
    def delete_node(self, key):
        temp = self.head

        # Jika node pertama yang ingin dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        # Mencari node yang akan dihapus
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika nilai tidak ditemukan
        if temp is None:
            print("Nilai tidak ditemukan dalam Linked List.")
            return

        # Menghapus node
        prev.next = temp.next
        temp = None

# Contoh penggunaan
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
print("Linked List sebelum dihapus:")
ll.display()
ll.delete_node(13)
print("Linked List setelah menghapus 13:")
ll.display()

# Membuat Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Singly Linked List
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Menambahkan node di akhir
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:  # Jika list kosong
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular link
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular link kembali ke head

# ===============================
# LATIHAN 2 - Pencarian
# ===============================
    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head

        # Cek node pertama
        if temp.data == key:
            print(f"Elemen {key} ditemukan dalam Circular Linked List.")
            return

        temp = temp.next

        # Loop sampai kembali ke head
        while temp != self.head:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")

# Program Utama
cll = CircularSinglyLinkedList()

# Input elemen
data_input = input("Masukkan elemen ke dalam Circular Linked List (pisahkan dengan koma): ")

if data_input.strip() != "":
    elemen = data_input.split(",")
    for item in elemen:
        cll.insert_at_end(int(item.strip()))

# Input nilai yang ingin dicari
cari = int(input("Masukkan elemen yang ingin dicari: "))

# Panggil fungsi pencarian
cll.search(cari)

# Membuat Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Single Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Menampilkan isi linked list
    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# ==========================================
# LATIHAN 4 - Menggabungkan 2 Linked List
# ==========================================
    def merge(self, list2):
        merged_list = LinkedList()

        # Salin semua elemen dari list pertama
        temp = self.head
        while temp:
            merged_list.insert_at_end(temp.data)
            temp = temp.next

        # Salin semua elemen dari list kedua
        temp = list2.head
        while temp:
            merged_list.insert_at_end(temp.data)
            temp = temp.next

        return merged_list

# Program Utama
ll1 = LinkedList()
ll2 = LinkedList()

# Input Linked List 1
data1 = input("Masukkan elemen untuk Linked List 1 (pisahkan dengan koma): ")
if data1.strip() != "":
    elemen1 = data1.split(",")
    for item in elemen1:
        ll1.insert_at_end(int(item.strip()))

# Input Linked List 2
data2 = input("Masukkan elemen untuk Linked List 2 (pisahkan dengan koma): ")
if data2.strip() != "":
    elemen2 = data2.split(",")
    for item in elemen2:
        ll2.insert_at_end(int(item.strip()))

# Tampilkan Linked List 1
print("Linked List 1:", end=" ")
ll1.display()

# Tampilkan Linked List 2
print("Linked List 2:", end=" ")
ll2.display()

# Gabungkan
merged = ll1.merge(ll2)

# Tampilkan hasil gabungan
print("Linked List setelah digabungkan:", end=" ")
merged.display()
