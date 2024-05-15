
import src.Functions as f

# Program F01 - REGISTER
def register():    
    if f.data_login != ['','','','','']: # ngecek islogin
        print(f"Register gagal!")
    else:
        print('REGISTER')
        user = input("Masukkan username: ")
        password = input("Masukkan password: ")

        isValid = True # validasi username
        for i in range(len(f.data_user)): # ngecek username di database
            if (user == f.data_user[i][1]):
                print(f"Username {user} sudah terpakai, silahkan gunakan username lain!")
                isValid =  False
                break

        if isValid: # jika username valid
            if not f.validate_username(user):
                print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            else:
                print("Silahkan pilih salah satu monster sebagai monster awalmu.")
                for i in range(1,len(f.data_monster)-1):
                    print(f"{i}. {f.data_monster[i][1]}")
                
                monster_id = input("Monster pilihanmu: ")
                f.data_monster_inventory += [[str(len(f.data_user)),monster_id,'1']]
                f.data_user += [[str(len(f.data_user)),user,password,'agent','0']]
                f.data_login = f.data_user[-1]
                
                print(f"Selamat datang Agent {user}. Mari kita mengalahkan Dr. Asep Spakbor dengan {f.data_monster[int(monster_id)][1]}!")