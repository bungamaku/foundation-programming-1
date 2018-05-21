#Bunga Amalia Kurniawati - 1706022104
#Lab 2 - DDP 1 kelas D, 15 September 2017
#PENEBUSAN​ ​DOSA​ ​BENNY

#Masukkan input kalimat surgawi dari user
desimal = int(input('Masukkan kalimat surgawi: '))

#Membuat string kosong untuk menyimpan hasil sementara
akhir = ""

#Mengubah desimal basis 10 menjadi basis 2
if desimal == 0 :
    print('Makna duniawi: P')  #Pengecualian jika input user '0'
else :
    while desimal > 0 :
        if desimal % 2 == 0 :
            akhir += 'P'  #Mengubah nilai 0 menjadi P
        else :
            akhir += 'B'  #Mengubah nilai 1 menjadi B
        desimal = desimal // 2  #Mengubah patokan untuk menjalankan while
    print('Makna duniawi:', akhir[::-1])  #Menulis output makna duniawi
    


   
