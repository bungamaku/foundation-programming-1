#Bunga Amalia Kurniawati - 1706022104
#Lab 5 DDP Kelas D - 6 Oktober 2017
#Ujian Sebentar Lagi

#Membuat fungsi untuk mencetak pertanyaan
def cetak_pertanyaan(urutan, angka_biner):
    print('Soal ' + str(urutan) + ' : Berapakah angka desimal dari bilangan biner ' + str(angka_biner) + '?')

#Membuat fungsi untuk mengecek jawaban    
def cek_jawaban(jawaban, angka_biner):
    if jawaban == str(int(angka_biner, 2)):
        return True
    else:
        return False
    
#Membuat fungsi utama yang ingin dijalankan    
def main():
    print('Selamat datang di Mini Kuis DDP-1: Sistem Bilangan!')
    soal1 = '11111100001'
    soal2 = '11111001111'
    soal3 = '10001100'
    soal4 = '100011101'
    counter_soal = 1
    skor = 0
#Membuat list untuk menyimpan soal
    list_soal = [soal1, soal2, soal3, soal4]

#Meminta input jawaban dan mengecek jawabannya untuk mendapatkan skor
    while counter_soal <= 4:
        cetak_pertanyaan(counter_soal, list_soal[counter_soal-1])
        jawaban = input('Jawab: ')
        if cek_jawaban(jawaban, list_soal[counter_soal-1]):
            skor += 25
        counter_soal += 1
    print('Skor akhir: ' + str(skor))

'''
SOAL BONUS
def main():
    print('Selamat datang di Mini Kuis DDP-1: Sistem Bilangan!')
    list_soal = input('Masukkan 4 soal: ').split()
    counter_soal = 1
    skor = 0
    
    while counter_soal <= 4:
        cetak_pertanyaan(counter_soal, list_soal[counter_soal-1])
        jawaban = input('Jawab: ')
        if cek_jawaban(jawaban, list_soal[counter_soal-1]):
            skor += 25
        counter_soal += 1
    print('Skor akhir: ' + str(skor))
'''

#Menjalankan fungsi utama        
if __name__ == '__main__':
    main()
