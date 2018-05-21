#Tugas Pemrograman 1
#Bunga Amalia Kurniawati - Ilmu Komputer 1706022104
#Chessboard and Flower with Random Colors

#Mengimpor modul Turtle dan Random
import turtle
import random

#Membuat variabel untuk mempersingkat perintah
pen = turtle.Turtle()
scr = turtle.Screen()

#Membuat judul di atas window
scr.title("Ama's Chessboard and Flower with Random Colors")

#Meminta input dari user dengan batasan yang telah ditentukan
petal = int(scr.numinput('Chessboard and Flower with Random Colors',
                         'Enter the number of petals of flower: ', minval=2, maxval=25))
row = int(scr.numinput('Chessboard and Flower with Random Colors',
                       'Enter the number of rows: ', minval=2, maxval=10))
size = int(scr.numinput('Chessboard and Flower with Random Colors',
                        'Enter the square size (pixels): ', minval=20, maxval=35))

#Mengatur keadaan dan posisi awal pen 
pen.speed(0)
pen.pensize(1.5)
pen.penup()
pen.goto(0,230)
pen.pendown()

#Membuat bunga dengan menggunakan perulangan
for a in range(petal):
    pen.color(random.random(), random.random(), random.random()) #Mengacak perubahan warna
    for b in range(2): 
        pen.circle(100, 70) #Membuat kurva
        pen.left(110) #Berputar sejauh pelurus dari sudut kurva
    pen.left(360/petal) #Berputar untuk menyesuaikan dengan jumlah petal

#Mengatur keadaan dan posisi pen untuk membuat chessboard ditengah
pen.penup()
pen.goto(-((size*row)//2), 45)

#Membuat chessboard
for c in range(row): #Perulangan untuk membuat banyak baris kotak
    for d in range(row): #Perulangan untuk membuat sebaris kotak
        pen.color(random.random(), random.random(), random.random()) #Mengacak perubahan warna
        pen.begin_fill() #Mulai mengisi warna
        for e in range(4): #Perulangan untuk membuat sebuah kotak
            pen.forward(size)
            pen.left(90)
        pen.forward(size) #Menuju posisi pembuatan kotak selanjutnya
        pen.end_fill() #Selesai mengisi warna
    pen.right(90) #Menuju baris selanjutnya
    pen.forward(size)
    pen.left(90)
    pen.backward(size*row) #Menuju titik awal pembuatan baris selanjutnya

#Menyimpan variabel untuk membuat pesan
#message = 'Colorful Chessboard of ' + str(row**2) + ' Squares and Flower of ' \
         # + str(petal) + ' Petals'

#Mengatur keadaan pen untuk menulis pesan sesuai yang ditunjukkan
pen.color('blue')
pen.goto(0, pen.ycor() - 20) #Mengatur posisi pen untuk menulis pesan
pen.write('Colorful Chessboard of ' + str(row**2) + ' Squares and Flower of ' \
          + str(petal) + ' Petals', align = 'center', font = ('Arial', 15, 'bold')) #Menulis pesan

#Menyiapkan untuk menyelesaikan program
pen.hideturtle()        
scr.exitonclick()

