#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

# ==========================================================
# Latihan 2: Tracing Rekursi 
# Program ini menunjukkan kapan print "Masuk" dan print "Keluar" dijalankan
# ==========================================================
def countdown(n):
 # BASE CASE: kondisi berhenti (n = 0)
 if n == 0:
    print("Selesai")  # Ketika n=0, program berhenti
    return
 
 # Eksekusi ini SEBELUM pemanggilan diri (print "Masuk" pertama)
 print("Masuk:", n)
 
 # RECURSIVE CALL: memanggil diri dengan n lebih kecil
 countdown(n - 1)
 
 # Eksekusi ini SETELAH pemanggilan diri selesai (print "Keluar" kemudian)
 print("Keluar:", n)

# Masuk: 3 → Masuk: 2 → Masuk: 1 → Selesai → Keluar: 1 → Keluar: 2 → Keluar: 3
countdown(3)