#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Latihan 4: Membuat BST yang Tidak Seimbang
# ==========================================================

# Bikin class Node sebagai kerangka tiap titik di pohon
class Node:
    def __init__(self, data):
        self.data = data    # isi datanya, misal 10, 20, 30
        self.left = None    # anak kiri, awalnya kosong dulu
        self.right = None   # anak kanan, awalnya kosong juga


# Fungsi buat masukin data ke BST sesuai aturan (kiri < root < kanan)
def insert(root, data):
    if root is None:                            # kalau treenya masih kosong
        return Node(data)                       # langsung bikin node baru di sini
    if data < root.data:                        # kalau data lebih kecil dari node sekarang
        root.left = insert(root.left, data)     # masukkin ke subtree kiri
    elif data > root.data:                      # kalau data lebih besar
        root.right = insert(root.right, data)   # masukkin ke subtree kanan
    return root                                 # kembaliin root yang udah diupdate


# Fungsi buat cetak isi tree dengan urutan: node sekarang -> kiri -> kanan
def preorder(root):
    if root is not None:            # kalau nodenya ada (bukan kosong)
        print(root.data, end=" ")   # cetak datanya dulu
        preorder(root.left)         # terus masuk ke kiri
        preorder(root.right)        # baru ke kanan


# Fungsi buat nampilin bentuk tree biar keliatan strukturnya
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:                                    # kalau nodenya ada
        print(" " * level + f"{posisi}: {root.data}")      # kasih spasi sesuai kedalamannya
        tampil_struktur(root.left, level + 1, "L")         # masuk ke kiri, level +1 biar menjorok
        tampil_struktur(root.right, level + 1, "R")        # masuk ke kanan, sama juga


# -----------------------------
# Program utama
# -----------------------------

root = None             # tree masih kosong di awal
data_list = [10, 20, 30]  # data dimasukkan urut naik, makanya tree bakal miring ke kanan

# insert satu-satu datanya ke dalam tree
for data in data_list:
    root = insert(root, data)   # tiap insert, root diupdate terus

# tampilkan hasil preorder
print("Preorder BST:")
preorder(root)          # harusnya keluar: 10 20 30

# tampilkan struktur treenya
print("\n\nStruktur BST:")
tampil_struktur(root)   # keliatan treenya miring ke kanan karena datanya urut naik