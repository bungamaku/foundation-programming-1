#Bunga Amalia Kurniawati - 1706022104
#Lab 4 DDP Kelas D - 29 September 2017
#Secret​ ​Agent​ ​069​ ​Benny

import re

#Meminta input nama file dari user
masukan, keluaran = input("Masukkan nama file input dan output: ").split(" ")

try:
    file_masukan = open(masukan, "r") #Membaca file masukan
    file_keluaran = open(keluaran, "w") #Menyiapkan file keluaran

    kalimat = file_masukan.read() #Membaca string dalam file

    sampah = ",+|!+|-+|/+|;" #Karakter yang ingin dibuang

    kalimat = re.split(sampah, kalimat) #Membuang karakter yang ingin dibuang
    kalimat = ''.join(kalimat) #Menjadikannya string kembali
    kalimat = kalimat.replace('\n', ' ') #Pengecualian untuk enter dan titik
    kalimat = kalimat.replace('.', '')
    kalimat = kalimat.split('<start>') #Memisahkan <start>

    pesan = ''

    for kata in kalimat:
        if '<end>' in kata: #Mencari kalimat mana yang ada <end>
            kata = kata.split('<end>') #Memisahkan <end>
            pesan += kata[0] #Memasukan pesan sebelum <end> ke kumpulan pesan

    print(pesan, file = file_keluaran) #Mengeprint di file keluaran
    print('Rahasia telah terbongkar, silakan cek file', keluaran) #Mengeprint di IDLE

    file_masukan.close() #Menutup file
    file_keluaran.close()
except(FileNotFoundError, IOError):
    print('File', masukan, 'bermasalah! Benny lolos kali ini.') #Jika error, mengeprit di IDLE

