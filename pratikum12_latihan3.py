#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

# Eksekusi
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"{node} = {distance}")
    
# soal:
# 1. Berapa bobot langsung dari A ke B?
# 2. Berapa total bobot jalur A -> C -> B?
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# 5. Apa yang dimaksud dengan proses relaksasi edge?
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?

# Jawaban:
# 1. Bobot langsung dari A ke B adalah 5.
# 2. Total bobot jalur A -> C -> B adalah 4 (A ke C) + (-2) (C ke B) = 2.
# 3. Jalur A -> C -> B menghasilkan jarak lebih kecil menuju B (2) dibandingkan jalur langsung A -> B (5).
# 4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena algoritma ini melakukan relaksasi edge secara berulang, sehingga dapat menemukan jalur terpendek meskipun ada edge dengan bobot negatif.
# 5. Proses relaksasi edge adalah langkah di mana algoritma memeriksa apakah jalur yang baru ditemukan ke suatu node melalui edge tertentu lebih pendek daripada jalur yang sudah diketahui sebelumnya. Jika ya, maka jarak ke node tersebut diperbarui dengan nilai yang lebih kecil.
# 6. Perbedaan utama Bellman-Ford dan Dijkstra adalah bahwa Bellman-Ford dapat menangani graph dengan bobot negatif, sedangkan Dijkstra tidak dapat. Selain itu, Dijkstra menggunakan priority queue untuk efisiensi, sementara Bellman-Ford melakukan relaksasi edge secara berulang tanpa menggunakan struktur data khusus.
