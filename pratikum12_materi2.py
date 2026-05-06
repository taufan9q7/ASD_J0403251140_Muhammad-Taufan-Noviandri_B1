#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#=============================================

# ==========================================================
# Materi 2
# ==========================================================

def bellman_ford(graph, start):
#    Algoritma Bellman-Ford untuk mencari jarak terpendek dari satu titik ke semua titik lainnya.
    
    # 1. Inisialisasi: Jarak ke semua node diset tak hingga (inf), 
    # kecuali node asal yang diset 0.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 2. Proses Relaksasi: Dilakukan sebanyak (V - 1) kali, 
    # di mana V adalah jumlah total node dalam graf.
    # Secara teoritis, jalur terpendek antar node maksimal melewati (V - 1) sisi.
    for _ in range(len(graph) - 1):
        # Iterasi melalui setiap node dan tetangganya (edge)
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    # Perbarui jarak ke tetangga dengan nilai yang lebih kecil tersebut.
                    distances[neighbor] = distances[node] + weight

    # Catatan: Jika ingin mendeteksi "Negative Cycle", kita bisa menambah satu iterasi lagi.
    # Jika jarak masih bisa mengecil pada iterasi ke-V, berarti ada siklus negatif.

    return distances

