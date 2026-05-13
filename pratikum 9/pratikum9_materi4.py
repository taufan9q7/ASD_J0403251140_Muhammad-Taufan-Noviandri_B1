#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================
# Latihan 4: Membuat Traversal inorder
#===========================================

# Class Node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat fungsi inorder left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# Membuat tree
# membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2 (child dari B dan C)
root.left.left = Node("D")   
root.left.right = Node("E")

print("hasil traversal inorder: ")    
inorder(root)

#penjelasan =  Inorder traversal adalah metode penelusuran tree dengan urutan
#Left -> Root -> Right, artinya subtree kiri dikunjungi dulu, lalu
#node induknya, baru kemudian subtree kanan. Pada tree ini, penelusuran
#dimulai dari node paling kiri yaitu D, lalu naik ke induknya B, lalu
#ke E (kanan dari B), kemudian ke root A, dan terakhir ke C yang berada
#di kanan root dan tidak punya anak. Maka output yang dihasilkan adalah:
#D B E A C