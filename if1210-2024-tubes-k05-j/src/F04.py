
import src.Functions as f

# fungsi help sebelum login
def help():
    if f.data_login[3] == '':
        print("""
=========== HELP ===========

Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.

Login: Masuk ke dalam akun yang sudah terdaftar
Register: Membuat akun baru

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid
""")
    elif f.data_login[3] == 'agent':
        print(f"""
=========== HELP ===========

Halo Agent {f.data_login[1]}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:

Logout: Keluar dari akun yang sedang digunakan
Inventory: Melihat owca-dex yang dimiliki oleh Agent

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid
""")
    elif f.data_login[3] == 'admin':
        print( f"""
=========== HELP ===========

Selamat datang, Admin {f.data_login[1]}. Berikut adalah hal-hal yang dapat kamu lakukan:

Logout: Keluar dari akun yang sedang digunakan
Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent


# ...dan seterusnya

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid

""")    
