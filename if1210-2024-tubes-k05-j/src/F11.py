def load_data(data, level):
    list = []
    with open(data, 'r') as file:
        # Lewati header
        file.readline()
        nilai = ''
        kolom = 0
        for line in file:
            for char in line:
                if char == ';':  # akhir nilai
                    if kolom == level:
                        list.append(nilai)
                    nilai = ''
                    kolom += 1
                elif char == '\n':  # akhir baris
                    if kolom == level:
                        list.append(nilai)
                    nilai = ''
                    kolom = 0
                else:
                    nilai += char
    return list

oc_agent = 1000 # masih perlu dihubungkan dengan koin agent yang sedang login
level = load_data('src/monster_inventory.csv', 2)
type = load_data('src/monster.csv', 1)

print("LABORATORY")
print("Selamat datang di Lab Dokter Asep !!!")
print("============ MONSTER LIST ============")
for i in range(len(level)):
    print(f"{i+1}. {type[i]} (Level: {level[i]})")

print("\n============ UPGRADE PRICE ============")
price = [200, 500, 700, 1100]
for i in range(len(price)):
    print(f"{i+1}. Level {i+1} -> Level {i+2}: {price[i]} OC")
    i += 1
print(" ")

option = int(input(">>> Pilih Monster: "))
level_int = [int(numeric_string) for numeric_string in level]
if (level_int[option-1]+1) == 5:
    print("Maaf, monster yang Anda pilih sudah memiliki level maksimum.")
else:
    print(f"{type[option-1]} akan di-upgrade ke level {level_int[option-1]+1}.")
    if (level_int[option-1]+1) == 2:
        harga = price[0]
    elif (level_int[option-1]+1) == 3:
        harga = price[1]
    elif (level_int[option-1]+1) == 4:
        harga = price[2]
    elif (level_int[option-1]+1) == 5:
        harga = price[3]
    print(f"Harga untuk melakukan upgrade {type[option-1]} adalah {harga}.\n")
ans = input(">>> Lanjutkan upgrade (Y/N): ")
if (ans == 'Y'):
    if (oc_agent >= harga) :
        oc_agent -= harga
        print(f"Selamat, {type[option-1]} berhasil di-upgrade ke level {level_int[option-1]+1} !")
    else:
        print("Maaf, jumlah OC tidak cukup untuk melakukan upgrade.")
# else: {jika ans == 'N' tidak terjadi apa-apa untuk sementara}
# masih belum dihubungkan dengan status apakah sudah di save atau tidak
