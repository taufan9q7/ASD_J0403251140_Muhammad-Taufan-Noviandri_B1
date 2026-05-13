#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================
# Latihan 3: Membuat Traversal preorder
#===========================================

#class node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai node
        self.left = None # Child kiri
        self.right = None # Child kanan
        pass

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right) 

# Membuat tree
# membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2 (child dari B dan C)
root.left.left = Node("D")   
root.left.right = Node("E")

# menjalankan traversal preorder
print("hasil traversal preorder: ")    
preorder(root)

#penjelasan = Program ini mengimplementasikan traversal preorder pada struktur data tree biner.
# Setiap node memiliki data serta child kiri dan kanan. Traversal preorder dilakukan
# dengan urutan mengunjungi root terlebih dahulu, kemudian subtree kiri, dan terakhir
# subtree kanan. Berdasarkan struktur tree yang dibuat (A sebagai root, B dan C sebagai
# child, serta D dan E sebagai child dari B), hasil traversal preorder yang diperoleh
# adalah: A B D E C.