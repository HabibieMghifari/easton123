import os
import src.Functions as f

def save():
    nama_folder = input('masukkan nama folder: ')
    
    isExist = False
    for folder in os.listdir('data'): # cek folder data apa aja
        if folder == nama_folder:
            isExist = True
            break
        
    # membuat folder baru
    if not isExist: 
        os.makedirs(f'data/{nama_folder}')
    # menambahkan csv dalam folder save
    f.csvwriter(f'data/{nama_folder}/user.csv', f.data_user)
    f.csvwriter(f'data/{nama_folder}/monster.csv', f.data_monster)
    f.csvwriter(f'data/{nama_folder}/item_inventory.csv', f.data_item_inventory)
    f.csvwriter(f'data/{nama_folder}/monster_inventory.csv', f.data_monster_inventory)
    f.csvwriter(f'data/{nama_folder}/item_shop.csv', f.data_item_shop)
    f.csvwriter(f'data/{nama_folder}/monster_shop.csv', f.data_monster_shop)

    print(f"Berhasil menyimpan data di folder {nama_folder}.")