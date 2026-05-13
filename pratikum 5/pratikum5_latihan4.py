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
    Fungsi rekursif untuk menghasilkan semua susunan huruf A dan B
    n     : panjang kombinasi yang diinginkan
    hasil : string yang sedang dibentuk (awal kosong)
    """
    # BASE CASE:
    # jika panjang string sudah sama dengan n,
    # berarti kombinasi sudah lengkap → tampilkan hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # RECURSIVE CASE: membuat 2 cabang (binary tree)
    # Cabang 1: tambah "A" dan panggil diri sendiri
    # Cabang 2: tambah "B" dan panggil diri sendiri
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

# menjalankan fungsi
kombinasi(2)