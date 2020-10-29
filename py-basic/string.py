# beljar string.

# dalam python tanda kutip satu atau dua adlah sama
print('ini tanda kutip satu', "ini tanda kutip dua")
print('-------------')

# assign string ke variable
a = "Hello"
print(a)
print('--------------')

#multiline string - mengunakan variable three quotes : 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print('--------------')

# string adalah array yang kita bisa ambil untuk datanya
a = "Hello, World!"
print(a[1])

# Slicing bila kita ingin karakter dari berapa sampai berapa
# nomor sampai tidak termasuk, jadi bila 2:5 yang diambil adalah 2,3,4
b = "Hello, World"
print(b[2:5])

# negative indexing, apabila kita ingin mengambil nilai dari belakang
b = "Hello, World"
print(b[-5:-1])

# panjang karakter dalam sebuah string
a = "Hello, World!"
print(len(a))

# python banyak punya build in methods yang dapat digunakan untuk manipulasi string
# dan semua method ini mengembalikan dengan nilai yang baru, bukan mengupdate
# dari string yang asli
# Strip -> digunakan untuk menghilangakan spasi di awal dan akhir 
a = "        Hello, World!        "
print(a.strip())

# Lower, upper, capitalize  -> untuk menjadikan format
a = "Hello, World!"
print(a.lower())
print(a.upper())
print(a.capitalize())

# replace -> untuk mengubah isi dari string, ini case sensitive
print(a.replace("H", "J"))

# split -> digunakan untuk memisah dengan di inputkan parameter karakternya
# dan otomatis akan berubah menjadi list
print(a.split(","))
b = a.split(",")
print(type(b))
print('----------------------')


# Check String
# untuk mengecek apakah ada dan tidak ada dalam sebuah string tersebut
# dengan mengunakan keyword in or not in hasilnya true or False
txt = "Ther rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


# String format 
# kita tidak bisa menggabungkan variable string dan varible number
# contohnya sperti ini 
# age = 36
# txt = "My name is John, I am " + age
# print(txt) # -> ini akan menjadi error
# untuk itu dipakai method format() dan stringnya di letakkan di {}
# contoh
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# apabila banyak maka bisa digunakan argumen index dalam menentukan posisinya
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

# Escape Karakter
txt = "We are the so-called \"Vikings\" from the north" # tanda petik
txt2 = "We are the so-called \"Vikings\" \b from the north" #enter
print(txt)
print(txt2)





