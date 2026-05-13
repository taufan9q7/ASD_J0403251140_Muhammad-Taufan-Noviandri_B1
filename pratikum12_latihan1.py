#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
# Praktikum 12 - Graph II: Shortest Path
#=============================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

print(f"Jalur 1: A -> B -> D = {jalur_1}")
print(f"Jalur 2: A -> C -> D = {jalur_2}")

# Menentukan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# soal:
# 1. Berapa total bobot jalur A -> B -> D?
# 2. Berapa total bobot jalur A -> C -> D?
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?

# Jawaban:
# 1. Total bobot jalur A -> B -> D adalah 4 (A ke B) + 5 (B ke D) = 9.
# 2. Total bobot jalur A -> C -> D adalah 2 (A ke C) + 1 (C ke D) = 3.
# 3. Jalur terpendek yang dipilih adalah A -> C -> D karena total bobotnya lebih kecil (3) dibandingkan A -> B -> D (9).
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit karena bobot pada setiap edge bisa berbeda.
# Misalnya, meskipun A -> B -> D memiliki lebih sedikit edge (2 edge) dibandingkan A -> C -> D (2 edge), 
# bobot totalnya lebih besar karena bobot pada edge A ke B dan B ke D lebih tinggi daripada bobot pada edge A ke C dan C ke D.

