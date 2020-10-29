# belajar tuple
# karaketer tipe data collection tuple : ordered, unchangeable

print("Create a tuple -------------")
# cara membuat tuple yaitu dengan cara memulai dan mengakhiri dengan tanda 
# kurung buka dan kurung tutup
thistuple = ("apple", "banana", "cherry")
print(thistuple)


print()
print("Access Tuple --------------")
# untuk mengakses tuple menggunakan index
print(thistuple[1])

# juga bisa diakses dengan negative indexing
print(thistuple[-1])

# juga bisa diakses dengan menggunakan range
thistuple = ("apple", "melon", "banana", "cherry", "orange", "kiwi", "mango")
print(thistuple[2:5])

#juga bisa range negative
print(thistuple[-4:-1])


print()
print("Change tuple values -----------")
# tuple tidak bisa di ganti isinya, tapi bisa diakali dengan 
# tuple nya diubah dulu menjadi list kemudian dikembalikan menjadi tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)



print()
print("Loop tuple -------------")
# cara looping mengambil nilai dari tuple dengan menggunakan for
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


print()
print("Check item exist -------")
# mengecek apakah item tersebut ada di dalam tuple? dengan mengunakan in
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, apple is in the fruits tuple")

print()
print("Tuple lenght ------------")
# untuk melihat number item di dalam tuple digunakan len
print(len(thistuple))

# ----------------------------------------------
# Tuple tidak bisa ditambahkan item datanya
# ----------------------------------------------

print()
print("Create tuple with one item ---- ")
# cara menambahkan tuple dengan satu item dengan cara menambahkan koma dibelakangnya
thistuple = ("apple",)
print(type(thistuple))

# ----------------------------------------------
# Tuple tidak bisa dihapus item datanya, bisa nya di delete
# ----------------------------------------------
print()
print("Delete tuple ------------")
thistuple = ("apple", "banana", "cherry")
del thistuple


print()
print("Join tuple --------------")
# untuk join tuple bisa digunakan operator +
tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)

tuple3 = tuple1 + tuple2
print(tuple3)

print()
print("tuple constructor -------")
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)



print()
print("Count --------------")
# untuk mengembalikan nilai item yang ada di dalam tuple tersebut
thistuple = (1,2,3,4,5,1,2,5,6)
print(thistuple.count(1))


print()
print("index --------------")
# untuk mengembalikan nilai index nomor berapa yang dicari
thistuple = (1,2,7,9,5,1,2,5,6)
print(thistuple.index(7))