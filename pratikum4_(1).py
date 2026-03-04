# ==========================================================
# Nama : Muhammad Taufan Noviandri
# NIM : J0403251140
# Kelas : TPL - B1
# ==========================================================

#===========================================================
#Implementasi Dasar : Node pada Linked List
#===========================================================

# Membuat class node (merupakan unit dasar dari linked list)
class Node:
        def __init__(self, data): #konstruktor 
            self.data = data # Menyimpan nilai/data
            self.next = None # Pointer untuk node berikutnya(awal=none)

# 1) Membuat node satu per satu
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')

# 2) Menghubungkan node : A -> B -> C -> None
nodeA.next = nodeB # Node A menunjuk ke Node B  
nodeB.next = nodeC # Node B menunjuk ke Node C

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data) # Cetak data pada node saat ini
    current = current.next # Pindah ke node berikutnya

#============================================================
#Implementasi Dasar : Linked List + Insert 
#============================================================

class LinkedList:
    def __init__(self):
        self.head = None # Awalnya kosong

    def insert_awal(self, data):
       # 1) buat node baru
       nodeBaru = Node(data) # panggil class node
       
       # 2) node baru menunjuk ke head lama
       nodeBaru.next = self.head

       # 3) head pindah ke node baru
       self.head = nodeBaru 

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        # menggeser head ke node berikutnya
        self.head = self.head.next 
        print('Node yang dihapus adalah :', data_terhapus)

    def tampilkan(self):  # Implementasi traversal untuk menampilkan isi linked list
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print('========== List Baru ==========')
ll = LinkedList() #instantiasi objek ke class linked list
ll.insert_awal('X')
ll.insert_awal('Y')
ll.insert_awal('Z')
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
