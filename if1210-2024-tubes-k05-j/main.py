
import src.Functions as f
import src.F01 as reg
import src.F02 as lgn
import src.F03 as lgt
import src.F04 as hlp
import src.F14 as ld
import src.F15 as sv
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
    elif command == 'exit':
        while True:
            mau_save = input('save duls gasi? (y/n): ')
            if mau_save == 'y':
                sv.save()
                break
            elif mau_save == 'n':
                break
        break

    
 

