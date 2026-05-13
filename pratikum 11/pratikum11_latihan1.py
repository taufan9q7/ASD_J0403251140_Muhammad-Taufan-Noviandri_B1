<<<<<<< HEAD
#============================================================
# Nama : Muhammad Taufan Noviandri
# Kelas: TPL - B1
# NIM  : J0403251140
# Latihan 1: Studi Kasus BFS
#===============================

graph = { 'Rumah': ['Sekolah', 'Toko'], 
         'Sekolah': ['Perpustakaan'], 
         'Toko': ['Pasar'], 
         'Perpustakaan': [], 
         'Pasar': [] 
} 

from collections import deque 

def bfs(graph, start): 

    visited = set() 

    queue = deque([start]) 

    visited.add(start) 

    while queue:
        node = queue.popleft() 
        print(node, end=" ") 
        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 

print("BFS dari Rumah:") 
bfs(graph, 'Rumah') 

# Pertanyaan Analisis 
# 1. Node mana yang dikunjungi pertama? 
#    Jawaban: 
#    Node yang dikunjungi pertama kali adalah 'Rumah'.
#    karena node tersebut ditentukan sebagai titik awal (start).

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?  
#    Jawaban:
#    Karena BFS menelusuri semua tetangga dari titik awal
#    sebelum berpindah ke node yang lebih jauh.

# 3. Apa perbedaan urutan BFS jika struktur graph diubah? 
#    Jawaban:
#    Jika urutan di dalam graph diubah (misalnya dari 
#    ['Sekolah', 'Toko'] menjadi ['Toko', 'Sekolah']), 
#    maka urutan cetak pada level yang sama juga akan berubah, 
=======
#============================================================
# Nama : Muhammad Taufan Noviandri
# Kelas: TPL - B1
# NIM  : J0403251140
# Latihan 1: Studi Kasus BFS
#===============================

graph = { 'Rumah': ['Sekolah', 'Toko'], 
         'Sekolah': ['Perpustakaan'], 
         'Toko': ['Pasar'], 
         'Perpustakaan': [], 
         'Pasar': [] 
} 

from collections import deque 

def bfs(graph, start): 

    visited = set() 

    queue = deque([start]) 

    visited.add(start) 

    while queue:
        node = queue.popleft() 
        print(node, end=" ") 
        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 

print("BFS dari Rumah:") 
bfs(graph, 'Rumah') 

# Pertanyaan Analisis 
# 1. Node mana yang dikunjungi pertama? 
#    Jawaban: 
#    Node yang dikunjungi pertama kali adalah 'Rumah'.
#    karena node tersebut ditentukan sebagai titik awal (start).

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?  
#    Jawaban:
#    Karena BFS menelusuri semua tetangga dari titik awal
#    sebelum berpindah ke node yang lebih jauh.

# 3. Apa perbedaan urutan BFS jika struktur graph diubah? 
#    Jawaban:
#    Jika urutan di dalam graph diubah (misalnya dari 
#    ['Sekolah', 'Toko'] menjadi ['Toko', 'Sekolah']), 
#    maka urutan cetak pada level yang sama juga akan berubah, 
>>>>>>> 7214ac27d648bd3885075c2fbd846002fd4f8107
#    meskipun levelnya berada di tingkatan yang sama.