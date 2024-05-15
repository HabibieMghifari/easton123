
import src.Functions as f

def login():
    if f.data_login != ['','','','','']: # ngecek islogin
        print('Login gagal')
    else:
        print('LOGIN')
        user = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        isExist = False
        for i in range(len(f.data_user)):
            if f.data_user[i][1] == user and f.data_user[i][2] == password:
                id = i
                isExist = True
                break

        if isExist: # jika username valid dan ada
            f.data_login = f.data_user[id]
            print(f"Login berhasil")
        else:
            print('Login gagal')
