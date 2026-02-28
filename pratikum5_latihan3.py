#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum Secara Rekursif
# Program ini membandingkan elemen satu per satu dari belakang
# ==========================================================

def cari_maks(data, index=0):
    """
    Mencari nilai maksimum dari list menggunakan rekursi
    data: list angka
    index: posisi elemen yang sedang dicek (dimulai dari 0)
    """
    
    # BASE CASE: ketika sudah mencapai elemen terakhir list
    # Kondisi: index == panjang list - 1
    # Return: elemen terakhir (tidak ada lagi yang dibanding)
    if index == len(data) - 1:
        return data[index]
    
    # RECURSIVE CASE: cari max dari elemen setelah index sekarang, 
    # lalu bandingkan dengan elemen sekarang
    maks_sisa = cari_maks(data, index + 1)
    
    # Return elemen sekarang atau max dari sisa, mana yang lebih besar
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))