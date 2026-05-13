#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ============================================================
# Latihan 5 - Tugas Mandiri
# Kasus 1: Jaringan Jalan Antar Kota
# Algoritma: Kruskal (Minimum Spanning Tree)
# ============================================================

# ============================================================
# 1. REPRESENTASI WEIGHTED GRAPH
# ============================================================
# Graph direpresentasikan sebagai daftar edge (sisi):
# Format: (bobot, node_asal, node_tujuan)

edges = [
    (5, "Bogor",   "Jakarta"),   # Bogor  - Jakarta  = 5
    (2, "Bogor",   "Depok"),     # Bogor  - Depok    = 2
    (3, "Depok",   "Jakarta"),   # Depok  - Jakarta  = 3
    (6, "Jakarta", "Bandung"),   # Jakarta- Bandung  = 6
    (4, "Depok",   "Bandung"),   # Depok  - Bandung  = 4
]

# Daftar semua node (kota) dalam jaringan
nodes = ["Bogor", "Jakarta", "Depok", "Bandung"]

# IMPLEMENTASI ALGORITMA KRUSKAL
# UNION-FIND (Disjoint Set Union) 

def make_set(nodes):
    """Inisialisasi setiap node sebagai himpunan sendiri."""
    parent = {n: n for n in nodes}
    rank   = {n: 0 for n in nodes}
    return parent, rank

def find(parent, node):
    """Cari root himpunan dari 'node' (dengan path compression)."""
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, u, v):
    """
    Gabungkan himpunan u dan v.
    Return True  -> edge diterima (tidak membentuk siklus)
    Return False -> edge ditolak (sudah satu himpunan / siklus)
    """
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u == root_v:
        return False  # Sudah terhubung -> TOLAK

    # Union by rank
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True  # Berhasil digabung -> TERIMA


# FUNGSI KRUSKAL

def kruskal_mst(nodes, edges):
    """Jalankan Kruskal, kembalikan MST edges dan total bobot."""

    # Langkah 1: Urutkan edge dari bobot terkecil
    sorted_edges = sorted(edges, key=lambda e: e[0])

    # Langkah 2: Inisialisasi Union-Find
    parent, rank = make_set(nodes)

    mst_edges  = []
    total_cost = 0

    # Header output
    print("=" * 58)
    print("   KRUSKAL MST - JARINGAN JALAN ANTAR KOTA")
    print("=" * 58)
    print(f"\n{'  Edge':<28} {'Bobot':>5}  {'Status'}")
    print("-" * 58)

    # Langkah 3: Proses setiap edge (terurut)
    for bobot, u, v in sorted_edges:
        accepted = union(parent, rank, u, v)
        status   = "✔ DIPILIH" if accepted else "✘ Ditolak (siklus)"
        print(f"  {u:<12} -- {v:<12} {bobot:>3}    {status}")

        if accepted:
            mst_edges.append((bobot, u, v))
            total_cost += bobot

        # Selesai jika sudah ada (n-1) edge
        if len(mst_edges) == len(nodes) - 1:
            break

    return mst_edges, total_cost

# MENJALANKAN & OUTPUT HASIL

mst_edges, total_cost = kruskal_mst(nodes, edges)

print("\n" + "=" * 58)
print("   HASIL MST - JARINGAN JALAN MINIMUM")
print("=" * 58)
print("\n  Edge yang dipilih untuk jaringan jalan:\n")
for i, (bobot, u, v) in enumerate(mst_edges, 1):
    print(f"    {i}. {u:<12} --  {v:<12}  [Bobot: {bobot}]")

print()
print(f"  Total Bobot Minimum  :  {total_cost}")
print("=" * 58)


# Soal dan Jawaban:
# 1. Kasus yang dipilih:
#    KASUS 1 - Jaringan Jalan Antar Kota
#    (Bogor, Jakarta, Depok, Bandung)

# 2. Algoritma yang digunakan:
#    KRUSKAL'S ALGORITHM
#    Cara kerja: urutkan semua edge dari bobot terkecil,
#    lalu pilih edge secara greedy selama tidak membentuk
#    siklus. Siklus dideteksi dengan struktur Union-Find.

# 3. Edge yang dipilih dalam MST:
#    - Bogor   -- Depok    [Bobot: 2]
#    - Depok   -- Jakarta  [Bobot: 3]
#    - Depok   -- Bandung  [Bobot: 4]

# 4. Total bobot MST:
#    2 + 3 + 4 = 9

# 5. Mengapa edge tertentu tidak dipilih?
#    - Bogor -- Jakarta (bobot 5):
#      DITOLAK karena Bogor dan Jakarta sudah terhubung
#      melalui jalur Bogor -> Depok -> Jakarta.
#      Memilihnya akan membentuk SIKLUS.

#    - Jakarta -- Bandung (bobot 6):
#      DITOLAK karena Jakarta dan Bandung sudah terhubung
#      melalui jalur Jakarta -> Depok -> Bandung.
#      Selain itu bobotnya paling besar (6), tidak efisien.

#    Prinsip MST: setiap kota harus terhubung, tanpa
#    jalur redundan, dengan total bobot seminimum mungkin.