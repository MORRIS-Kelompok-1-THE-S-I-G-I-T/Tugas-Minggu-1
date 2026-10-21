# ==========================================
# Latihan 1 - Kalkulator Konsol Sederhana
# Pelatihan Dasar Pemrograman MORRIS IF 26
#===========================================

print("=====================================")
print(" KALKULATOR KONSOL SEDERHANA")
print("=====================================")
print("operasi tersedia + - * /")
print("-------------------------------------")

# --- Bagian masukan Pengguna ---
angka1 = float(input("masukan bilangan pertama : "))
angka2 = float(input("masukan bilangan kedua : "))
operator = input("masukan operator (+ - * /): ")

print("--------------------------------------")

# --- Bagian Proses ---
if operator == "+":
    hasil = angka1 + angka2
    print(f"hasil: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasil: {angka1} - {angka2} = {hasil:.2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print (f"hasil: {angka1} x {angka2}= {hasil:.2f}")

elif operator == "/":
    if angka2 == 0:
        print("kesalahan: bilangan tidak dapat dibagi dengan nol.")
    else:
        hasil = angka1 / angka2
        print(f"hasil: {angka1} : {angka2} = {hasil:.2f}")

else:
    print(f"operator '{operator}' tidak dikenali.")
    print("Gunakan salah satu dari: + - * /")

print("============================================")
print("Terima kasih telah menggunakan kalkulator ini.")
