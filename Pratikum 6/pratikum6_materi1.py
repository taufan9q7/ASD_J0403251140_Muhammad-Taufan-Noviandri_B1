#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

# Insertion sort (Ascending)

#==========================================

def insertion_sort(data):
    #loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):
        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri

        
        while j >= 0 and data[j] > key: #bandingkan dengan elemen di bagian kiri
            data[j + 1] = data[j] #geser elemen ke kanan
            j -= 1 #pindah ke elemen sebelumnya
        # sisipkan key pada posisi yang benar
        data[j + 1] = key
    return 

angka = [7, 8, 5, 2, 4, 6]
print("Hasil Sorting : ", insertion_sort(angka))
