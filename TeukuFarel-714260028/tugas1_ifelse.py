# ===================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : Teuku Farel Febriansyah
# NIM   : 714260028
# Kelas : 12
# ===================================================

print("===================================")
print("     CEK KELULUSAN NILAI MATKUL    ")
print("===================================")

nilai = float(input("Masukin Nilai 0-100 : "))
print("-----------------------------------")

if nilai < 0 or nilai > 100:
    print("Nilai yang dimasukin tidak benar. Masukan nilai antara 0-100.")

elif nilai >= 80:
    print(f"Kamu lulus dengan nilai A")
elif nilai >= 70:
    print(f"Kamu lulus dengan nilai B")
elif nilai >= 60:
    print(f"Kamu lulus dengan nilai C")
elif nilai >= 50:
    print(f"Kamu tidak lulus dengan nilai D")
else:
    print(f"Kamu tidak lulus dengan nilai E")

    
print("===================================")
print("Hatur Nuhun Dulur")