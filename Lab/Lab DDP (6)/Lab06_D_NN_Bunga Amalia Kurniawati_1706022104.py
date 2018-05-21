#Bunga Amalia Kurniawati - 1706022104
#Lab 6 DDP Kelas D - 27 Oktober 2017
#Benny’s Plagiarism Filter

#Membuat list untuk menyimpan set
list_set = []

#Meminta input banyaknya jumlah set
jumlah_submisi = int(input())

#Memisahkan input menjadi satuan integer, lalu memasukkannya ke dalam list
for i in range(jumlah_submisi):
    submisi = input().replace(' ', '')
    submisi = submisi[1:len(submisi)-1].split(',')      
    for j in submisi:
        list_set.append(j)

#Mengeluarkan output berupa set baru    
print({int(x) for x in list_set if list_set.count(x) == 1})

