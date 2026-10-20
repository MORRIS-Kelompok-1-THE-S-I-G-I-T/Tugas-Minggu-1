# ==================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : (Hafsoh Zahidah Nafisah)
# NIM   : (714260031)
# Kelas : (1B)
# ==================================================

GARIS = "=" * 45

print(GARIS)
print("   PROGRAM KONVERSI NILAI AKHIR KE HURUF MUTU")
print(GARIS)

try:
    nilai = float(input("Masukkan nilai akhir (0 - 100): "))
except ValueError:
    nilai = None

print("-" * 45)

if nilai is None:
    print("ERROR: Masukkan angka antara 0 sampai 100")
elif nilai < 0 or nilai > 100:
    print("ERROR: Masukkan angka antara 0 sampai 100")
else:
    if nilai >= 80:
        huruf = "A"
    elif nilai >= 70:
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
print("Terima kasih telah menggunakan program ini.")