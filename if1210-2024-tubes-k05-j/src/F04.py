# fungsi help sebelum login
def help_BeforeLogin():
     print("""
=========== HELP ===========

Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.

Login: Masuk ke dalam akun yang sudah terdaftar
Register: Membuat akun baru

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid
""")
     
#Fungsi help Login sebagai Agent
def help_agent (username):
    print(f"""
=========== HELP ===========

Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:

Logout: Keluar dari akun yang sedang digunakan
Inventory: Melihat owca-dex yang dimiliki oleh Agent

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid
""")
    
# Fungsi help login sebagai Admin
def help_admin(username):
    print( f"""
=========== HELP ===========

Selamat datang, Admin {username}. Berikut adalah hal-hal yang dapat kamu lakukan:

Logout: Keluar dari akun yang sedang digunakan
Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent


# ...dan seterusnya

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid

""")

# Fungsi untuk logout
def logout(user):
    if user:
        print(f"Goodbye, {user}!")
        return None
    else:
        print("Kamu belum login.")
        return user

# Fungsi untuk login
def login(role, username=""):
    print(f"Selamat datang, {role} {username}!")
    return {"role": role, "name": username}

# Fungsi untuk menampilkan bantuan
def help_menu(user):
    if not user:
        help_BeforeLogin()
    elif user["role"] == "Agent":
        help_agent(user["name"])
    elif user["role"] == "Admin":
        help_admin(user["name"])
    else:
        print("Role tidak valid.")

# Contoh penggunaan
active_user = None
help_menu(active_user)

# Login sebagai Agent
active_user = login("Agent", "Purry")
help_menu(active_user)

# Logout
active_user = logout(active_user)

# Login sebagai Admin
active_user = login("Admin", "AdminX")
help_menu(active_user)
        
