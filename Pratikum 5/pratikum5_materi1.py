#===========================================
# Nama: Muhammad Taufan Noviandri
# NIM: J0403251140
# Kelas: TPL - B1
#===========================================

#===========================================
# Materi Rekursif : Faktorial
# Recursive case => 3! = 3 * 2 * 1
# Base case => 0 berhenti
#===========================================

def faktorial(n):
    
    #base case
    if n == 0: 
        return 1

    # recursive case
    return n*faktorial(n-1) #n-1*n-2*n-3*......n-?

print("=============Program Faktorial=============")
print("Faktorial 3 adalah : ", faktorial(3))
