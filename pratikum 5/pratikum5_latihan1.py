#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

# ==========================================================
# Latihan 1: Rekursi Pangkat - Menghitung a^n
# Alur: a^n = a * a * a ... (n kali)
# ==========================================================

def pangkat(a, n):
    # BASE CASE: kondisi berhenti rekursi
    # Return 1 karena: a^0 = 1 (aturan matematika)
    # Contoh: 2^0 = 1, 5^0 = 1, dst
    # Jika return 0 atau angka lain, hasil perkalian jadi salah
    if n == 0:
     return 1
    # RECURSIVE CALL: a^n = a * a^(n-1) - problem dibagi jadi lebih kecil
    return a * pangkat(a, n - 1)

print(pangkat(2, 4))  # Output: 16