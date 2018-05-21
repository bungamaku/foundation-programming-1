class Staff:
    def __init__(self, nama):
        self.nama = nama
        self.jam_kerja = 0
        self.progress = 0
        
    def kerja(self, jam):
        self.jam_kerja += jam

    def hitung_gaji(self):
        pass    


class StaffAcara(Staff):
    def __init__(self,nama):
        super().__init__(nama)
        
    def kerja(self, jam):
        self.jam_kerja += jam
        self.progress += self.jam_kerja * 4
        if self.progress < 100:
            return '{} bekerja selama {} jam'.format(self.nama.capitalize(), self.progress)
        else:
            return '{} sudah mencapai {}% progress'.format(self.nama.capitalize(), self.progress)

    def hitung_gaji(self):
        return self.progress * 2000

class StaffPartnership(Staff):
    def __init__(self,nama):
        super().__init__(nama)

    def kerja(self, jam):
        self.jam_kerja += jam
        self.progress += self.jam_kerja * 1
        if self.progress < 100:
            return '{} bekerja selama {} jam'.format(self.nama.capitalize(), self.progress)
        else:
            return '{} sudah mencapai {}% progress'.format(self.nama.capitalize(), self.progress)

    def hitung_gaji(self):
        return self.jam_kerja * self.progress * 4000

class StaffPublikasi(Staff):
    def __init__(self,nama):
        super().__init__(nama)

    def kerja(self, jam):
        self.jam_kerja += jam
        self.progress += self.jam_kerja * 20
        if self.progress < 100:
            return '{} bekerja selama {} jam'.format(self.nama.capitalize(), self.progress)
        else:
            return '{} sudah mencapai {}% progress'.format(self.nama.capitalize(), self.progress)

    def hitung_gaji(self):
        return self.jam_kerja * 1500

class Manager:
    def __init__(self):
        self.staffs = {}

    def recruit_staff(self, staf):
        self.staffs[staf.nama] = staf

    def get_staff(self,nama):
        return self.staffs[nama]

    def is_staff_recruited(self, nama):
        return nama in self.staffs

manager = Manager()

while True:
    masukan = input().lower().split(';')

    if masukan[0] == 'exit':
        break

    perintah = masukan[0]

    if perintah == 'rekrut' and len(masukan) == 3:
        if manager.is_staff_recruited(masukan[1]):
            print('{} sudah direkrut sebelumnya'.format(staf.nama.capitalize()))
        else:
            if(masukan[2] == 'acara'):
                staf = StaffAcara(masukan[1])
            elif(masukan[2] == 'partnership'):
                staf = StaffPartnership(masukan[1])
            elif(masukan[2] == 'publikasi'):
                staf = StaffPublikasi(masukan[1])
            manager.recruit_staff(staf)
            print('{} direkrut'.format(staf.nama.capitalize()))

    if perintah == 'kerja' and len(masukan) == 3:
        print(manager.get_staff(masukan[1]).kerja(int(masukan[2])))

    if perintah == 'log' and len(masukan) == 2:
        print('>> ', manager.get_staff(masukan[1]).nama,\
            '\nTelah bekerja selama:', manager.get_staff(masukan[1]).jam_kerja,\
            'jam\nProgress:', manager.get_staff(masukan[1]).progress,\
            'persen\nGaji sementara:', manager.get_staff(masukan[1]).hitung_gaji(),\
            'bencoin')
