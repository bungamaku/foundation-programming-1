#Bunga Amalia Kurniawati - 1706022104
#Lab 9 DDP Kelas D - 24 November 2017
#Angka Cantik Versi Benny

def angka_cantik(bil):
#Membuat base case apabila masukan sudah termasuk angka cantik
	if int(bil) <= 9:
		return bil
#Membuat rekursif dengan mengeluarkan digit yang pertama
	else:
		bil = str(bil)
		return angka_cantik(int(bil[0]) + angka_cantik(int(bil[1:])))

#Meminta input dari user
bil = input()
print(angka_cantik(bil))