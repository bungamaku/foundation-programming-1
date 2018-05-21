#Lab DDP kelas D, 8 September 2017
#Bunga Amalia Kurniawati - Ilmu Komputer 1706022104
#Pertarungan 2

#input biaya pernikahan dari user
biaya_nikah = int(input('Masukkan biaya pernikahan: Rp '))

#menghitung banyaknya hari yang dibutuhkan
lama = biaya_nikah // 500000

#menghintung tahun, bulan, minggu, dan hari
tahun = lama // 336
lama = lama % 336
bulan = lama // 28
lama = lama % 28
minggu = lama // 7
lama = lama % 7
hari = lama

#output lamanya bekerja   
print('Anda harus bekerja selama', tahun, 'tahun', bulan, 'bulan',\
      minggu, 'minggu', hari, 'hari untuk memenuhi biaya pernikahan.')
