#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

# ==========================================================
# Studi Kasus: Generator PIN - Membuat Semua Kombinasi PIN
# ==========================================================

# ALUR EKSEKUSI:
# Setiap level rekursi menambah 1 digit
# Level 1: "" → "0", "1", "2"
# Level 2: "0" → "00", "01", "02" | "1" → "10", "11", "12" | "2" → "20", "21", "22"
# Level 3: semua hasil di-print karena sudah panjang 3

def buat_pin(panjang, hasil=""):
    """
    panjang: target panjang PIN
    hasil: PIN yang sedang dibangun
    """
    
    # BASE CASE: berhenti ketika PIN sudah lengkap
    # Kondisi: panjang hasil == panjang target
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # RECURSIVE CASE: 
    # Loop 3 kali untuk setiap pilihan angka (0, 1, 2)
    # Setiap iterasi membuat cabang baru dengan menambah 1 digit
    # Proses terus sampai panjang PIN sesuai target (base case)
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)