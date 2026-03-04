def insertion_sort(data):
    for i in range(1, len(data)):
       key = data[i]
       j = i - 1

    while j >= 0 and data[j] < key:
       data[j + 1] = data[j]
       j -= 1

    data[j + 1] = key

    return data

# Soal:
# 1. Lengkapi kondisi agar menjadi sorting ascending.
# 2. Ubah agar menjadi descending.

# Jawaban:
# 1. tanda > supaya kalau data sebelumnya lebih besar dari key,
# maka digeser ke kanan. Hasilnya urut dari kecil ke besar.

# 2. tanda < supaya kalau data sebelumnya lebih kecil dari key,
# maka digeser ke kanan. Hasilnya urut dari besar ke kecil.