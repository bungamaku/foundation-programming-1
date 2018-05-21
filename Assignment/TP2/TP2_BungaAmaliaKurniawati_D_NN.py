#Tugas Pemrograman 2
#Bunga Amalia Kurniawati - Ilmu Komputer 1706022104
#Word Clouds    

#Mengimpor modul yang digunakan
import random
import string
import htmlFunctions    

#Mengeprint tulisan awal pembuka dan meminta input user
print('Program to create word cloud from a text file\nThe result is stored as an HTML file\n')
nama_file = input('Please enter the file name: ')   

#Membaca file masukan dan stopwords
try:
    file_teks = (open(nama_file, 'r')).read().lower().split()
    stop_words = (open('stopWords.txt', 'r')).read().strip().split('\n')    

#membuat list kosong dan variabel untuk menghitung atau membuang
    list_kata = []
    list_akhir = []
    list_stop = []
    hitung = 1
    batasan = 0
    dibuang = string.punctuation + string.digits

#Membuang whitespace dari stopwords
    for word in stop_words:
        list_stop.append(word.strip())

#Membuang punctuation, angka, dan stopwords dari list kata masukan
    for kata in file_teks:
        kata = ''.join(huruf for huruf in kata if huruf not in dibuang)
        if (kata not in list_stop and kata != ''):
            list_kata.append(kata)  

#Mengurutkan list berdasarkan alfabet
    list_kata.sort()    

#Mengecek dan menghitung frekuensi kata yang sama
    for i in range(len(list_kata)):
        if (list_kata[i] == list_kata[i-1]):
            hitung += 1
        else:
            list_akhir.append([hitung, list_kata[i-1]])
            hitung = 1  
    
#Mengurutkan list berdasarkan frekuensi terbanyak dan membuat patokan high dan low
    list_akhir.sort(reverse=True)
    list_akhir = list_akhir[:50]
    high_count = list_akhir[0][0]
    low_count = list_akhir[-1][0]   

#Mengeprint list kata
    print('\n' + nama_file + ' :\n50 words in frequency order as (count:word) pairs\n') 

    for i in range(len(list_akhir)):
        print("{:>3d} : {:<14s}".format(list_akhir[i][0], list_akhir[i][1]), end='')
        batasan += 1
        if batasan > 3:
            print()
            batasan = 0
        list_akhir[i] = [list_akhir[i][1], list_akhir[i][0]]    

#Mengurutkan list berdasarkan alfabet
    list_akhir.sort()   

#Meminta input enter dari user untuk melanjutkan membuat file html
    input('\n\nPlease type Enter to continue ...')  

#Membuat file html
    body=''
    for word,cnt in list_akhir:
        body = body + " " + htmlFunctions.make_HTML_word(word,cnt,high_count,low_count)
    box = htmlFunctions.make_HTML_box(body)
    htmlFunctions.print_HTML_file(box,nama_file + ' Word Cloud')

#Jika terjadi error salah input atau ada interupsi dari user
except(FileNotFoundError):
    print("File doesn't exist, please try again!")
except(IOError):
    print('Input or output error, please try again!')
except(KeyboardInterrupt):
    print('Keyboard interruption, please try again!')
