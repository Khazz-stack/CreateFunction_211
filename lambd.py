import math

luas_lingkaran = lambda r: math.pi * r ** 2

jari_jari = float(input("Masukkan jari-jari: "))

if jari_jari >= 0:
    hasil = luas_lingkaran(jari_jari)
    print(f"Luas lingkaran: {hasil:.2f}") #:.2f digunakan untuk membulatkan angka desimal menjadi 2 angka di belakang koma.
else:
    print("Jari-jari tidak boleh negatif.")