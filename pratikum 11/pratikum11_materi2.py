#============================================================
#Implementasi BFS
#============================================================

#Struktur untuk membuat antrian, kita gunakan dari library collection, bawaan phyton 
from collections import deque

#representasi graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

def bfs(graph, start):
   #Fungsi untuk melakukan penelusuran graph dengan BFS
   #graph: dictionary yang menyimpan struktur dari graph
   #start: node awal penelusuran

   #Queue digunakan untuk menyimpan node yang akan diproses-/-dibocd
    queue = deque()

   #variabel yang digunakan utuk menyimpan node yang udah diproses/sudah dikunjungi 
    visited = set()

    #masukkan node awal ke queue  
    queue.append(start)

    #tandai node awal sebagat node yang sudah dikunjungi
    visited.add(start)
    
    while queue:
        #mengambil node paling depan dari queu
        node = queue.popleft()

        #tampilkan node yang sedang dikunjungi
        print(node, end=" ")
        
        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetannga sebelum dikunjungi
            if neighbor not in visited:
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #masukkan tetanng ke queue untuk diproses nanti
                queue.append(neighbor)

#menjalankan BFS dari node A
bfs(graph, 'A')