#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================
# Latihan 1 : Membuat Node
#===========================================

#Class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai node
        self.left = None # Child kiri
        self.right = None # Child kanan
        pass

# Membuat root
root = Node("A")

# Menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

# Pembahasan = Pada latihan ini, kita membuat sebuah Node yang merupakan
# komponen dasar dari struktur data Tree. Class Node memiliki 3 atribut,
# yaitu data untuk menyimpan nilai, left untuk child kiri, dan right untuk
# child kanan. Saat pertama kali dibuat, child kiri dan kanan bernilai None
# karena belum ada node lain yang terhubung. Pada contoh ini, kita membuat
# satu node root dengan nilai "A". Karena belum ada child yang ditambahkan,
# maka output dari root.left dan root.right adalah None.