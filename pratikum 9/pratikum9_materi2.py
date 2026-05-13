#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================
# Latihan 2 : 
#===========================================

#Class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai node
        self.left = None # Child kiri
        self.right = None # Child kanan
        pass

# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2 (child dari B dan C)
root.left.left = Node("D")   # D adalah child kiri dari B
root.left.right = Node("E")  # E adalah child kanan dari B
root.right.left = Node("F")  # F adalah child kiri dari C
root.right.right = Node("G") # G adalah child kanan dari C

# Menampilkan isi node
print("Data pada root: ", root.data)           
print("Child left root: ", root.left.data)     
print("Child right root: ", root.right.data)   
print("Child left dari B: ", root.left.left.data)    
print("Child right dari B: ", root.left.right.data)  
print("Child left dari C: ", root.right.left.data)   

# Penjelasan = Materi ke 2 ini, membuat tree dengan 3 level. Root "A" di level 0,
# node "B" dan "C" di level 1, serta "D", "E", "F", "G" di level 2.
# Untuk mengakses node caranya berantai dari root, contohnya node D
# ditulis root.left.left karena D adalah child kiri dari B, dan B
# adalah child kiri dari root.