import src.Functions as f

def logout():  
    if f.data_login == ['','','','','']:
        print('belom login anjing!')
    else:
        f.data_login = ['','','','','']
        print('Logout berhasil')
