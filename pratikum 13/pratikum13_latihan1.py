#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================


# Daftar edge graph
edges = [
 ('A', 'B'),
 ('A', 'C'),
 ('A', 'D'),
 ('C', 'D'),
 ('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
 ('A', 'C'),
 ('C', 'D'),
 ('D', 'B')
]
print("Edge pada graph:")
for edge in edges:
 print(edge)
print("\nSpanning Tree:")

for edge in spanning_tree:
 print(edge)
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Soal:
# 1. Apa perbedaan graph awal dan spanning tree?
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

# Jawaban:
# 1. Perbedaan graph awal dan spanning tree:
#    - Graph awal memiliki 5 edge, sedangkan spanning tree hanya memiliki 3 edge.
#    - Graph awal memiliki cycle (misalnya A-B-D-A), sedangkan spanning tree tidak memiliki cycle.
#    - Spanning tree adalah subgraph dari graph awal yang menghubungkan semua node tanpa membentuk cycle.               
# 2. Spanning tree tidak boleh memiliki cycle karena:
#    - Cycle akan menyebabkan redundansi dalam koneksi antar node, yang bertentangan dengan
#      tujuan spanning tree untuk menghubungkan semua node dengan jumlah edge minimum.
#    - Cycle juga dapat menyebabkan masalah dalam algoritma yang menggunakan spanning tree, seperti
#      algoritma Kruskal atau Prim, yang mengandalkan struktur pohon untuk memastikan efisiensi dan keakuratan.
# 3. Jumlah edge spanning tree selalu lebih sedikit karena:
#    - Spanning tree menghubungkan semua node dengan jumlah edge minimum, yaitu (V - 1) edge untuk V node.
#    - Graph awal dapat memiliki lebih banyak edge, termasuk edge yang tidak diperlukan untuk menghubungkan semua node, sehingga jumlah edge pada graph awal bisa lebih banyak daripada spanning tree.
