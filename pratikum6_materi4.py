#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

# Merge Sort (Ascending)

#==============================

def merge_sort(data,depth = 0):
    indent='' * depth #Indentasi berdasarkan level rekursif
    print(f'{indent}merge_sort({data})')
    
    #Base case
    if len(data) <= 1:
        return data

    #Membagi data menjadi 2 bagian
    mid = len(data) // 2
    left = data[:mid] #Slicing bagian kiri
    right = data[mid:] #Slicing bagian kanan

    print(f'{indent}divide -> left = {left} | right = {right}')

    #Recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged=merge(left_sorted,right_sorted)
    print(f'{indent}merge -> {left_sorted} + {right_sorted} = {merged}')

    return merge(left_sorted, right_sorted)

def merge(left,right):
    result = []
    i=0
    j=0

    #Membandingkan elemen kiri dan kanan
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    #Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result

angka = [13,7,28,5,19,36,4]
print('Hasil sorting: ', merge_sort(angka))