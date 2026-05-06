#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga (inf)
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke dirinya sendiri adalah 0
    distances[start] = 0
    
    # Priority queue menyimpan pasangan (jarak, node)
    # heapq akan selalu menempatkan jarak terkecil di paling atas
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
        # berarti kita sudah menemukan jalur yang lebih baik sebelumnya
        if current_distance > distances[current_node]:
            continue
            
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jalur yang lebih murah/pendek ke tetangga
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Eksekusi program
hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"{node} = {distance}")
    
# soal:
# 1. Berapa jarak terpendek dari A ke B?
# 2. Berapa jarak terpendek dari A ke C?
# 3. Berapa jarak terpendek dari A ke D?
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?

# Jawaban:
# 1. Jarak terpendek dari A ke B adalah 4.
# 2. Jarak terpendek dari A ke C adalah 2.
# 3. Jarak terpendek dari A ke D adalah 3 (melalui C).
# 4. Jarak A ke D lebih kecil melalui C karena bobot dari A ke C (2) dan C ke D (1) lebih kecil dibandingkan bobot dari A ke B (4) dan B ke D (5).
# 5. Fungsi priority_queue dalam algoritma Dijkstra adalah untuk menyimpan node-node yang akan dieksplorasi berdasarkan jarak terpendek yang ditemukan sejauh ini,
# sehingga node dengan jarak terkecil selalu diproses terlebih dahulu.
# 6. Dijkstra tidak cocok untuk graph dengan bobot negatif karena algoritma ini mengasumsikan bahwa setelah sebuah node diproses, jaraknya tidak akan berubah lagi. 
# Jika ada bobot negatif, jarak ke node yang sudah diproses bisa menjadi lebih kecil, yang menyebabkan hasil yang salah.
