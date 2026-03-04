#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

# Insertion sort dengan tracing

#==========================================

def insertion_sort(data):

        # Melihat data awal
        print("data awal : ", data)
        print("=" * 50)

            #loop mulai dari data ke 2 (index array ke 1)
        for i in range(1, len(data)):

            key = data[i] #simpan nilai yang disisipkan
            j = i - 1 #index elemen terakhir di bagian kiri

            print("Iterasi ke-", i)
            print("Nilai key = ", key)
            print("Bagian kiri (terurut): ", data[:i])
            print("Bagian kanan (belum terurut): ", data[i:])
            print("-" * 50)
        
        
        while j >= 0 and data[j] > key: #bandingkan dengan elemen di bagian kiri
            data[j + 1] = data[j] #geser elemen ke kanan
            j -= 1 #pindah ke elemen sebelumnya

        # sisipkan key pada posisi yang benar
            data[j + 1] = key
            print("Setelah disisipkan: ", data)
            print("-" * 50)
        return data 

angka = [7, 8, 5, 2, 4, 6]
print("Hasil Sorting : ", insertion_sort(angka))
