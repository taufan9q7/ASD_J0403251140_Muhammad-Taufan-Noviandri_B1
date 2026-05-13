#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

#===========================================
# Materi Rekursif : menjumlahkan bilangan elemen list
#===========================================

def jumlahkan_list(data, index):
    #base case
    if index == len(data):
        return 0

    #recursive case
    return data[index] + jumlahkan_list(data, index + 1)

print("=============Program Jumlahkan List=============")
print("Penjumlahan elemen list [2,4,5] = ", jumlahkan_list([2,4,5], 0))