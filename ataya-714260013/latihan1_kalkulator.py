print("===============================")
print("    KALKULATOR KONSOL SEDERHANA    ")
print("===============================")
print("Operasi tersedia: + - * /")
print("-------------------------------")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operasi = input("Masukkan operasi (+, -, *, /): ")
print("-------------------------------")
if operasi == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")

elif operasi == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operasi == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operasi == "/":
    if angka2 == 0: 
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
    elif angka1 == 0:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
    else:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
else:
    print("Operasi tidak valid!")
    print("Silakan pilih operasi yang tersedia: +, -, *, /")

print("-------------------------------")
print("Terima kasih telah menggunakan kalkulator sederhana ini!")