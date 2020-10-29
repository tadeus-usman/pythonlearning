# Belajar List
# sifat list : ordered, changeable, allows duplicate members, 

# cara membuat list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# cara akses item berdasarkan dengan indexnya
print(thislist[1])

# list juga bisa negative list (ini dari belakang)
print(thislist[-1]) # ini juga digunakan untuk last item


# untuk list juga bisa diakses dengan menggunakan range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "manggo"]
print(thislist[2:5]) # diambil data item dari nomor index 2, 3, 4 (5 tidak termasuk)

# bisa juga dari awal sampai ke index berapa
print(thislist[:4]) # akan ditampilkan index ke 0 sampai dengan 3 (4 tidak termasuk)

# atau dimulai dari index ke berapa sampai index terakhir
print(thislist[4:]) # akan ditampilkan index ke 4 sampai index terakhir

print("--------------------------")



# mengubah item value dari index dengan cara index nomor berapa yang ingin diganti
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print("loop list ---------------------")
# cara loop item list bisa menggunakan for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

print("")
print("keyword in ----------------------")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruit list")

print()
print("list lenght -----------------")
# untuk mengecek banyaknya data di dalam list
print(len(thislist))

print()
print("Add item list ---------------")
# untuk menambahkan item ist, digunakan mehtod append()
thislist.append("orange")
print(thislist)

# atau bisa digunakan method insert() apabila ingin sepesifik indexnya
thislist.insert(1, "guava")
print(thislist)


print()
print("Remove item -----------------")
# untuk menghapus item di dalam list digunakan method remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# atau digunakan method pop() untuk specified index atau last item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# ada keyword del juga bisa digunakan untuk menghapus index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# del juga bisa menghapus semua isi dari list
thislist = ["apple", "banana", "cherry"]
del thislist

# untuk mengkosongkan / clear list digunakan method clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


print('')
print("Copy a List ----------------")
# untuk menyalin / copy list digunakan method copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# atau bisa juga digunakan method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(thislist)


print()
print("Join List -----------------")
# cara untuk menggabungkan list adalah dengan menggunakan operator +
list1 = ["a", "b", "c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

# atau juga bisa digunakan dengan method append()
list1 = ["a", "b", "c"]
list2 = [1,2,3]

for x in list2:
    list1.append(x)

print(list1)

# bisa digunakan juga method extend() bila ingin ditambahkan dari akhir list1
list1 = ["a", "b", "c"]
list2 = [1,2,3]

list1.extend(list2)
print(list1)


print("")
print("List() Constructor --------")
thislist = list(("apple", "banana", "cherry"))
print(thislist)

print()
print("reverse ------------------")
#digunakan untuk membalik order dari list
thislist = ["apple", "banana", "cherry"]
thislist.reverse()
print(thislist)

print()
print("sort ---------------------")
#digunakan untuk mengurutkan list
thislist = ["melon", "guava", "apple", "blackberry"]
thislist.sort()
print(thislist)