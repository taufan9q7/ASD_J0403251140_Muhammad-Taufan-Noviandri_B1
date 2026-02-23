# ==========================================================
# Nama : Muhammad Taufan Noviandri
# NIM : J0403251140
# Kelas : TPL - B1
# ==========================================================

#=================================================
# Pratikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 1A : Membaca seluruh isi file
#=================================================

# Membuka file dengan mode read ("r")

# Membuka file dalam satu string
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()                                     # Membaca keseluruhan isi file dalam satu string
print(isi_file)    
print("=========== Hasil Read =============")
print("Tipe Data: ", type(isi_file))    #
print("Jumlah Karakter", len(isi_file))
print("Jumlah Baris", isi_file.count("\n")+1)

# Membuka file per baris
print ('========== Membaca file per baris ==========')
jumlah_baris = 0
with open('data_mahasiswa.txt',"r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()          # Menghilangkan baris baru \n
        print('Baris ke-', jumlah_baris)
        print ('isinya :', baris)

#=========================================================
# Pratikum 1 : Konsep ADT dan file handling
# Latihan dasar 2 : Parsing baris menjadi kolom data
#=============================================================

with open('data_mahasiswa.txt','r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        print('NIM :', nim, '| Nama:', nama, '| Nilai: ', int(nilai))

#===========================================================
# Pratikum 1 : Konsep ADT dan file handling
# Latihan Dasar 3 : Membaca file dan menyimpan ke list
#===========================================================

data_list = [] # List untuk menampung data mahasiswa

with open('data_mahasiswa.txt','r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',') # pecah menjadi data satuan
        data_list.append([nim,nama,int(nilai)])    # Simpan sebagai list  "[nim,nama,nilai]"

print('============== Data mahasiswa dalam list ==============')
print (data_list)

print('============== Jumlah record dalam list ===============')
print ('Jumlah record', len(data_list))

print('======== Menampilkan data record tertentu =======')
print('Contoh record pertama: ', data_list[0])  # Array dimulai dari 0 

#=====================================
# Pratikum 1: Konsep ADT dan file handling
# Latihan dasar 4: Membaca file dan menyimpan file ke dictionary
#=====================================

data_dict = {}       # buat variabel untuk dictionary
with open('data_mahasiswa.txt','r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        # Simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim] = {        # Key
            'nama': nama,         # Values
            'nilai': int(nilai)   # Values
        }
print('========= Data mahasiswa dalam dictionary =========')
print(data_dict)

#=========================== END =================================