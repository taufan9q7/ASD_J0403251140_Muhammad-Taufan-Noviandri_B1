#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================
# Latihan 6: Struktur Organisasi Perusahaan
#=============================================

# Class Node adalah unit dasar pada Tree
class Node:
    def __init__(self, data):
        self.data = data
        # menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right) 

#membuat tree struktur organisasi
root = Node("Direktur ")

#child Level 1
root.left = Node("Manajer A ")
root.right = Node("Manajer B ")
root.right.left = Node("Manajer C ")  # tambahan Manajer C

#child Level 2
root.left.left = Node("Staff 1 ")
root.left.right = Node("Staff 2 ")

root.right.right = Node("Staff 3 ")

root.right.left.left = Node("Staff 4 ")  # child kiri Manajer C
root.right.left.right = Node("Staff 5 ") # child kanan Manajer C

# menjalankan traversal preorder
print("hasil traversal preorder: ")    
preorder(root)

#penjelasan = Program ini mensimulasikan struktur organisasi perusahaan menggunakan
#binary tree dengan traversal preorder (Root -> Left -> Right). Root
#adalah Direktur sebagai puncak organisasi, lalu di level 1 ada Manajer
#A (kiri), Manajer B (kanan), dan Manajer C (kiri dari Manajer B) yang
#ditambahkan sebagai pengembangan tree. Di level 2, Manajer A membawahi
#Staff 1 dan Staff 2, Manajer B membawahi Staff 3, sedangkan Manajer C
#membawahi Staff 4 dan Staff 5. Dengan preorder, output yang dihasilkan
#adalah: Direktur -> Manajer A -> Staff 1 -> Staff 2 -> Manajer B ->
#Manajer C -> Staff 4 -> Staff 5 -> Staff 3.