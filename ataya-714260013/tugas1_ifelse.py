# ===============================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : Ataya Mahardika
# NIM   : 71420013
# Kelas : 1A
#================================================

GARIS = "=" * 45

print(GARIS)

try:
    nilai = float(input("Masukkan nilai akhir (0 - 100): "))
except ValueError:
    nilai = None

if nilai is None:
    print("ERROR: Input tidak valid. Harap masukkan angka.")
elif nilai < 0 or nilai > 100:
    print("ERROR: Masukkan angka antara 0 sampai 100")
else:
    if nilai >= 85:
        huruf = "A"
    elif nilai >= 75:
        huruf = "B"
    elif nilai >= 60:
        huruf = "C"
    elif nilai >= 50:
        huruf = "D"
    else:
        huruf = "E"

    if huruf in ("A", "B", "C"):
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print(f"Nilai Akhir : {nilai:g}")
    print(f"Huruf Mutu  : {huruf}")
    print(f"Status      : {status}")

print(GARIS)