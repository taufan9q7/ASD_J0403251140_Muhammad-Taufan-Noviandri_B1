#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

#===========================================
# Materi Rekursif : call stack
# Tracing bilangan (masuk-keluar)
# Input : 3
# 3-2-1 | 1-2-3
#===========================================

def hitung(n):

    #base case
    if n == 0:
        print("Selesai")
        return

    print("Masuk: ", n)
    hitung(n-1) # Recursive case
    print("Keluar: ", n)

print("=============Program Hitung=============")
hitung(3)


