#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Materi 1
# ==========================================================

import heapq

# Representasi graf menggunakan Adjacency List (Dictionary)
# Key: Nama node, Value: Dictionary tetangga dan bobot jalurnya
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
#    Algoritma Dijkstra untuk mencari jalur terpendek dari satu titik ke semua titik lainnya.
    
    # 1. Inisialisasi: Anggap semua node memiliki jarak tak hingga (inf) di awal,
    # kecuali node awal (start) yang jaraknya ke diri sendiri adalah 0.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # 2. Priority Queue (pq): Digunakan untuk mengambil node dengan jarak terkecil secara efisien.
    # Format data di dalamnya adalah (jarak_kumulatif, nama_node).
    pq = [(0, start)]
    
    while pq:
        # Mengambil node dengan jarak terkecil dari queue
        current_distance, current_node = heapq.heappop(pq)
        
        # 3. Optimasi: Jika jarak yang baru diambil lebih besar dari jarak yang sudah 
        # dicatat di tabel 'distances', maka abaikan proses ini.
        if current_distance > distances[current_node]:
            continue
            
        # 4. Eksplorasi Tetangga: Periksa semua node yang terhubung langsung dengan node saat ini.
        for neighbor, weight in graph[current_node].items():
            # Hitung total jarak dari start ke tetangga melalui current_node
            distance = current_distance + weight
            
            # 5. Relaksasi: Jika ditemukan jalur yang lebih pendek menuju tetangga tersebut...
            if distance < distances[neighbor]:
                # Update nilai jarak terkecil di tabel
                distances[neighbor] = distance
                # Masukkan ke dalam priority queue untuk mengecek tetangga-tetangganya nanti
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# Eksekusi Algoritma
hasil = dijkstra(graph, 'A')

# Menampilkan hasil akhir
# Output berupa dictionary yang menunjukkan biaya minimum dari 'A' ke setiap node lainnya.
print(f"Jarak terpendek dari titik A ke setiap node: \n{hasil}")