#Tugas Pemrograman 3 kelas D - BenCoin
#Bunga Amalia Kurniawati - 1706022104

class AkunBen():
    
#=================================================================================================================================#
#                             Menginisiasi variabel yang akan digunakan sebagai atribut dalam class                               #
#=================================================================================================================================#
    def __init__(self, nama='', jenis=''):
        self.nama = nama
        self.jenis = jenis
        self.tabungan = 0
        self.transaksi = []
        self.batas_transaksi = jenis_akun[self.jenis][0]
        self.batas_tabungan = jenis_akun[self.jenis][1]
        self.biaya_transaksi = jenis_akun[self.jenis][2]
        
#=================================================================================================================================#
#                               Untuk menyimpan string yang dapat diprint setiap pemanggilan class                                #
#=================================================================================================================================#
    def __str__(self):
        return 'Akun atas nama ' + self.nama.capitalize() + ' telah terdaftar dengan paket ' + self.jenis.capitalize()
    
#=================================================================================================================================#
# Membuat fungsi untuk perintah SETOR yang memiliki 3 kasus yaitu:                                                                #
#   1. Ketika tabungan dapat menerima seluruh setoran                                                                             #
#   2. Ketika tabungan hanya dapat menerima sebagian setoran karena tabungan akan mencapai batas tabungan                         #
#   3. Ketika tabungan tidak dapat menerima setoran karena tabungan sudah mencapai batas tabungan                                 #
#=================================================================================================================================#
    def setor(self, jumlah, matauang):
        if self.tabungan < self.batas_tabungan:
            self.setoran = jumlah/mata_uang[matauang]
            if self.setoran > self.batas_tabungan - self.tabungan:
                self.setoran = self.batas_tabungan - self.tabungan
            self.tabungan += self.setoran
            self.transaksi.append(str('SETOR ' + matauang.upper() + ' ' + str(round(jumlah,5)) + ' ' + str(round(self.setoran,5))))
            print('Akun', self.nama.capitalize(), 'telah bertambah', round(self.setoran,5), 'BenCoin')
        else:
            print('Akun', self.nama.capitalize(), 'sudah memenuhi kapasitas')
            
#=================================================================================================================================#
# Membuat fungsi untuk perintah TARIK yang memiliki 4 kasus yaitu:                                                                #
#   1. Ketika user dapat menarik seluruh jumlah uang yang diinginkan                                                              #
#   2. Ketika user hanya dapat menarik sebagian dari jumlah uang yang diinginkan karena melewati batas transaksi jenis akunnya    #
#   3. Ketika user hanya dapat menarik sebagian dari jumlah yang diinginkan karena tabungan akan habis                            #
#   4. Ketika user tidak dapat menarik uang karena tabungan habis                                                                 #
#=================================================================================================================================#        
    def tarik(self, jumlah, matauang):
        if self.tabungan > self.biaya_transaksi:
            self.tabungan -= self.biaya_transaksi
            self.tarikan = jumlah
            if self.tarikan > self.tabungan and self.tarikan > self.batas_transaksi:
                self.tarikan = min(self.tabungan, self.batas_transaksi)
            elif self.tarikan > self.tabungan:
                self.tarikan = self.tabungan
            elif self.tarikan > self.batas_transaksi:
                self.tarikan = self.batas_transaksi
            self.tabungan -= self.tarikan
            self.transaksi.append(str('TARIK ' + matauang.upper() + ' ' + str(round((jumlah*mata_uang[matauang]),5)) +\
                                      ' ' + str(round(self.tarikan,5))))
            print('Penarikan', round((jumlah*mata_uang[matauang]),5), 'dari akun', self.nama.capitalize(), 'berhasil!')
        else:
            print('Akun', self.nama.capitalize(), 'tidak dapat melakukan transaksi penarikan karena tabungan tidak mencukupi')
            
#=================================================================================================================================#
# Membuat fungsi untuk perintah TRANSFER yang memiliki 6 kasus yaitu:                                                             #
#   1. Ketika user dapat mentransfer seluruh jumlah uang yang diinginkan                                                          #
#   2. Ketika user hanya dapat mentransfer sebagian dari jumlah uang yang diinginkan karena pengirim melewati batas transaksi     #
#   3. Ketika user hanya dapat mentransfer sebagian dari jumlah uang yang diinginkan karena tabungan pengirim akan habis          #
#   4. Ketika user hanya dapat mentransfer sebagian dari jumlah uang yang diinginkan karena tabungan penerima akan penuh          #
#   5. Ketika user tidak dapat mentransfer uang karena tabungan pengirim tidak mencukupi kebutuhan uang untuk transfer            #
#   6. Ketika user tidak dapat mentransfer uang karena tabungan penerima sudah memenuhi batas tabungannya                         #
#=================================================================================================================================#
    def transfer(self, penerima, jumlah):
        if self.tabungan > self.biaya_transaksi:
            self.tabungan -= self.biaya_transaksi
            self.transferan = jumlah
            maks_penerima = penerima.batas_tabungan - penerima.tabungan
            if self.transferan > self.batas_transaksi and self.transferan > self.tabungan and self.transferan > maks_penerima:
                self.transferan = min(self.batas_transaksi, self.tabungan, maks_penerima)
            elif self.transferan > self.batas_transaksi and self.transferan > self.tabungan:
                self.transferan = min(self.batas_transaksi, self.tabungan)
            elif self.transferan > self.batas_transaksi and self.transferan > maks_penerima:
                self.transferan = min(self.batas_transaksi, maks_penerima)
            elif self.transferan > self.tabungan and self.transferan > maks_penerima:
                self.transferan = min(self.tabungan, maks_penerima)
            elif self.transferan > self.batas_transaksi:
                self.transferan = self.batas_transaksi
            elif self.transferan > self.tabungan:
                self.transferan = self.tabungan
            elif self.transferan > maks_penerima:
                self.transferan = maks_penerima
            self.tabungan -= self.transferan
            penerima.tabungan += self.transferan
            self.transaksi.append(str('TRANSFER ' + penerima.nama.capitalize() + ' ' + str(round(self.transferan,5))))
            print(self.nama.capitalize(), 'berhasil mentransfer', round(self.transferan,5), 'BenCoin kepada',\
                  penerima.nama.capitalize())
        elif penerima.tabungan == penerima.batas_tabungan:
            print('Tabungan akun', penerima.nama.capitalize(), 'berada di batas tabungan paket', penerima.jenis.capitalize(),\
                  'sehingga tidak dapat menerima transfer')
        else:
            print('Akun', self.nama.capitalize(), 'tidak cukup untuk melakukan transfer')
            
'''--------------------------------------------------------------------------------------------------------------------------------
                                                        Batas Main Program
--------------------------------------------------------------------------------------------------------------------------------'''

#=================================================================================================================================#
#               Membuat variabel kosong dan dictionary jenis akun yang akan digunakan sebagai atribut dalam class                 #
#=================================================================================================================================#      
nasabah = {}
mata_uang = {}

jenis_akun = {'pelajar' : [25, 150, 0], 'reguler' : [100, 500, 5],\
              'bisnis' : [500, 2000, 15], 'elite' : [10000, 100000, 50]}

#=================================================================================================================================#
#                    Membuat awalan program yang menjelaskan jenis akun dan format perintah yang dapat digunakan                  #
#=================================================================================================================================#
print('------------------------------------------------------------------------------\n'\
      '                        Selamat datang di Bank BenCoin!\n',\
      'Terdapat 4 jenis akun yaitu:\n'\
      '1. Pelajar : Maks Transaksi[25], Maks Tabungan[150], Biaya Transaksi[0]\n'\
      '2. Reguler : Maks Transaksi[100], Maks Tabungan[500], Biaya Transaksi[5]\n'\
      '3. Bisnis : Maks Transaksi[500], Maks Tabungan[2000], Biaya Transaksi[15]\n'\
      '4. Elite : Maks Transaksi[10000], Maks Tabungan[100000], Biaya Transaksi[50]\n'\
      'Berikut perintah yang dapat dijalankan:\n',\
      '1. DAFTAR [nama] [jenis akun: pelajar/reguler/bisnis/elite]\n',\
      '2. TAMBAH [nama mata uang] [rate mata uang awal per BenCoin]\n',\
      '3. UBAH [nama mata uang] [rate mata uang baru per BenCoin]\n',\
      '4. SETOR [nama] [jumlah uang] [mata uang]\n',\
      '5. TARIK [nama] [jumlah uang] [mata uang]\n',\
      '6. TRANSFER [nama pengirim] [nama penerima] [jumlah uang BenCoin]\n',\
      '7. INFO [nama]\n',\
      '       Silakan masukkan perintah yang diinginkan sesuai format yang ada.\n'\
      '------------------------------------------------------------------------------\n')

#=================================================================================================================================#
#                               Meminta input dari user selama input tersebut tidak kosong/enter                                  #
#=================================================================================================================================#
while True:
    try:
        masukan = input('>>> ').lower().split()
    
        if len(masukan) == 0:
            print('Terima kasih telah menggunakan Bank BenCoin!')
            break

#=================================================================================================================================#
#                                        Mengecek jenis perintah yang dimasukkan user                                             #
#=================================================================================================================================#
        perintah = masukan[0]

#=================================================================================================================================#
# Jika perintah adalah DAFTAR, terdapat 3 kasus yaitu:                                                                            #
# 1. Jika nasabah belum terdaftar dan jenis akun sesuai dengan jenis akun yang ada                                                #
# 2. Jika nasabah sudah terdaftar di dalam sistem                                                                                 #
# 3. Jika jenis akun tidak sesuai dengan jenis akun yang ada                                                                      #
#=================================================================================================================================#
        if perintah == 'daftar' and len(masukan) == 3:
            if masukan[1] not in nasabah and masukan[2] in jenis_akun:
                nasabah[masukan[1]] = AkunBen(masukan[1], masukan[2])
                print(nasabah[masukan[1]])
            elif masukan[1] in nasabah:
                print('Akun atas nama', masukan[1].capitalize(), 'sudah terdaftar')
            elif masukan[2] not in jenis_akun:
                print('Tidak terdapat jenis akun', masukan[2].capitalize())

#=================================================================================================================================#
# Jika perintah adalah TAMBAH, terdapat 3 kasus yaitu:                                                                            #
# 1. Jika mata uang belum terdaftar dan rate bernilai > 0                                                                         #
# 2. Jika mata uang sudah terdaftar                                                                                               #
# 3. Jika rate bernilai <= 0                                                                                                      #
#=================================================================================================================================#
        elif perintah == 'tambah' and len(masukan) == 3:
            if eval(masukan[2]) > 0:
                if masukan[1] not in mata_uang:
                    mata_uang[masukan[1]] = float(eval(masukan[2]))
                    print('Mata uang', masukan[1].upper(), 'telah ditambahkan dengan rate', masukan[2], 'per BenCoin')
                else:
                    print('Mata uang sudah terdaftar. Jika ingin mengubah rate mata uang gunakan perintah UBAH')
            else:
                print('Rate tidak dapat bernilai', masukan[2])

#=================================================================================================================================#
# Jika perintah adalah UBAH, terdapat 3 kasus yaitu:                                                                              #
# 1. Jika mata uang sudah terdaftar dan rate bernilai > 0                                                                         #
# 2. Jika mata uang belum terdaftar                                                                                               #
# 3. Jika rate bernilai <= 0                                                                                                      #
#=================================================================================================================================#
        elif perintah == 'ubah' and len(masukan) == 3:
            if eval(masukan[2]) > 0:
                if masukan[1] in mata_uang:
                    mata_uang[masukan[1]] = float(eval(masukan[2]))
                    print('Rate mata uang', masukan[1].upper(), 'berubah menjadi', masukan[2], 'per BenCoin')
                else:
                    print('Mata uang', masukan[1].upper(), 'tidak ada')
            else:
                print('Rate tidak dapat bernilai', masukan[2])

#=================================================================================================================================#
# Jika perintah adalah SETOR atau TARIK, terdapat 4 kasus yaitu:                                                                  #
# 1. Jika nasabah sudah terdaftar, jumlah setoran atau tarikan bernilai > 0 dan mata uang sudah terdaftar                         #
# 2. Jika nasabah belum terdaftar                                                                                                 #
# 3. Jika jumlah setoran atau tarikan bernilai <= 0                                                                               #
# 4. Jika mata uang belum terdaftar                                                                                               #
#=================================================================================================================================#
        elif perintah == 'setor' and len(masukan) == 4:
            if masukan[1] in nasabah and eval(masukan[2]) > 0 and masukan[3] in mata_uang:
                nasabah[masukan[1]].setor(float(eval(masukan[2])), masukan[3])
            elif masukan[1] not in nasabah:
                print('Akun atas nama', masukan[1].capitalize(), 'belum terdaftar')
            elif eval(masukan[2]) <= 0:
                print('Jumlah uang tidak dapat bernilai', masukan[2])
            elif masukan[3] not in mata_uang:
                print('Mata uang', masukan[3].upper(), 'tidak ada')

        elif perintah == 'tarik' and len(masukan) == 4:
            if masukan[1] in nasabah and eval(masukan[2]) > 0 and masukan[3] in mata_uang:
                nasabah[masukan[1]].tarik(float(eval(masukan[2])), masukan[3])
            elif masukan[1] not in nasabah:
                print('Akun atas nama', masukan[1].capitalize(), 'belum terdaftar')
            elif eval(masukan[2]) <= 0:
                print('Jumlah uang tidak dapat bernilai', masukan[2])
            elif masukan[3] not in mata_uang:
                print('Mata uang', masukan[3].upper(), 'tidak ada')

#=================================================================================================================================#
# Jika perintah adalah TRANSFER, terdapat 5 kasus yaitu:                                                                          #
# 1. Jika nasabah pengirim dan penerima sudah terdaftar, bukan nasabah yang sama dan jumlah transferan bernilai > 0               #
# 2. Jika nasabah pengirim belum terdaftar                                                                                        #
# 3. Jika nasabah penerima belum terdaftar                                                                                        #
# 4. Jika nasabah pengirim dan penerima sama                                                                                      #
# 5. Jika jumlah transferan bernilai <= 0                                                                                         #
#=================================================================================================================================#
        elif perintah == 'transfer' and len(masukan) == 4:
            if ((masukan[1] and masukan[2]) in nasabah) and masukan[1] != masukan[2] and eval(masukan[3]) > 0:
                nasabah[masukan[1]].transfer(nasabah[masukan[2]], float(eval(masukan[3])))
            elif masukan[1] not in nasabah:
                print('Akun atas nama', masukan[1].capitalize(), 'belum terdaftar')
            elif masukan[2] not in nasabah:
                print('Akun atas nama', masukan[2].capitalize(), 'belum terdaftar')
            elif masukan[1] == masukan[2]:
                print('Tidak dapat mentransfer ke akun yang sama')
            elif eval(masukan[3]) <= 0:
                print('Jumlah uang tidak dapat bernilai', masukan[3])

#=================================================================================================================================#
# Jika perintah adalah INFO, terdapat 2 kasus yaitu:                                                                              #
# 1. Jika nasabah sudah terdaftar                                                                                                 #
# 3. Jika nasabah belum terdaftar                                                                                                 #
#=================================================================================================================================#
        elif perintah == 'info' and len(masukan) == 2:
            if masukan[1] in nasabah:
                print('Nama           :', masukan[1].capitalize())
                print('Jenis Akun     :', nasabah[masukan[1]].jenis.capitalize())
                print('Jumlah BenCoin :', nasabah[masukan[1]].tabungan)
                print('Transaksi      :')
                for transaksi in nasabah[masukan[1]].transaksi:
                    print(transaksi)
            else:
                print('Akun atas nama', masukan[1].capitalize(), 'belum terdaftar')
                
#=================================================================================================================================#
#            Jika perintah yang dimasukkan tidak sesuai atau terjadi error, maka akan diminta kembali input yang sesuai           #
#=================================================================================================================================#
        else:
            print('Perintah salah, tolong masukan perintah sesuai format')
            
    except(IndexError, ValueError, KeyError, TypeError, NameError, KeyboardInterrupt):
        print('Perintah salah, tolong masukan perintah sesuai format')
