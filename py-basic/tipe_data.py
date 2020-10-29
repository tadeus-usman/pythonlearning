# tipe data

"""
Tipe data di python ada bermacam-macam diantaranya 
- Boolean -> True / False

- String -> "character"

- Integer -> bilangan bulat
- Float -> bilangan pecahan
- Complex -> Menyatakan pasangan angka real dan imajiner

- List -> [] -> Data untaian yang menyimpan berbagai tipe data dan isinya bisa diubah-ubah
- Tuple -> () -> Data untaian yang menyimpan berbagai tipe data tapi isinya tidak bisa diubah
- Dictionary -> {} -> Data untaian yang menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai
"""


# tipe data Boolean
print(True)

#tipe data String
print("Ayo belajar Python")
print('Belajar Python Sangat Mudah')

#tipe data Integer
print(20)

#tipe data Float
print(3.14)

#tipe data Complex
print(5j)

#tipe data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])

#tipe data Tuple
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))

#tipe data Dictionary
print({"nama":"Budi", 'umur':20})
#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Andi", 'umur':21} #proses inisialisasi variabel biodata
print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
print(type(biodata)) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'> yang berarti dict adalah tipe data dictionary