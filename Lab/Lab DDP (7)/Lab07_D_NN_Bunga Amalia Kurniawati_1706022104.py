#Bunga Amalia Kurniawati - 1706022104
#Lab 7 DDP Kelas D - 10 November 2017
#BenJek, Benny Ojek

#Membuat class utama untuk menjalankan program
class DriverBenJek:
    
#inisialisasi saat class dipanggil
    def __init__(self, nama = '', tipe = ''):
        self.nama_driver = nama
        self.tipe_driver = tipe
        self.pendapatan = 0
        self.pendapatan_total = 0

#membuat fungsi untuk mengetahui driver dapat jalan atau tidak dan berapa pendapatannya masing-masing
    def perjalanan(self, jarak):
        if self.tipe_driver == 'NORMAL':
            min_jarak = 0
            if int(jarak) > min_jarak:
                self.pendapatan = 1000 * int(jarak)
                self.pendapatan_total += self.pendapatan
                print(self.nama_driver, 'melakukan perjalanan sejauh', jarak, 'dan mendapatkan pendapatan sebesar', str(self.pendapatan))
            else:
                print(self.nama_driver, 'tidak bisa melakukan perjalanan')
        elif self.tipe_driver == 'SPORT':
            min_jarak = 10
            if int(jarak) > min_jarak:
                self.pendapatan = 2500 * int(jarak)
                self.pendapatan_total += self.pendapatan
                print(self.nama_driver, 'melakukan perjalanan sejauh', jarak, 'dan mendapatkan pendapatan sebesar', str(self.pendapatan))
            else:
                print(self.nama_driver, 'tidak bisa melakukan perjalanan')
        elif self.tipe_driver == 'CRUISER':
            min_jarak = 25
            if int(jarak) > min_jarak:
                self.pendapatan = 7500 * int(jarak)
                self.pendapatan_total += self.pendapatan
                print(self.nama_driver, 'melakukan perjalanan sejauh', jarak, 'dan mendapatkan pendapatan sebesar', str(self.pendapatan))
            else:
                print(self.nama_driver, 'tidak bisa melakukan perjalanan')

#Membuat fungsi untuk mengeprint pendapatan total sementara perdriver
    def cek_pendapatan(self, nama):
        print(nama, 'memiliki pendapatan sebesar', str(self.pendapatan_total))

#Membuat fungsi untuk mengeprint pendapatan total akhir perdriver
    def pendapatan_driver(self, nama):
        print(('{} : Rp.{}').format(nama, str(self.pendapatan_total * 4//5)))

#Membuat variabel kosong sebelum menjalankan program
dict_nama = {}
list_pendapatan = []
total_benjek = 0

#Program terus berjalan sampai input berupa 'AKHIR BULAN'
while True:
    masukan = input().split()
#Program yang dijalankan untuk perintah 'DAFTAR'
    if masukan[0] == 'DAFTAR':
        if masukan[1] not in dict_nama:
#Memasukkan driver ke dictionary apabila driver belum terdaftar
            dict_nama[masukan[1]] = DriverBenJek(masukan[1], masukan[2])
            print(masukan[1], 'berhasil mendaftar sebagai driver BenJek layanan', masukan[2])
        else:
            print(masukan[1], 'gagal mendaftar sebagai driver BenJek')
#Program yang dijalankan untuk perintah 'MULAI PERJALANAN'
    elif masukan[0] == 'MULAI':
        if masukan[2] in dict_nama:
            dict_nama[masukan[2]].perjalanan(masukan[3])
        else:
            print(masukan[2], 'tidak ada di dalam sistem')
#Program yang dijalankan untuk perintah 'CEK PENDAPATAN'
    elif masukan[0] == 'CEK':
        if masukan[2] in dict_nama:
            dict_nama[masukan[2]].cek_pendapatan(masukan[2])
        else:
            print(masukan[2], 'tidak ada di dalam sistem')
#Program yang dijalankan untuk perintah 'AKHIR BULAN'
    elif masukan[0] == 'AKHIR':
#Menghitung pendapatan total untuk BenJek
        for nama in dict_nama:
            total_benjek += dict_nama[nama].pendapatan
        print('Sudah akhir bulan! Pendapatan BenJek bulan ini adalah Rp.', str(total_benjek//5))
        print('Daftar pendapatan pengemudi:')
#Mengeprint pendapatan akhir setiap driver di akhir bulan
        for nama in dict_nama:
            dict_nama[nama].pendapatan_driver(nama)
        break
        

















    
    
    
    
        
        
    
