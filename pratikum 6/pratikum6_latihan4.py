def merge_sort(data):
    if len(data) <= 1:
       return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

# Soal:
# 1. Apa yang dimaksud dengan base case?
# 2. Mengapa fungsi memanggil dirinya sendiri?
# 3. Apa tujuan fungsi merge()?

# jawaban:
# 1. Base case adalah kondisi berhenti rekursi.
# Pada kode ini: len(data) <= 1 karena data sudah terurut.

# 2. Fungsi memanggil dirinya sendiri untuk membagi data
# menjadi bagian lebih kecil sampai mencapai base case (rekursi).

# 3. Fungsi merge() bertujuan menggabungkan dua list
# yang sudah terurut menjadi satu list terurut.