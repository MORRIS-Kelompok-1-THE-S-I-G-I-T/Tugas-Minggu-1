# ==================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : Alyssa ivana purnama
# NIM   : 613260001
# Kelas : D3 TI 1A
# ==================================================

try:
    nilai = float(input("Masukkan nilai (0 - 100): "))
except ValueError:
    nilai = None

print("====================================")

if nilai is None:
    print("Error: input tidak valid, harap masukkan angka")
elif nilai < 0 or nilai > 100:
    print("Error: masukkan angka antara 0 sampai dengan 100")
else:
    if nilai >= 95:
        huruf = "A"
        status = "LULUS"
    elif nilai >= 80:
        huruf = "B"
        status = "LULUS"
    elif nilai >= 75:
        huruf = "C"
        status = "LULUS"
    elif nilai >= 60:
        huruf = "D"
        status = "Tidak Lulus"
    else:
        huruf = "E"
        status = "Tidak Lulus"

    print(f"Nilai Anda : {nilai:.1f}")
    print(f"Huruf Mutu : {huruf}")
    print(f"Status : {status}")

print("====================================")
print("Terima Kasih telah menggunakan program ini.")  
          