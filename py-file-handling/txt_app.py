# belajar membuat baca tulis file interaktif
def pilihan_salah():
    print()
    print()
    print("Pilihan tidak tersedia ulangi lagi")

def tanya_user():
    print("-----------------------------")
    print("ketik 0 untuk kembali ke menu")
    item = input("ketik item yang ditambah : ")
    
    if item == "0":
        pilih_menu()
    else:
        add_catatan(item)    

def new_catatan():
    file = open("txt_app.txt", "w")
    file.write("Daftar Catatan belanja \n")
    file.write("------------------------------- \n")
    file.close()

    file = open("txt_app.txt", "r")
    catatan = file.read()
    print()
    print(catatan)
    file.close()

    tanya_user()

def view_catatan():
    file = open("txt_app.txt", "r")
    catatan = file.read()
    print()
    print(catatan)
    print("-------------------------------")
    pilihan = input("ketik 0 untuk kembali ke menu : ")
    
    if pilihan == "0":
        pilih_menu()
    else:
        pilihan_salah()
        view_catatan()
    

def add_catatan(new_item):
    new_item = new_item.capitalize()
    file = open("txt_app.txt", 'a+')
    file.write("- " + new_item + '\n')
    file.close()
    tanya_user()




#membuat fungsi add_to_list inputan dari user
def pilih_menu(pilihan = 0):
    print()
    print("-------------------------")
    print("Applikasi Catatan Belanja")
    print("-------------------------")
    print("Pilih Menu : ")
    print("1. Membuat catatan baru")
    print("2. Melihat catatan")
    print("3. Menambahkan catatan")
    print("----------------------")
    print("0. Keluar Aplikasi ")
    pilihan = input("Pilihan Anda ? ")

    if pilihan == "1":
        new_catatan()
    elif pilihan == "2":
        print()
        view_catatan()
    elif pilihan == "3":
        tanya_user()
    elif pilihan == "0":
        print("Terima kasih, sampai jumpa")
    else:
        print("Pilihan tidak tersedia")
        pilih_menu()

pilih_menu()




