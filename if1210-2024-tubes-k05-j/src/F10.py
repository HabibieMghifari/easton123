import src.Functions as f

def ubah_koin(nominal):
    for i in range(len(f.data_user)):
        if f.data_user[i] == f.data_login:
            f.data_user[i][4] = str(int(f.data_user[i][4])+nominal)

def display_shop(item_type): 
    if item_type == "monster":
        print("ID | Type                | ATK Power | DEF Power | HP   | Stok | Harga")  
        for i in range(1,len(f.data_monster_shop)):
            print(f"{f.data_monster[i][0]}  | {f.data_monster[i][1]:<19} | {f.data_monster[i][2]:<9} | {f.data_monster[i][3]:<9} | {f.data_monster[i][4]:<4} | {f.data_monster_shop[i][1]:<4} | {f.data_monster_shop[i][2]}")
    elif item_type == "potion":
        print("ID | Type                | Stok | Harga") 
        for i in range(1,len(f.data_item_shop)):         
            print(f"{f.data_item_shop[i][0]}  | {f.data_item_shop[i][1]:<19} | {f.data_item_shop[i][2]:<4} | {f.data_item_shop[i][3]}")
    print()

def buy():
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {f.data_login[4]}.")
    item_type = input(">>> Mau beli apa? (monster/potion): ")
    if item_type == "monster":
        item_id = int(input(f">>> Masukkan id {item_type}: "))
        if item_id in range(1,len(f.data_monster_shop)):
            
            isExist = False
            for i in range(len(f.data_monster_inventory)):
                if f.data_monster_inventory[i][0] == f.data_login[0] and f.data_monster_inventory[i][1] == str(item_id):
                    isExist = True
                    break
            
            if isExist:
                print("Monster tersebut sudah ada dalam inventory-mu! Pembelian dibatalkan.")
            else:
                if int(f.data_monster_shop[item_id][1]) > 0:
                    total_price = f.data_monster_shop[item_id][2]
                    if int(f.data_login[4]) >= int(total_price):                    
                        ubah_koin(-int(total_price))
                        f.data_monster_shop[item_id][1] = str(int(f.data_monster_shop[item_id][1])-1)
                        
                        print(f"Berhasil membeli item: {f.data_monster[item_id][1]}. Item sudah masuk ke inventory-mu!")
                    else:
                        print("OC-mu tidak cukup untuk pembelian ini.")
                else:
                    print('Stok tidak cukup')
        else:
            print("ID Monster tidak ditemukan.")
    elif item_type == "potion":
        item_id = int(input(f">>> Masukkan id {item_type}: "))
        jumlah = int(input('>>> Masukkan jumlah item: '))
        if item_id in range(1,len(f.data_item_shop)):
            if int(f.data_item_shop[item_id][2]) >= jumlah:
                total_price = f.data_item_shop[item_id][3]
                if int(f.data_login[4]) >= int(total_price):                    
                    ubah_koin(-int(total_price)*jumlah)
                    f.data_item_shop[item_id][2] = str(int(f.data_item_shop[item_id][2])-jumlah)
                    
                    print(f"Berhasil membeli item: {f.data_item_shop[item_id][1]} dengan jumlah {jumlah}. Item sudah masuk ke inventory-mu!")
                else:
                    print("OC-mu tidak cukup untuk pembelian ini.")
            else:
                print('Stok tidak cukup')
        else:
            print("ID item tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")


def shop():
    print("\nIrasshaimase! Selamat datang di SHOP!!")
    while True:
        action = input("\n>>> Pilih aksi (lihat/beli/keluar): ")
        if action == "lihat":
            item_type = input(">>> Mau lihat apa? (monster/potion): ")
            if item_type == 'monster' or item_type == 'potion':
                display_shop(item_type)
            else:
                print("Pilihan tidak valid.")
        elif action == "beli":
            buy()
        elif action == "keluar":
            print("\nMr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break
        else:
            print("Pilihan tidak valid.")