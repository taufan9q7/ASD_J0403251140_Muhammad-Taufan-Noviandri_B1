#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Implementasi Algoritma Kruskal (Minimum Spanning Tree)
# ==========================================================

# 1. Definisi Data: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# 2. Inisialisasi Struktur Data Disjoint Set (DSU)
# Parent menyimpan representasi grup dari setiap node
parent = {node: node for edge in edges for node in edge[1:]}

def find(i):
    """Mencari root dari node i dengan path compression."""
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    """Menggabungkan dua set jika tidak membentuk cycle."""
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        parent[root_i] = root_j
        return True
    return False

# 3. Eksekusi Algoritma Kruskal
def kruskal(edge_list):
    # Mengurutkan edge berdasarkan bobot terkecil
    edge_list.sort()
    
    mst = []
    total_weight = 0
    
    for weight, u, v in edge_list:
        # Jika union berhasil (berarti u dan v belum terhubung)
        if union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            
    return mst, total_weight

# 4. Output Hasil
mst_result, weight_result = kruskal(edges)

print("Minimum Spanning Tree (MST):")
print("-" * 30)
for u, v, weight in mst_result:
    print(f"Edge {u} - {v} dengan bobot {weight}")

print("-" * 30)
print(f"Total Bobot MST = {weight_result}")

# Soal:
# 1. Edge mana yang dipilih pertama kali?
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# 3. Berapa total bobot MST yang dihasilkan?
# 4. Mengapa edge tertentu tidak dipilih?

# Jawaban:
# 1. Edge yang dipilih pertama kali adalah edge dengan bobot terkecil, yaitu edge C-D dengan bobot 1.
# 2. Edge dengan bobot paling kecil dipilih lebih dahulu karena algoritma Kruskal bertujuan untuk membangun MST dengan total bobot minimum. 
#    Memilih edge dengan bobot terkecil memastikan bahwa kita selalu menambahkan edge yang paling efisien ke dalam MST, sehingga mengurangi total bobot keseluruhan.
# 3. Total bobot MST yang dihasilkan adalah 6, yang merupakan jumlah dari bobot edge A-C (2), C-D (1), dan B-D (3).
# 4. Edge tertentu tidak dipilih karena jika dipilih, edge tersebut akan membentuk cycle dalam MST. 
#    Misalnya, edge A-B dengan bobot 4 tidak dipilih karena jika dipilih, akan membentuk cycle A-B-D-A,
#    yang bertentangan dengan sifat pohon (tree) yang tidak boleh memiliki cycle. 
