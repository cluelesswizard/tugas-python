# import library python
from os import system, name

# kode warna
rt = '\033[0m'
yl = '\033[93m'
lc = '\033[96m'
gr = '\033[32m'
pu = '\033[35m'

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

# dekorasi
print("\n\t{}------------------------{} Input Data {}-------------------------" .format(pu,rt,pu))

# meminta input dari user
nama = input("\n\t{}[{}?{}] Masukkan nama anda    : {}" .format(rt,yl,rt,lc))
kelas = input("\t{}[{}?{}] Masukkan kelas anda   : {}" .format(rt,yl,rt,lc))
jurusan = input("\t{}[{}?{}] Masukkan jurusan anda : {}" .format(rt,yl,rt,lc))

# dekorasi
print("\n\t{}-----------------------{} Output Data {}-------------------------" .format(pu,rt,pu))

# menampilkan output
print("\n\t{}[{}√{}] Nama    : {}" .format(rt,gr,rt,yl) + nama)
print("\t{}[{}√{}] Kelas   : {}" .format(rt,gr,rt,yl) + kelas)
print("\t{}[{}√{}] Jurusan : {}" .format(rt,gr,rt,yl) + jurusan + rt)
