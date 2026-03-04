def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
     
    while j >= 0 and data[j] > key:
       data[j + 1] = data[j]
       j -= 1
       
    data[j + 1] = key

    return data

 #Soal:
# 1. Mengapa perulangan dimulai dari indeks 1?
# 2. Apa fungsi variabel key?
# 3. Mengapa digunakan while, bukan for?
# 4. Operasi apa yang terjadi di dalam while?

# jawaban:
# 1. Karena indeks 0 dianggap sudah terurut, jadi mulai dari indeks 1.
# 2. key untuk menyimpan nilai yang mau dipindahkan ke posisi yang benar.
# 3. Karena jumlah pergeseran tidak pasti, jadi pakai while berdasarkan kondisi.
# 4. Terjadi perbandingan dan pergeseran elemen ke kanan sampai posisi key pas.
