#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

graph = {
    'Bogor'  : {'Jakarta': 5, 'Depok': 2},   # Bogor -> Jakarta = 5, Bogor -> Depok = 2
    'Depok'  : {'Jakarta': 2, 'Bandung': 6}, # Depok -> Jakarta = 2, Depok -> Bandung = 6
    'Jakarta': {'Bandung': 7},               # Jakarta -> Bandung = 7
    'Bandung': {}                            # node tujuan
}


def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Inisialisasi semua jarak dengan tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue: menyimpan pasangan (jarak, node)
    # Dimulai dari node awal dengan jarak 0
    pq = [(0, start)]

    while pq:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(pq)

        # Lewati jika jarak yang tersimpan sudah lebih kecil
        # (artinya node ini sudah pernah diproses dengan jarak lebih kecil)
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru menuju tetangga melalui node saat ini
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui dan masukkan ke queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Penentuan node awal
node_awal = 'Bogor'


# Jalankan Dijkstra dan tampilkan output jarak terpendek dari node awal ke semua node lainnya
hasil = dijkstra(graph, node_awal)

print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"  {node_awal} -> {kota} = {jarak}")

# Soal:
# 1. Node awal yang digunakan adalah
# 2. Node yang memiliki jarak paling kecil dari node awal
# 3. Node yang memiliki jarak paling besar dari node awal 
# 4. Cara kerja algoritma Dijkstra pada kasus ini

# Jawaban:
# 1. Bogor
# 2. Depok, dengan jarak = 2
# 3. Bandung, dengan jarak = 8
# 4. Dijkstra bekerja dengan memulai dari node awal (Bogor) dan secara iteratif memperbarui jarak ke tetangga-tetangganya. 
# Setiap kali menemukan jarak yang lebih kecil ke suatu node, Dijkstra memperbarui jarak tersebut dan menambahkannya ke priority queue untuk diproses lebih lanjut. 
# Proses ini berlanjut hingga semua node telah diproses, menghasilkan jarak terpendek dari node awal ke semua node lainnya.