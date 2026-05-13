#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ============================================================
# Latihan 4: Studi Kasus - Jaringan Kabel Antar Gedung
# ============================================================


# REPRESENTASI WEIGHTED GRAPH
# Graph direpresentasikan sebagai daftar edge (sisi):
# Format: (bobot, node_asal, node_tujuan)

edges = [
    (4, "GedungA", "GedungB"),   # Biaya A-B = 4
    (2, "GedungA", "GedungC"),   # Biaya A-C = 2
    (3, "GedungB", "GedungD"),   # Biaya B-D = 3
    (1, "GedungC", "GedungD"),   # Biaya C-D = 1
    (5, "GedungA", "GedungD"),   # Biaya A-D = 5
]

# Daftar semua node (gedung) dalam jaringan
nodes = ["GedungA", "GedungB", "GedungC", "GedungD"]


# ============================================================
# IMPLEMENTASI ALGORITMA KRUSKAL
# ============================================================

# STRUKTUR DATA UNION-FIND 
# Digunakan untuk mendeteksi siklus saat membangun MST

def make_set(nodes):
    """Inisialisasi: setiap node menjadi himpunan sendiri."""
    parent = {node: node for node in nodes}
    rank   = {node: 0    for node in nodes}
    return parent, rank

def find(parent, node):
    """Cari root (wakil) dari himpunan yang memuat 'node'.
    Menggunakan path compression agar lebih efisien."""
    if parent[node] != node:
        parent[node] = find(parent, parent[node])  # path compression
    return parent[node]

def union(parent, rank, node1, node2):
    """Gabungkan dua himpunan. Kembalikan False jika sudah
    satu himpunan (berarti akan membentuk siklus)."""
    root1 = find(parent, node1)
    root2 = find(parent, node2)

    if root1 == root2:
        return False  # Sudah terhubung -> siklus -> TOLAK edge ini

    # Union by rank: pohon lebih kecil digabung ke pohon lebih besar
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

    return True  # Berhasil digabung -> TERIMA edge ini


# FUNGSI UTAMA KRUSKAL

def kruskal_mst(nodes, edges):
    """
    Menjalankan algoritma Kruskal untuk mencari MST.
    Mengembalikan daftar edge yang dipilih dan total biayanya.
    """
    # Langkah 1: Urutkan edge dari bobot terkecil ke terbesar
    sorted_edges = sorted(edges, key=lambda e: e[0])

    # Langkah 2: Inisialisasi Union-Find
    parent, rank = make_set(nodes)

    mst_edges    = []   # Edge yang masuk ke MST
    total_cost   = 0    # Total biaya minimum

    print("=" * 55)
    print("   ALGORITMA KRUSKAL - JARINGAN KABEL ANTAR GEDUNG")
    print("=" * 55)
    print(f"\n{'Edge (Sorted)':<30} {'Bobot':>5}  {'Status'}")
    print("-" * 55)

    # Langkah 3: Proses setiap edge (sudah terurut)
    for bobot, u, v in sorted_edges:
        accepted = union(parent, rank, u, v)
        status   = "✔ DIPILIH" if accepted else "✘ Ditolak (siklus)"

        print(f"  {u} -- {v:<12} {bobot:>5}  {status}")

        if accepted:
            mst_edges.append((bobot, u, v))
            total_cost += bobot

        # MST selesai jika sudah ada (n-1) edge
        if len(mst_edges) == len(nodes) - 1:
            break

    return mst_edges, total_cost


# JALANKAN PROGRAM 

mst_edges, total_cost = kruskal_mst(nodes, edges)

# OUTPUT HASIL 
print("\n" + "=" * 55)
print("   HASIL MINIMUM SPANNING TREE")
print("=" * 55)
print("\n  Edge yang dipilih untuk jaringan kabel:")
print()
for i, (bobot, u, v) in enumerate(mst_edges, 1):
    print(f"    {i}. {u}  --  {v}   [Biaya: {bobot}]")

print()
print(f"  Total Biaya Minimum : {total_cost}")
print("=" * 55)


# Soal dan Jawaban: 
# 1. Algoritma yang digunakan:
#    KRUSKAL'S ALGORITHM
#    Bekerja dengan mengurutkan semua edge dari bobot terkecil,
#    lalu memilih edge secara greedy selama tidak membentuk
#    siklus (dideteksi dengan Union-Find / Disjoint Set Union).

# 2. Edge yang dipilih (MST):
#    - GedungC -- GedungD  [Biaya: 1]
#    - GedungA -- GedungC  [Biaya: 2]
#    - GedungB -- GedungD  [Biaya: 3]

# 3. Total biaya minimum:
#    1 + 2 + 3 = 6

# 4. Mengapa MST cocok digunakan pada kasus ini?
#    MST (Minimum Spanning Tree) cocok karena:
#    - Tujuan: menghubungkan SEMUA gedung (node) dengan kabel
#      sehingga setiap gedung dapat saling berkomunikasi.
#    - Syarat: tidak ada kabel yang redundan (tidak ada siklus),
#      sehingga biaya tidak terbuang percuma.
#    - Optimasi: MST menjamin total biaya pemasangan kabel
#      adalah yang PALING MINIMUM di antara semua kemungkinan
#      jaringan yang menghubungkan semua gedung.
#    - Hasil MST = n-1 kabel untuk n gedung (paling efisien).
