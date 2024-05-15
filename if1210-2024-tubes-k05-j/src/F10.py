import Functions as f

OWCA_coin = 1000 #ini belum ada jadi baru asumsi

mons_id = f.read_csv('data/monster_shop.csv',0)
stok = f.read_csv('data/monster_shop.csv', 1)
harga = f.read_csv('data/monster_shop.csv', 2)

potion_id = f.read_csv('data/item_shop.csv', 0)
tipe = f.read_csv('data/item_shop.csv', 1)
stock = f.read_csv('data/item_shop.csv', 2)
price = f.read_csv('data/item_shop.csv', 3)

mons_inv = f.read_csv('data/monster_inventory.csv',0)
pot_inv = f.read_csv('data/item_inventory.csv',0)

def display_shop(item_type): 
    if item_type == "monster":
        print("ID | Type                | ATK Power | DEF Power | HP   | Stok | Harga")  
        for i in range(len(mons_id)):
            print(f"{mons_id[i]}  | {type[i]:<19} | {atk_power[i]:<9} | {def_power[i]:<9} | {hp[i]:<4} | {stok[i]:<4} | {harga[i]}")
    elif item_type == "potion":
        print("ID | Type                | Stok | Harga") 
        for i in range(len(potion_id)):         
            print(f"{potion_id[i]}  | {tipe[i]:<19} | {stock[i]:<4} | {price[i]}")
    print()

def buy(OWCA_coin, mons_inv, harga, stock, price, type):
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {OWCA_coin}.")
    item_type = input(">>> Mau beli apa? (monster/potion): ")
    if item_type == "monster":
        item_id = int(input(f">>> Masukkan id {item_type}: "))
        if item_id in mons_id:
            if item_id in mons_inv:
                print("Monster tersebut sudah ada dalam inventory-mu! Pembelian dibatalkan.")
            else:
                if item_id in harga:
                    total_price = harga[mons_id][item_id]
                    if OWCA_coin >= total_price:
                        OWCA_coin -= total_price
                        print(f"Berhasil membeli item: {type[mons_id][item_id]}. Item sudah masuk ke inventory-mu!")
                    else:
                        print("OC-mu tidak cukup untuk pembelian ini.")
                else:
                    print("ID Monster tidak ditemukan.")
    elif item_type == "potion":
        item_id = int(input(f">>> Masukkan id {item_type}: "))
        if item_id not in stock:
            print("ID Potion tidak ditemukan.")
        else:
            quantity = int(input(f">>> Masukkan jumlah: "))
            if quantity > stock[item_id]:
                print("Maaf, stok item tidak cukup.")
            else:
                total_price = price[potion_id][item_id] * quantity
                if OWCA_coin >= total_price:
                    OWCA_coin -= total_price
                    stock[potion_id][item_id] -= quantity
                    print(f"Berhasil membeli {quantity} {type[potion_id][item_id]}. Item sudah masuk ke inventory-mu!")
                else:
                    print("OC-mu tidak cukup untuk pembelian ini.")
    else:
        print("Pilihan tidak valid.")
    return OWCA_coin, mons_inv, stock


def SHOP():
    global OWCA_coin
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
            buy(OWCA_coin, mons_id, harga, stock, price, type)
        elif action == "keluar":
            print("\nMr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break
        else:
            print("Pilihan tidak valid.")

# Main program
SHOP()