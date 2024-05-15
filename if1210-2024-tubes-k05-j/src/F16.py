
import src.Functions as f
import src.F15 as sv

def exit():
    while True:
        mau_save = input('save duls gasi? (y/n): ')
        if mau_save == 'y':
            sv.save()
            break
        elif mau_save == 'n':
            break