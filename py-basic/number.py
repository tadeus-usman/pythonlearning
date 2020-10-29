# belajar number

# di python ada 3 tipe data number : int, float, dan complex
# example

x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

print('---------------------')


# dalam tipe data number kita bisa konversikan ke tipe yang lain
# kecuali tipe data complex tidak bisa diconvert ke tipe data yang lain

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print('----------------------')

# ada juga build in fungsi yang sudah ada di python yang kita harus
# import dulu contohnya random()

import random

print('contoh nomor random : ', random.randrange(1,100))



