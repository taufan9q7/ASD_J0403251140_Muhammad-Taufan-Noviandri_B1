#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    # Inisialisasi jarak semua node ke tak hingga
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue menyimpan (jarak, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, abaikan
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            # Perhitungan jarak baru
            distance = current_distance + weight
            
            # Jika ditemukan jalur lebih singkat ke tetangga
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Eksekusi program
hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(f"{lokasi} = {jarak} menit")
    
# Soal:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

# Jawaban:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit.
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit melalui jalur Gerbang -> Kantin -> Lab -> Aula.
# 3. Tidak selalu. Jalur langsung mungkin memiliki bobot yang lebih besar dibandingkan jalur yang melalui node lain. Dalam kasus ini, jalur langsung dari Gerbang ke Aula tidak ada, sehingga kita harus melalui node lain untuk mencapai Aula.
# 4. Dijkstra cocok digunakan pada kasus lokasi kampus ini karena graf yang digunakan memiliki bobot positif (waktu tempuh) dan kita ingin menemukan jalur terpendek dari satu titik ke semua titik lainnya. Dijkstra efisien untuk graf dengan bobot positif dan memberikan hasil yang akurat dalam konteks ini.   

