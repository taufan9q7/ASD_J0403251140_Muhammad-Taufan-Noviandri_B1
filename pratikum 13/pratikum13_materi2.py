#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

import heapq

# ==========================================================
# Implementasi Algoritma Prim (MST)
# ==========================================================

def prim(graph, start_node):
    """
    Mencari Minimum Spanning Tree menggunakan algoritma Prim.
    
    Args:
        graph (dict): Adjacency list berupa dictionary of dictionaries.
        start_node (str): Node awal pencarian.
    """
    # Inisialisasi
    visited = {start_node}
    edges = []
    mst = []
    total_weight = 0

    # Masukkan edge dari node awal ke dalam priority queue (heap)
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(edges, (weight, start_node, neighbor))

    while edges:
        # Ambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Tambahkan edge baru dari node yang baru dikunjungi
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# --- Data Input ---
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# --- Eksekusi dan Output ---
start_point = 'A'
mst_result, total = prim(graph, start_point)

print(f"Minimum Spanning Tree (Mulai dari '{start_point}'):")
print("-" * 35)
print(f"{'Edge':<15} | {'Bobot':<10}")
print("-" * 35)

for u, v, weight in mst_result:
    print(f"{u} <---> {v:<7} | {weight:<10}")

print("-" * 35)
print(f"Total Bobot MST = {total}")