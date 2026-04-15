#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================
# Latihan 5: Membuat Traversal postorder
#===========================================

# Class Node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Membuat Traversal Postorder: Left -> Right -> Root
def postorder(node):
    if node is not None:
        postorder (node.left)
        postorder(node.right)
        print(node.data, end=" ")



# Membuat tree
# membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2 (child dari B dan C)
root.left.left = Node("D")   
root.left.right = Node("E")

print("hasil traversal postorder: ")    
postorder(root)

#penjelasan = Postorder traversal adalah metode penelusuran tree dengan urutan
#Left -> Right -> Root, artinya setiap subtree kiri dikunjungi dulu,
#lalu subtree kanan, baru terakhir node induknya. Pada tree ini, node
#D dan E adalah daun (tidak punya anak), jadi langsung diproses duluan.
#Kemudian naik ke B (induk D dan E), lalu ke C (yang tidak punya anak),
#dan terakhir ke root A. Maka output yang dihasilkan adalah: D E B C A.