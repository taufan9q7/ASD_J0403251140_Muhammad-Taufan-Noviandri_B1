#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Implementasi Algoritma Kruskal (MST)
# ==========================================================

def find(parent, i):
    """Fungsi untuk mencari root dari node i dengan path compression."""
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    """Fungsi untuk menggabungkan dua set berdasarkan rank."""
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(edges):
    # Mengambil semua node unik
    nodes = set()
    for _, u, v in edges:
        nodes.add(u)
        nodes.add(v)
    
    # Inisialisasi DSU
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    
    # 1. Urutkan edge berdasarkan bobot (Weight)
    edges.sort()
    
    mst = []
    total_weight = 0

    print(f"{'Edge':<10} | {'Bobot':<6} | {'Status'}")
    print("-" * 30)

    for weight, u, v in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        # 2. Jika root berbeda, berarti tidak membentuk cycle
        if root_u != root_v:
            union(parent, rank, root_u, root_v)
            mst.append((u, v, weight))
            total_weight += weight
            print(f"{u} - {v:<5} | {weight:<6} | Diterima")
        else:
            print(f"{u} - {v:<5} | {weight:<6} | Skip (Cycle)")

    return mst, total_weight

# --- Data Input ---
edges_list = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Eksekusi
hasil_mst, total = kruskal(edges_list)

print("-" * 30)
print(f"Total Bobot MST = {total}")