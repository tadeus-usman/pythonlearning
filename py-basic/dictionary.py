# belajar dictionary
# karakterisik nya adalah : unordered, changeable, and indexed
# menggunakan curly brackets {} dan mempunya key dan values

print("Create dictionary ---------------")
# cara membuat dictionary ada pasangan key dan valuesnya
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)

print()
print("Accessing dictionary item ------")
# cara mengakses dictionary adalah dengan merefer kepada nama 'key'nya
x = thisdict["model"]
print(x)

# atau dengan menggunakan method get()
x = thisdict.get("model")
print(x)


print()
print("Change Values -----------------")
# pada dictionary bisa diubah value nya dengan merefer pada keynya
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["year"] = 2008
print(thisdict)




print()
print("Loop through a Dictionary -----")
# melakukan perulangan untk mengambil nilai pada dictionary digunakan for
for x in thisdict:
    print(x) # -> ini akan menampilkan hanya key nya saja

print()

# untuk mengambil value nya digunakan sebagai berikut
for x in thisdict:
    print(thisdict[x])
print()

# juga dapat menggunakan method values()
print("by method values()")
for x in thisdict.values():
    print(x)
print()

# untuk mengambil key dan valuenya, digunakan method items()
print("by method item()")
for x,y in thisdict.items():
    print(x,y)


print()
print("Check if Key Exists -----------")
# untuk mengecek keynya nya apakah ada digunakan keyword in
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary ")


print()
print("Dictionary lenght -----------")
# untuk melihat banyaknya item di dict digunakan len() function
print(len(thisdict))


print()
print("Adding items")
# untuk menambahkan items di dict digunakan dengan new key dan value nya
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1980
}
thisdict["color"] = "red" # penambahan items pada dict
print(thisdict)

print("Menggunakan function update() ---")
# menggunakan function update
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.update({"color" : "Red"})


print()
print("Remove in dictionary ------------")
# ada beberapa cara untuk menghapus di dictionary
# menggunakan method pop() -> key nya spesifik
print("method pop()")
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.pop("model")
print(thisdict)

print("method popitem() ---------")
# akan meremove last item pada dict
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964 # ini yang akan di remove
}
thisdict.popitem()
print(thisdict)

print("keyword del ----------------")
# menggunakan keyword del
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
del thisdict["model"]
print(thisdict)

# keyword del juga bisa digunakan untuk menghapus thisdict
del thisdict


print("method clear() ---------")
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.clear()
print(thisdict)



print()
print("Copy a Dictionary ------")
print("method copy() ----------")
# cara menggukan method copy() untuk mengkopy dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
mydict = thisdict.copy()
print(mydict)

# juga bisa digunakan function dict()
print("dict() function -------")
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
mydict = dict(thisdict)
print(mydict)


print()
print("Nested Dictionary -------------")
# dict bisa menampung banyak dict -> nested dict
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}

print(myfamily)

# atau ingin menakses tiga dictionary yang sudah ada dan dijadikan menjadi satu
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily)



print()
print("The dict() Constructor ---------")
# untuk membuat dict baru dengan dict()
thisdict = dict(brang = "Ford", model = "Mustang", year = 1904)
print(thisdict)