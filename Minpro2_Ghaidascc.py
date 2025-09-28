import getpass

USERS = {
    "ghaida": {"password": "adminn123", "role": "Admin"},
    "suci": {"password": "user456", "role": "User"}
}

produk = {
    "items":{
        1:{"produk": "Baju", "harga": 120000, "stok": 17, "kategori": "pakaian"},
        2:{"produk": "Buku", "harga": 3000, "stok": 20, "kategori": "ATK"},
    },
    "next_number": 3
}


def tambah_produk_admin(toko):
    try:
        nama = input("nama barang: ")
        harga = int(input("harga: "))
        stok = int(input("stok: "))
        kategori = input("kategori: ")

    except ValueError:
        print("input salah, coba lagi.")
    except KeyboardInterrupt:
        print("jangan tekan + C yaa !")
    except EOFError:
        print("jangan tekan CTRL + Z yaa !")
        return
    
    no_barang = toko["next_number"]
    toko["items"][no_barang] = {"produk": nama, "harga": harga, "stok": stok, "kategori": kategori}
    print(f"barang'{nama}'ditambahkan dengan nomor barang {no_barang}")
    toko["next_number"] += 1

def tambah_produk_user(toko):
    try:
        nama = input("nama barang: ")
        jumlah = int(input("jumlah item: "))

    except ValueError:
        print("input salah, coba lagi.")
    except KeyboardInterrupt:
        print("jangan tekan + C yaa !")
    except EOFError:
        print("jangan tekan CTRL + Z yaa !")
        return
    
    no_barang = toko["next_number"]
    toko["items"][no_barang] = {"nama": nama, "jumlah item": jumlah}
    print(f"barang'{nama}'ditambahkan ke keranjang")

def lihat_barang(toko):
    if not toko["items"]:
        print("Barang belum tersedia")
    else:
        for no_barang, info in toko["items"].items():
            print(f"{no_barang}. {info['produk']} , Rp{info['harga']} , stok{info['stok']} , kategori{info['kategori']}")


def edit_barang(toko):
    try:
        no_barang = int(input("Nomor barang yang ingin diubah: "))
        if no_barang not in toko["items"]:
            print("Nomor barang tidak ditemukan.")
            return
        item = toko["items"][no_barang]
        nama = input(f"nama baru ({item['produk']}): ") or item['nama']
        harga = input(f"harga baru ({item['harga']}): ")
        stok = input(f"stok baru ({item['stok']}): ")
        kategori = input(f"kategori ({item['kategori']}): ") or item['kategori']
        if harga:item['harga'] = int(harga)
        if stok:item['stok'] = int(stok)
        item['produk'], item['kategori'] = nama, kategori
        print("Barang berhasil di update. ")
    except ValueError:
        print("input salah!")
    except KeyboardInterrupt:
        print("jangan tekan + C yaa !")
    except EOFError:
        print("jangan tekan CTRL + Z yaa !")

def hapus_barang(toko):
    try:
        no_barang = int(input("Nomor barang yang mau dihapus: "))
        if no_barang in toko["items"]:
            del toko["items"][no_barang]
            print("Barang dihapus. ")
        else:
            print("Nomor barang tidak ditemukan. ")
    except ValueError:
        print("Input salah. ")
    except KeyboardInterrupt:
        print("jangan tekan + C yaa !")
    except EOFError:
        print("jangan tekan CTRL + Z yaa !")

def login():
    username = input("Username: ")
    password = getpass.getpass("Passworrd: ")
    user = USERS.get(username)
    if user and password == user["password"]:
        print(f"Selamat datang {username} ({user['role']})")
        return user["role"]
    else:
        print("Login gagal. ")
        return None
    
    
def admin_menu(toko):
    while True:
            print("\n1. Lihat barang\n2. Tambah produk\n3. Edit barang\n4. Hapus barang\n5. Logout")
            pilih = input("Pilih: ")
            if pilih == "1": lihat_barang(toko)
            elif pilih == "2": tambah_produk_admin(toko)
            elif pilih == "3": edit_barang(toko)
            elif pilih == "4": hapus_barang(toko)
            elif pilih == "5":
                print("Anda telah logout...")
                break
            else:
                print("Pilihan tidak valid!")
                break

            lanjut = input("\nMau lanjut pilih menu lagi?? (y/n):").lower()
            if lanjut != "y":
                print("Proses selesai. Terima kasih! ")
                exit()

def user(toko):
    while True:
        print("\n1. Lihat barang tersedia\n2. Tambah produk\n3. Logout")
        pilih = input("Pilih: ")
        if pilih == "1": lihat_barang(toko)
        elif pilih == "2": tambah_produk_user(toko)
        elif pilih == "3":
            print("Anda telah logout. ")
            break
        else:
            print("Pilihan tidak valid!")
            break
            

        lanjut = input("\nMau lanjut pilih menu lagi? (y/n):").lower()
        if lanjut != "y":
            print("Proses selesai. Terima kasih! ")
            exit()


def main():
        while True:
            role = login()
            if role == "Admin": 
                admin_menu(produk)
                lagi = input("Login lagi?? (y/n): ")
                if lagi.lower() != "y":
                    print("Proses selesai. Terima kasih! ")
                    break
            elif role:
                user(produk)
                lagi = input("Login lagi?? (y/n): ")
                if lagi.lower() != "y":
                    print("Proses selesai. Terima kasih! ")
                    break    

if __name__ == "__main__":
    main()