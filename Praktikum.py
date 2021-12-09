from PrettyTable import PrettyTable

print("Nama : Indira Rully Pricilia")
print("NIM : 312110354")
print("Kelas : TI.21.CA.1")
print("===========================")
print("Praktikum - Modul Praktikum")
print()

daftar = []
stop = False 

# Mengisi Nilai
while not stop:
     nama = input("Masukkan Nama : ")
     nim = input("Masukkan NIM : ")
     tugas = input("Masukkan Nilai Tugas : ")
     uts = input("Masukkan Nilai UTS : ")
     uas = input("Masukkan Nilai UAS : ")
     nilai_akhir = 0.3 * float(tugas) + 0.35 * float(uts) + 0.35 * float(uas)
     daftar.append([nama, nim, tugas, uts, uas, nilai_akhir])
         
     tanya = input("Tambah data? (y/n) : ")
     if tanya == "n":
        stop = True

# Cetak semua nilai
print("==============================")
print()

x = PrettyTable()
i = 0

for data in daftar:
     i += 1
     x.field_names = ["No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"]
     x.add_row([i, data[0], data[1], data[2], data[3], data[4], data[5]])
print(x)
