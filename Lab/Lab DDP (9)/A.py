#Bunga Amalia Kurniawati - 1706022104
#Lab 9 DDP Kelas D - 24 November 2017
#Kompresi Benny

def kompresi(s):
#Membuat base case apabila string kosong atau hanya berisi 1 huruf
	if len(s) <= 1:
		return s
	else:
#Apabila menemukan huruf yang sama, akan membuang huruf tersebut dan mengecek huruf selanjutnya
		if s[0] == s[1]:
			return kompresi(s[1:])
#Apabila menemukan huruf yang tidak sama, huruf disimpan lalu mengecek huruf selanjutnya
		else:
			return s[0] + kompresi(s[1:])

#Memintra input dari user
masukan = input()
print('Hasil kompresinya adalah ' + kompresi(masukan))
