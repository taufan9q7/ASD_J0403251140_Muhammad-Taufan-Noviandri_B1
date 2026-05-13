#============================================================
# Nama : Muhammad Taufan Noviandri
# Kelas: TPL - B1
# NIM  : J0403251140
#============================================================

#============================================================
# Latihan 2 - Studi Kasus DFS (Eksplorasi Jalur)
#============================================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)

# Output: A B D E C F

#============================================================
# Pertanyaan Analisis
#============================================================

# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
#    Karena DFS pakai rekursi — begitu ketemu tetangga yang belum dikunjungi,
#    dia langsung nyemplung ke sana tanpa nunggu tetangga lain selesai.
#    Jadi dari A, dia pilih B dulu, lanjut ke D (ujung), balik ke B, lanjut
#    ke E (ujung), baru balik ke A dan masuk ke C, lanjut ke F. Intinya
#    DFS itu "habiskan satu jalur sampai mentok, baru pindah jalur lain".

# 2. Apa yang terjadi jika urutan neighbor diubah?
#    Urutan kunjungan pasti berubah. Misalnya kalau 'A': ['C', 'B'],
#    maka DFS bakal masuk ke C dulu lanjut ke F, baru balik ke A dan
#    masuk ke B lanjut D dan E. Jadi outputnya jadi A C F B D E.
#    Algoritmanya tetap sama, cuma jalur yang ditempuh duluan yang beda.

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama:
#    DFS : A B D E C F  → masuk sedalam mungkin dulu per cabang
#    BFS : A B C D E F  → kunjungi semua tetangga selapis dulu baru turun
#    Perbedaannya ada di prioritas — DFS utamain kedalaman, BFS utamain
#    kelebaran. Makanya BFS lebih cocok buat cari jalur terpendek,
#    sedangkan DFS lebih cocok buat eksplorasi semua kemungkinan jalur.