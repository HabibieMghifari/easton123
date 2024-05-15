
import src.Functions as f
import src.F01 as reg
import src.F02 as lgn
import src.F03 as lgt
import src.F04 as hlp
import src.F10 as shp
import src.F14 as ld
import src.F15 as sv
import src.F16 as ext
import os

os.chdir('if1210-2024-tubes-k05-j')

ld.load()
while True:
    command = input('>>> ')
    if command == 'register':
        reg.register()
    elif command == 'login':
        lgn.login()
    elif command == 'logout':
        lgt.logout()
    elif command == 'help':
        hlp.help()
    elif command == 'save':
        sv.save()
    elif command == 'shop' and f.data_login[3] =='agent':
        shp.shop()
    elif command == 'exit':
        ext.exit()
        break

    
 

