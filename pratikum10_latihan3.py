#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# ==========================================================

# Bikin class Node buat nyimpen data di setiap titik pohon
class Node:
    def __init__(self, data):
        self.data = data    # ini isi datanya, misal 10, 20, 30
        self.left = None    # pointer ke node kiri, awalnya kosong
        self.right = None   # pointer ke node kanan, awalnya kosong


# Fungsi buat cetak isi tree dengan urutan: node sekarang -> kiri -> kanan
def preorder(root):
    if root is not None:            # kalau nodenya ada (bukan kosong)
        print(root.data, end=" ")   # cetak datanya dulu
        preorder(root.left)         # terus masuk ke kiri
        preorder(root.right)        # baru ke kanan


# Fungsi buat nampilin bentuk tree biar keliatan strukturnya
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:                                        # kalau nodenya ada
        print(" " * level + f"{posisi}: {root.data}")          # kasih spasi sesuai kedalamannya biar keliatan hierarkinya
        tampil_struktur(root.left, level + 1, "L")             # masuk ke kiri, level +1 biar lebih menjorok
        tampil_struktur(root.right, level + 1, "R")            # masuk ke kanan, sama juga


# Fungsi rotasi kiri, dipake waktu tree condong ke kanan
def rotate_left(x):
    y = x.right     # y itu node kanan dari x, dia yang bakal jadi root baru
    T2 = y.left     # simpen dulu subtree kiri milik y, nanti dipindahin ke x

    # proses rotasinya di sini
    y.left = x      # x turun ke bawah, jadi anak kiri y
    x.right = T2    # bekas tempat y di kanan x, diisi sama T2 yang tadi disimpen

    return y        # kembaliin y karena sekarang dia yang jadi root baru


# -----------------------------
# Program utama
# -----------------------------

# Buat tree yang condong ke kanan dulu (tree tidak seimbang)
root = Node(10)             # root-nya 10
root.right = Node(20)       # 20 ada di kanan 10
root.right.right = Node(30) # 30 ada di kanan 20, jadi tree miring ke kanan

# Tampilkan kondisi tree sebelum dirotasi
print("Preorder sebelum rotasi kiri:")
preorder(root)              # harusnya keluar: 10 20 30

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)       # keliatan kalau treenya miring ke kanan

# Lakukan rotasi kiri supaya tree lebih seimbang
root = rotate_left(root)    # root baru sekarang jadi 20

# Tampilkan kondisi tree sesudah dirotasi
print("\nPreorder sesudah rotasi kiri:")
preorder(root)              # harusnya keluar: 20 10 30

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)       # sekarang 20 jadi root, 10 di kiri, 30 di kanan