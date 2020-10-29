# belajar file txt
# membaca dan menulis

# untuk membaca dan menulis python menggukanan open()
# beberapa mode parameter
# "r" -> untuk membuka -> membaca
# "a" -> untuk membuka file dan appending (menambahkan), 
# "w" -> untuk menulis
# "x" -> untuk exclusive creation
# "+" -> untuk reading + writing

print("")
print("Membuka dan membaca file txt----------")
file = open("data.txt","r")
text = file.read()
print(text)
file.close()

print()
print("Menulis file txt ----------------")
file = open("data2.txt", "w")
file.write("Ini test untuk menulis di file txt")
file.close()


print()
print("Membaca dan menulis ----------------")
file = open("data3.txt", "a+")
file.write("Test menuis file \n")
file.seek(0)
text = file.read()
print(text)


