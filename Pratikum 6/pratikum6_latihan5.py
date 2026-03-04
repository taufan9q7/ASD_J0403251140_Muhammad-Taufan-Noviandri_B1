def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Soal:
# 1. Lengkapi kondisi agar menjadi ascending.
# 2. Jelaskan fungsi result.extend().

# Jawaban:
# 1. Kondisi ascending: left[i] <= right[j]
# Supaya nilai lebih kecil masuk dulu (urut kecil ke besar) 

# 2. result.extend() untuk menambahkan sisa elemen
# yang belum dibandingkan ke dalam result.
