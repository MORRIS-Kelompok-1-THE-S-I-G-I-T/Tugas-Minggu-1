#==================================
#Tugas IF ELSE
#Nama: [Muhammad Sajid Algani]
#NIM: [714260014]
#Kelas: [D4 kelas 12]
#================================

# TUGAS IFELSE
print("=" * 45)
print("PROGRAM KONVERSI NILAI ANGKA KETIKA HURUF MUTU")
print("-" * 45)

# Pembatas 
print("-" * 45)

# 2. Input Nilai dari Program
input_user = input("Masukkan nilai akhir Anda: ")
nilai = float(input_user)

# 3. Logika Percabangan (baris 21-34)
if nilai < 0 or nilai > 100:
    print(f"Error: Nilai {nilai} di luar rentang! Masukkan angka 0 hingga 100.")
elif nilai >= 85:
        huruf_mutu = "A"
        keterangan = "Lulus"
elif nilai >= 70:
         huruf_mutu = "B"
         keterangan = "Lulus"
elif nilai >= 55:
         huruf_mutu = "D"
         keterangan = "Tidak Lulus"
elif nilai >= 40:
         huruf_mutu = "E"
         keterangan = "Tidak Lulus"
else:
         huruf_mutu = "T"
         keterangan = "Tidak Lulus"
# 4. Menampilkan Hasil Menggunakan f-string (Hanya jika nilai valid)
if 0 <= nilai <= 100:
    print(f"Nilai Angka : {nilai}")
    print(f"Huruf Mutu : {huruf_mutu}")
    print(f"Keterangan : {keterangan}")

# Tampilan Konsol: Pesan Penutup
print("-" * 45) # Pemisah
print("Terima kasih telah menggunakan program ini")
print("=" * 45)