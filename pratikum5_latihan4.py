#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

# ==========================================================
# Latihan 4: Kombinasi Huruf 
# ==========================================================
def kombinasi(n, hasil=""):
    """
    Fungsi rekursi yang membuat kombinasi A dan B
    n: panjang kombinasi yang diinginkan
    hasil: string kombinasi yang sedang dibangun (default kosong)
    """
    
    # BASE CASE: panjang hasil sudah sesuai target
    # Ketika selesai, print hasil dan berhenti
    if len(hasil) == n:
        print(hasil)
        return
    
    # RECURSIVE CASE: membuat 2 cabang (binary tree)
    # Cabang 1: tambah "A" dan panggil diri sendiri
    # Cabang 2: tambah "B" dan panggil diri sendiri
    # Contoh kombinasi(2) menghasilkan: AA, AB, BA, BB
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)