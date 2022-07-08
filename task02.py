# import library python
from os import system, name

# kode warna
rt = '\033[0m'
yl = '\033[93m'
lc = '\033[96m'
gr = '\033[32m'
pu = '\033[35m'
lr = '\033[91m'

# fungsi clear terminal
def clear():
    # jika os windows
    if name == 'nt':
        _ = system('cls')

    # jika os mac / linux
    else:
        _ = system('clear')

# trigger clear terminal
clear()

# fungsi cek inputan user
def cek(inputan):

    # inisiasi looping
    valid = False
    
    # meminta input dari user + mengecek apakah tipe inputan integer atau bukan
    while not valid:
        try:
            masukan = int(input("\t{}[{}?{}] Masukkan nilai {} : {}" .format(rt,yl,rt,inputan,lc)))
            valid = True 
        except ValueError:
            print("\t{}[{}!{}] Hanya menerima input angka! silahkan ulangi!" .format(rt,lr,rt))

    # mengembalikan nilai masukan
    return masukan

# dekorasi
print("\n\t{}------------------------{} Input Data {}-------------------------\n" .format(pu,rt,pu))

# meminta input dari user lewat fungsi cek
x = cek("x")
y = cek("y")
z = cek("z")

# dekorasi
print("\n\t{}-----------------------{} Output Data {}-------------------------" .format(pu,rt,pu))

# membuat variable hasil perkalikan x, y, dan z
hasil = x * y * z

# menampilkan output
print("\n\t{}[{}√{}] Hasil dari perkalian {} * {} * {} =" .format(rt, gr, rt, x, y, z), hasil, rt)
