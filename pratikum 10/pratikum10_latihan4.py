#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
# ==========================================================

# Class Node untuk menyimpan data pada setiap simpul tree
class Node:
    def __init__(self, data):
        self.data = data    # nilai node
        self.left = None    # child kiri
        self.right = None   # child kanan


# Fungsi preorder: cetak node dimulai dari root -> kiri -> kanan
def preorder(root):
    if root is not None:
        print(root.data, end=" ")   # cetak nilai node saat ini
        preorder(root.left)          # rekursif ke kiri
        preorder(root.right)         # rekursif ke kanan


# Fungsi untuk menampilkan struktur tree secara visual
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")           # cetak node dengan indentasi
        tampil_struktur(root.left, level + 1, "L")              # tampilkan subtree kiri
        tampil_struktur(root.right, level + 1, "R")             # tampilkan subtree kanan


# Fungsi rotasi kanan
def rotate_right(y):
    x = y.left      # x adalah child kiri dari y (akan jadi root baru)
    T2 = x.right    # simpan subtree kanan milik x sementara

    # Proses rotasi
    x.right = y     # y menjadi child kanan dari x
    y.left = T2     # child kiri y diganti dengan T2

    return x        # x menjadi root baru


# -----------------------------
# Program utama
# -----------------------------

# Membuat tree tidak seimbang ke kiri: 30 -> 20 -> 10
root = Node(30)         # root = 30
root.left = Node(20)    # child kiri 30 = 20
root.left.left = Node(10)  # child kiri 20 = 10

# Tampilkan kondisi tree sebelum rotasi
print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# Lakukan rotasi kanan pada root
root = rotate_right(root)

# Tampilkan kondisi tree sesudah rotasi
print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)