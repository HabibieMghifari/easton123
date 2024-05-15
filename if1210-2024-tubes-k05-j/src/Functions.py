import os

def validate_username(username):
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    for char in username:
        if not char in valid_chars:
            return False
    return True

def csvwriter(file_name, data):
    with open(file_name, 'w', newline='') as file:
        for row in data:
            file.write(';'.join(map(str, row)) + '\n')
        
def split_str(string : str,delimiter : str) -> list[str]:
    # variable lokal
    array : list[str] # hasil split
    limit : int # membatasi string untuk ditambah ke array
    
    array = []
    limit = 0
    for i in range(len(string)):
        if string[i] == delimiter:
            array += [string[limit:i]]
            limit = i+1
    array += [string[limit:]]
    return array            

# fungsi membaca file csv sebagai matriks
def read_csv(file_name : str) -> list[list[str]]:
    # variable lokal
    data : list[list[str]] # hasil read
    
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            row = split_str(line[:-1],';')
            data += [row]
    return data

data_login = ['','','','','']
data_user = []
data_monster = []
data_monster_inventory = []
data_item_inventory = []
data_item_shop = []
data_monster_shop = []