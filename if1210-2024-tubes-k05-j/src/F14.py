
import src.Functions as f
import os

def load():
    while True:
        nama_folder = input('masukkan nama folder: ')
        
        isExist = False
        for folder in os.listdir('data'):
            if folder == nama_folder:
                isExist = True
                break
        
        if isExist:
            break
        else:
            print('folder tidak ditemukan!')
        
    f.data_user = f.read_csv(f'data/{nama_folder}/user.csv')
    f.data_monster = f.read_csv(f'data/{nama_folder}/monster.csv')
    f.data_item_inventory = f.read_csv(f'data/{nama_folder}/item_inventory.csv')
    f.data_monster_inventory = f.read_csv(f'data/{nama_folder}/monster_inventory.csv')
    f.data_item_shop = f.read_csv(f'data/{nama_folder}/item_shop.csv')
    f.data_monster_shop = f.read_csv(f'data/{nama_folder}/monster_shop.csv')