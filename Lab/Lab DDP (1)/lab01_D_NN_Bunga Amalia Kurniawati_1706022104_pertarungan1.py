#Lab DDP kelas D, 8 September 2017
#Bunga Amalia Kurniawati - Ilmu Komputer 1706022104
#Pertarungan 1

import turtle
t = turtle.Turtle()

panjang = int(input('Masukkan panjang dari sisi anak tangga: '))

t.pendown()

t.color('yellow')
t.left(90)
t.forward(panjang)
t.right(90)
t.forward(panjang)              

t.color('blue')
t.left(90)
t.forward(panjang)
t.right(90)
t.forward(panjang)

t.color('red')
t.left(90)
t.forward(panjang)
t.right(90)
t.forward(panjang)

t.color('green')
t.right(90)
t.forward(panjang*3)
t.right(90)
t.forward(panjang*3)
