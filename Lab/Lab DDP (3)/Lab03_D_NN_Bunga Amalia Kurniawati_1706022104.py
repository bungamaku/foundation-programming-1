#Bunga Amalia Kurniawati - 1706022104
#Lab 3 DDP Kelas D - 22 September 2017
#Classic Cryptography

#Meminta input user
pesan_awal = input('Masukkan operasi: ').split()

#Mengubah besaran geser
geser = int(pesan_awal[0])

#Mengubah isi pesan awal yang akan diubah
pesan_awal = " ".join(pesan_awal[1:])

#Mengubah isi pesan
pesan_akhir = ""
for x in pesan_awal:
    if (x == ' '): #Pengecualian untuk spasi
        pesan_akhir += " "
    else:
        pesan_akhir += chr((ord(x) - geser-97) % 26 + 97)

#Mengeprint output
print('Kalimat aslinya adalah:', pesan_akhir)


