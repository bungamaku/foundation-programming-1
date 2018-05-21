#Tugas Pemrograman 4 kelas D - Super Calculator
#Bunga Amalia Kurniawati - 1706022104

from tkinter import *
from math import *
from idlelib.tooltip import *

class GUI:
    #Inisiasi awal dalam pembuatan window
    def __init__(self, window):
        self.window = window
        self.window.title('Supercalculator [by Bunga Amalia Kurniawati]')
        self.memory = 0
        self.expr = ''
        self.temp = 0
        self.startOfNextOperand = True

        #Menampilkan kolom masukan
        self.entry = Entry(window, relief=RIDGE, borderwidth=8, width=38,
                           bg='azure4', font=('Helvetica', 15), fg='grey20')
        self.entry.grid(row=0, column=0, columnspan=5)

        #Daftar dari tombol
        buttons = [[ 'Clr',  'MC',  'M+',  'M-',  'MR'],
                   [   'd',   'e',   'f',   '+',   '-'],
                   [   'a',   'b',   'c',   '/',   '*'],
                   [   '7',   '8',   '9',  '**',   '√'],
                   [   '4',   '5',   '6', 'sin', 'cos'],
                   [   '1',   '2',   '3', 'tan',  'ln'],
                   [   '0',   '.',   '±',   '~',  '2C'],
                   [   'x',   'o',   '^',   '|',   '&'],
                   [   'π', 'int', 'rad',  '//', 'exp'],
                   [ 'bin', 'hex', 'oct',   '%',   '=']]

        #Daftar dari keterangan tooltip
        description = [['Clear the display field', 'Clear memory', 'Add to memory', 'Subtract from memory', 'Recall from memory'],
                       ['Letter d', "Letter e and euler's number", 'Letter f', 'Add', 'Subtract'],
                       ['Letter a', 'Letter b', 'Letter c', 'Divide', 'Multiply'],
                       ['Digit 7', 'Digit 8', 'Digit 9', 'Power', 'Squareroot'],
                       ['Digit 4', 'Digit 5', 'Digit 6', 'Sine(radians)', 'Cosine(radians)'],
                       ['Digit 1', 'Digit 2', 'Digit 3', 'Tangent(radians)', 'Natural log'],
                       ['Digit 0', 'Decimal point', 'Toggle +- sign', 'Bitwise complement', "32-bit 2's complement representation"],
                       ['Letter x', 'Letter o', 'Bitwise xor', 'Bitwise or', 'Bitwise and'],
                       ['The number Pi', 'Truncate float to int', 'Convert degrees to radians', 'Integer divide', 'Power of E(2.718...)'],
                       ['Convert int to binary', 'Convert int to hexadecimal', 'Convert int to octal', 'Modulus', 'Compute to decimals']]

        #Meletakkan tombol sesuai baris dan kolom
        #Khusus untuk 5 tombol teratas              
        for c in range(5):
            def cmd(x=buttons[0][c]):
                self.click(x)

		#Membuat tombol sesuai daftar tombol
            b = Button(window, text=buttons[0][c], width=7, bg='azure1',
                       font=('Helvetica', 15), fg='grey20', relief=RAISED, command=cmd)
            b.grid(row=1, column=c)
            #Mengaktifkan tooltip
            ToolTip(b, description[0][c])

        #Meletakkan tombol sesuai baris dan kolom sisanya
        for r in range(1, 10):
            for c in range(5):
                
                def cmd(x=buttons[r][c]):
                    self.click(x)

		#Membuat tombol sesuai daftar tombol
                b = Button(window, text=buttons[r][c], width=7, bg='grey20',
                           font=('Helvetica', 15), fg='azure1', relief=RAISED, command=cmd)
                b.grid(row=r+1, column=c)
                #Mengaktifkan tooltip
                ToolTip(b, description[r][c])

    #Fungsi untuk mengolah data masukan
    def click(self, key):
        #Untuk hasil akhir
        if key == '=':
            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(END, result)
                self.expr = ''
                self.startOfNextOperand = True
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')
                self.startOfNextOperand = True
        #Untuk operasi matematik dasar
        elif key in '+**-//&|^%':
            self.expr = '(' + self.expr + self.entry.get() + ')'
            self.expr += key
            self.startOfNextOperand = True
        #Untuk pengubah tanda positif negatif
        elif key == '±':
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass
        #Untuk operasi matematik yang langsung mengubah nilai di entry
        elif key in ('√', 'sin', 'cos', 'tan', 'ln', 'int', 'rad',
                     'exp', 'bin', 'hex', 'oct', '~', '2C'):
            try:
                if key == '~':
                    self.temp = eval(key+self.entry.get())
                elif key == '2C':
                    bil = eval(self.entry.get())
                    if bil >= 0:
                        self.temp = format(bil, '#034b')
                    else:
                        self.temp = format(2**32+bil, '#034b')
                else:
                    if key == '√': key = 'sqrt'  
                    if key == 'ln': key = 'log'
                    if key == 'rad': key = 'radians'
                    self.temp = eval(key + '(' + self.entry.get() + ')')     
                self.entry.delete(0, END)
                self.entry.insert(END, self.temp)
                self.startOfNextOperand = True
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')
                self.startOfNextOperand = True
        #Untuk nilai phi yang tidak perlu parameter
        elif key == 'π':
            self.entry.delete(0, END)
            self.entry.insert(END, pi)
            self.startOfNextOperand = True
        #Untuk penyimpanan data di memori
        elif key == 'MC':
            self.memory = 0
        elif key == 'M+':
            self.memory += eval(self.entry.get())
        elif key == 'M-':
            self.memory -= eval(self.entry.get())
        elif key == 'MR':
            self.entry.delete(0, END)
            self.entry.insert(END, self.memory)
            self.startOfNextOperand = True
        #Untuk menghapus operasi yang sedang dijalankan
        elif key == 'Clr':
            self.entry.delete(0, END)
            self.expr = ''
        #Untuk melanjutkan ke operasi berikutnya
        else:
            if self.startOfNextOperand:
                self.entry.delete(0, END)
                self.startOfNextOperand = False
            self.entry.insert(END, key)

#Untuk menjalankan program
window = Tk()
gui = GUI(window)
window.mainloop()




















