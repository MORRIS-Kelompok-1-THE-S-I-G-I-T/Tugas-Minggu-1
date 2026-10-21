GARIS = "=" * 45
GARNIS = "-" * 45

def minta_operasi(pesan):
    while True:
        operasi = input(pesan).strip()
        if operasi in ["+", "-", "*", "/"]:
            return operasi
        print("Operasi tidak valid! Silakan pilih: +, -, *, /")

def minta_angka(pesan):
    while True:
        try:
            return float(input(pesan).strip().replace(",", "."))
        except ValueError:
            print("Input tidak valid! Masukkan angka, contoh: 6, 9 atau 6.7")


print(GARIS)
print("    KALKULATOR KONSOL SEDERHANA    ")
print(GARIS)
print("Operasi tersedia: + - * /")
print(GARNIS)

angka1 = minta_angka("Masukkan angka pertama: ")
angka2 = minta_angka("Masukkan angka kedua: ")
operasi = minta_operasi("Masukkan operasi (+, -, *, /): ")
print(GARNIS)

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
        print("Tidak terdefinisi")
    else:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
else:
    print("Operasi tidak valid!")
    print("Silakan pilih operasi yang tersedia: +, -, *, /")

print(GARNIS)
print("Terima kasih telah menggunakan kalkulator sederhana ini!")