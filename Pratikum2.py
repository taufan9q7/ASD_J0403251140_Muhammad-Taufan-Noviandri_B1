#===================================================
# Pratikum 2 : konsep ADT dan file handling (Studi Kasus)
# Latihan dasar 1 : Membuat fungsi load data
#===================================================

nama_file ='data_mahasiswa.txt'

# membuat fungsi untuk membaca data mahasiswa dari file
def baca_data_mahasiswa(nama_file):
    data_dict = {} # inisialisasi data dictionary
    with open('data_mahasiswa.txt', 'r', encoding= 'utf-8') as file:
     for baris in file:
        baris = baris.strip() #menghilang karakter baris baru

        parts = baris.split(',')
        if len(parts) != 3:
           continue                  # lewati baris yang tidak sesuai
        nim, nama, nilai_str = parts #pecah menjadi data satuan 
        nilai = int(nilai_str)
        data_dict[nim] = {
            'nama' : nama,
            'nilai' : int(nilai)
        }
        nim, nama, nilai = baris.split(',')
        data_dict
    return data_dict

# memanggil fungsi untuk membaca data mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
# print('jumlah data terbaca ', len(buka_data))

#=========================================================
# Pratikum 2 
# Latihan 2 : membuat fungsi menampilkan data
#=========================================================

def tampilkan_data(data_dict):
   
   if len(data_dict) == 0:
      print('data kosong')
      return
   
   # membuat header tabel
   print('\n======== DATA MAHASISWA =========')
   print(f'{'NIM' : <10} | {'Nama':<12} | {'Nilai':>5}')
   print('-' * 32)

   '''
   Untuk tampilkan yang rapi, atur f-string formating
        {'NIM' : <10} 
        artinya: tampilkan nim <= rata kiri dengan lebar 10 karakter
        {'Nama' :<12}
        artinya: tampilkan nama rata dengan lebar kolom 12 karakter
        {'Nilai' :>5} 
        artinya: tampilkan nilai rata kanan dengan lebar 5 karakter
   '''

   for nim in sorted(data_dict.keys()):
      nama = data_dict[nim]['nama']
      nilai = data_dict[nim]['nilai']
      print(f'{nim : <10} | {nama:<12} | {nilai:>5}')

# memanggil fungsi untuk menampilkan data
#tampilkan_data(buka_data)

#=====================================================
# Pratikum 2 : 
# Latihan 3 : membuat fungsi mencari data
#=====================================================

def cari_data(data_dict):
   # mencari data mahasiswa berdasarkan NIM
   nim_cari = input('Masukkan NIM yang dicari: ').strip()

   if nim_cari in data_dict:
       nama = data_dict[nim_cari]['nama']
       nilai = data_dict[nim_cari]['nilai']

       print('\n ===== DATA MAHASISWA DITEMNUKAN ====')
       print(f'NIM: {nim_cari}')
       print(f'nama: {nama}')
       print(f'Nilai: {nilai}')
   else:
       print('\n Data tidak ditemukan')

#cari_data(buka_data)

# ================================================
# Pratikum 2
# Latihan 4 : membuat fungsi update nilai
# ================================================

def update_nilai(data_dict):
   
   # cari nim mahasiswa yang akan diupdate nilainya
   nim = input('Masukkan NIM mahasiswa yang akan diupdate nilai: ').strip()

   if nim not in data_dict:
      print('NIM tidak ditemukan, update dibatalkan.')
      return  
   try:
      nilai_baru = int(input('Masukkan nilai baru (0-100): ').strip())
   except ValueError:
      print('Nilai harus berupa angka, update dibatalkan')
      return
   
   if nilai_baru < 0 or nilai_baru > 100:
      print('Nilai harus antara 0-100. update dibatalkan')

   nilai_lama = data_dict[nim]['nilai']
   # Memasukkan nilai update baru ke dictionary\
   data_dict[nim]['nilai'] = nilai_baru

   print('update berhasil. nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}')

#update_nilai(buka_data)

# ================================================
# Pratikum 2
# Latihan 5 : membuat fungsi menyimpan perubahan data ke file 
# ================================================

def simpan_data_ke_file(nama_file, data_dict):
   with open(nama_file, 'w', encoding='utf-8') as file: 
      for nim in sorted(data_dict.keys()):
         nama = data_dict[nim]['nama']
         nilai = data_dict[nim]['nilai']
         file.write(f'{nim},{nama},{nilai}\n')
 
# simpan_data_ke_file(nama_file, buka_data)
# print('Data berhasil disimpan')

# ================================================
# Pratikum 2
# Latihan 6 : membuat menu program
# ================================================

def main():
   #Menjalankan fungsi 1 load data
   buka_data = baca_data_mahasiswa(nama_file)

while True:
   print('\n=== MENU DATA MAHASISWA ===')
   print('1. Tampilkan semua data')
   print('2. Cari data berdasarkan NIM')
   print('3. Update nilai mahasiswa')
   print('4. Simpan data ke file')
   print('0. keluar')

   pilihan = input('Pilihan menu: ')

   if pilihan == '1':
      tampilkan_data(buka_data)

   elif pilihan == '2':
      cari_data(buka_data)
      
   elif pilihan == '3':
      update_nilai(buka_data)
   elif pilihan == '4':
      simpan_data_ke_file(buka_data)
   elif pilihan == '0':
      print('program selesai')
      break
   else:
      print('print tidak valid. coba lagi')

if __name__ == '__main__':
 main()

# ======================= END ==============================