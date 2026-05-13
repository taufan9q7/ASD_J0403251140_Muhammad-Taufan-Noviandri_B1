#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

#============================================
# Latihan 1: BST (Binary Search Tree)
#=============================================

# Bikin class Node sebagai kerangka tiap titik di pohon
class Node:
    def __init__(self, data):
        self.data = data    # isi datanya, misal 50, 30, 70, dll
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

# Mulai dari tree kosong dulu
root = None
data_list = [50, 30, 70, 20, 40, 60, 80]   # ini datanya, 50 masuk duluan jadi root

# Insert satu-satu datanya ke dalam tree
for data in data_list:
    root = insert(root, data)   # tiap insert, root diupdate terus

print("BST berhasil dibuat dengan data: ", data_list)

#==============================================
# Latihan 2 : Traversal Inorder pada BST
#==============================================

# Fungsi inorder: cetak tree dengan urutan kiri -> node sekarang -> kanan
# hasilnya otomatis urut dari kecil ke besar karena sifat BST
def inorder(root):
    if root is not None:            # kalau nodenya ada (bukan kosong)
        inorder(root.left)          # masuk ke kiri dulu sampai habis
        print(root.data, end=" ")   # baru cetak datanya
        inorder(root.right)         # terakhir baru ke kanan

print("\nHasil Traversal Inorder: ")
inorder(root)   # harusnya keluar urut: 20 30 40 50 60 70 80

#==============================================
# Latihan 3 : Search pada BST
#==============================================

# Fungsi buat nyari data di BST, return True kalau ketemu, False kalau nggak
def search(root, key):
    if root is None:                        # kalau nodenya udah habis tapi data ga ketemu
        return False                        # berarti datanya emang ga ada
    if root.data == key:                    # kalau data yang dicari sama dengan node sekarang
        return True                         # ketemu! langsung return True
    elif key < root.data:                   # kalau data yang dicari lebih kecil
        return search(root.left, key)       # cari ke subtree kiri
    else:                                   # kalau data yang dicari lebih besar
        return search(root.right, key)      # cari ke subtree kanan

# Uji pencarian dengan key = 10
key = 10                    # angka 10 ga ada di data_list, jadi harusnya "tidak ditemukan"
if search(root, key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")