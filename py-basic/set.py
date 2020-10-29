# belajar set
# karakteristik set adalah unordered dan unindexed, ditandai dengan curly 
# bracket {}

print("Create Set ------------")
thisset = {"apple", "banana", "cherry"}
print(thisset)

print()
print("Access items set ------")
# cara mengakses item set dengan cara menggunakan for in, 
# dikarenakan set tidak ada indexing
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)


print()
print("Check if item in the set ------")
# cara cek apakah item tersebut ada di dalam set -> ini akan retur true or false
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


print()
print("Add items --------------------")
# di set tidak bisa update item, hanya bisa menambahkan dengan method add()
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# atau bila multiple item digunakan method update()
thisset.update(["orange", "mango", "grapes"])
print(thisset)



print()
print("Get length set --------------")
# method len() digunakan untuk mengetahui banyaknya item di set
print(len(thisset))

print()
print("Remove item set --------------")
# digunakan untuk menghapus item di dalam set menggunakan method remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# bisa juga digunakan method discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("cherry")
print(thisset)

# method clear() digunakan untuk mengosongkan set
thisset.clear()
print(thisset)

# untuk menghapus set digunakan keyword del
del thisset



print()
print("Join set --------------------")
# untuk menggabungkan set bisa dipakai method union() atau update()
set1 = {"a", "b", "c"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)

# menggunakan mehtod update()
set1 = {"a", "b", "c"}
set2 = {1,2,3}

set1.update(set2)
print(set1)


print()
print("Set Constructor --------------")
thisset = set(("apple", "banana", "cherry"))
print(thisset)
