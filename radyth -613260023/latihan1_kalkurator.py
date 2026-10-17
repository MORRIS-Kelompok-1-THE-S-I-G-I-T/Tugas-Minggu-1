#=========================================
#latihan 1 - kalkulator konsor sederhana
#pelatihan dasar pemrograman MORRIS IF 26
#=========================================

print("===================================")
print("     KALKULATOR KONSOR SEDERHAMA")
print("===================================")
print("operasi tersedia: +  -   *   /")
print("===================================")

#--- bagian masukan pengguna ---
angka1 = float (input("Masukan bilangan pertama: "))
angka2 = float (input("Mmasukan bilangan kedua : "))
operator = input("masukan operator (+ - * /) ")

print("----------------------------------")

# --- Bagian proses ---
if operator == "+":
    hasil = angka1 + angka2
    print(f"hasil: {angka1} + {angka2} = {hasil:.2f}")

elif opertaor == "_":
    hasil = angka1 - angka2
    print(f"hsil: {angka1} - {angka2} = {hasil:.2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"hasil: {angka1} x {angka2} = {hasil:.2f}")

elif operator =="/":
    if angka2 == 0:
        print("kesalahan: bilangan tidak dapat dibagi dengan nol.")
    else:
        hasil = angka1 / angka2
        print(f"hasil: {angka1} : {angka2} = {hasil:.2f}")

else:
    print(f"operator '{operator}' tidak dikenali.")
    print("gunakan salah satu dari: + - * /")

    print("==============================")
    print("terima kasih telah menggunakan kalkulator ini.")