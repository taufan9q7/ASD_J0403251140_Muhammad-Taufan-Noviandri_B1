#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

import heapq

# 1. Definisi Graf (Adjacency List)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start_node):
    """
    Implementasi Algoritma Prim menggunakan Priority Queue (Min-Heap)
    untuk mencari Minimum Spanning Tree (MST).
    """
    mst = []
    total_weight = 0
    visited = {start_node}
    edges = []

    # Masukkan semua edge dari node awal ke dalam min-heap
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(edges, (weight, start_node, neighbor))

    # Selama heap tidak kosong
    while edges:
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi, tambahkan ke MST
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Tambahkan semua edge dari node yang baru dikunjungi ke heap
            for neighbor, next_weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (next_weight, v, neighbor))

    return mst, total_weight

# 2. Eksekusi Program
start_point = 'A'
mst_result, total_cost = prim(graph, start_point)

# 3. Output Hasil
print(f"Minimum Spanning Tree (Mulai dari '{start_point}'):")
print("-" * 40)
for u, v, weight in mst_result:
    print(f"Edge {u} - {v} | Bobot: {weight}")

print("-" * 40)
print(f"Total Bobot MST = {total_cost}")

# Soal:
# 1. Node awal apa yang digunakan?
# 2. Edge mana yang dipilih pertama kali?
# 3. Bagaimana Prim menentukan edge berikutnya?
# 4. Berapa total bobot MST yang dihasilkan?
# 5. Apa perbedaan pendekatan Prim dan Kruskal?

# Jawaban:
# 1. Node awal yang digunakan adalah 'A'.
# 2. Edge yang dipilih pertama kali adalah edge A-C dengan bobot 2, karena memiliki bobot terkecil.
# 3. Prim menentukan edge berikutnya dengan memilih edge dengan bobot terkecil yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi.
# 4. Total bobot MST yang dihasilkan adalah 6 (A-C: 2, C-D: 1, D-B: 3).
# 5. Perbedaan pendekatan Prim dan Kruskal: 
#   - Prim membangun pohon secara bertahap dari satu node pusat (seperti menanam pohon yang tumbuh membesar). Sangat efisien untuk graf yang padat (dense graph). 
#   - Kruskal memilih edge terpendek dari seluruh graf sekaligus tanpa harus terhubung dengan node sebelumnya (seperti menyambungkan ranting-ranting terpisah), 
#     dan menggunakan Union-Find untuk mencegah cycle. Sangat efisien untuk graf yang renggang (sparse graph).