print("==================")
print("KALKULATOR SEDERHANA")
print("==================")
print("operasi tersedia:+, -, *, /")
print("==================")
angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))
operasi = input("Masukkan operasi (+, -, *, /): ")
print("==================")
if operasi == "+":
    hasil = angka1 + angka2
    print(f"Hasil dari {angka1} + {angka2} = {hasil}")
elif operasi == "-":
    hasil = angka1 - angka2
    print(f"Hasil dari {angka1} - {angka2} = {hasil}")
elif operasi == "*":
    hasil = angka1 * angka2
    print(f"Hasil dari {angka1} * {angka2} = {hasil}")
elif operasi == "/":
    if angka2 == 0:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
    elif angka1 == 0:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else: 
         hasil = angka1 / angka2
  
         print(f"Hasil dari {angka1} / {angka2} = {hasil}")
    
else:
    print("operasi tidak dikenal")
    print("gunakan salah satu dari operasi yang tersedia: +, -, *, /")

print("==================")
print("terimakasih telah menggunakan kalkulator sederhana ini")