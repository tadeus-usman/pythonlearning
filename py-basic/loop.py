# Belajar Loop
# di python ada 3 yaitu : while loop, for loop, dan nested loop

# while loop : akan diesekusi ketika nilai yang kondisi = True
x = 5
while (x <= 10):
    print(f"Nilai x = {x} ")
    x += 1

print()
#----------------------------------------------------------

# For loop digunakan apabila ingin melakukan perulangan item dari urutan apapun
# contohnya data dari list / string

angka = [1,2,3,4,5]
for x in angka:
    print(x)

print()

buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
    print(f"Saya suka makan {makanan}")   

# ataupun list di dalam list

buah = ["nanas", "apel", "jeruk"]
sayur = ["bayarm", "wortel", "kangkung"]
lauk = ["ayam","tempe", "tahu"]
makanan = [buah,sayur,lauk]

for belanja in makanan:
    print(f"Saya belanja {belanja}")
    for item_belanja in belanja:
        print("itemnya adalah " + item_belanja)
    print()   
