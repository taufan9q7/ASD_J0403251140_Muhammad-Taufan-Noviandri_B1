def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

data = [5, 2, 4, 6, 1, 3]
hasil = insertion_sort(data)
print("Hasil akhir:", hasil)

# soal
# 1. Tuliskan isi list setelah iterasi i = 1.
# 2. Tuliskan isi list setelah iterasi i = 3.
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4?

# Jawaban:
# 1. [2, 5, 4, 6, 1, 3]

# 2. [2, 4, 5, 6, 1, 3]

# 3. terjadi 4 kali pergeseran, karena angka 1 lebih kecil dari 6, 5, 4, dan 2,
# jadi semua digeser ke kanan dulu sebelum 1 masuk ke depan.


