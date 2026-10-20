print("===================================")
print("     KALKULATOR KONSOL SEDERHANA")
print("===================================")
print("Operasi tersedia: + - * /")

angka1 = float(input("Masukan bilangan pesrtama : "))
angka2 = float(input("Masukan bilang kedua: "))
operator = input("Masukan operator(+ - * /): ")


print("------------------------------------")

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} x {angka2} = {hasil:.2f}")


elif operator == "/":
    if angka2 == 0:
        print("Kesalahan bilangan tidak dapat di bagi dengan nol.")
    else:
        hasil = angka1 / angka2

else:
    print(f"Operator '{operator}' tidak dikenali.")
    print("Gunakan salah satu dari: + - * /")

print("=================================")
print("Terima kasih telah menggunakan kalkulator ini.")
