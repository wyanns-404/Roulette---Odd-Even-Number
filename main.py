# Revisi line 22, 76

import random # Gibe----------------------------------------------------------------------------------------
import os

def header():   
    print("┌─────────────────────────────┐")
    print("│    ~    Odd or Even     ~   │")
    print("└─────────────────────────────┘\n")

# OOP
class Dadu:
    def __init__(self):
        self.value = None
    
    def roll(self):
        self.value = random.randint(1, 6) # Gibe--------------------------------------------------------------

# Array ()
dadu = ["","\n┌─────────┐\n│         │\n│    ●    │\n│         │\n└─────────┘\n", # wayan--------------------------------------------------------------
        "\n┌─────────┐\n│  ●      │\n│         │\n│      ●  │\n└─────────┘\n",
        "\n┌─────────┐\n│  ●      │\n│    ●    │\n│      ●  │\n└─────────┘\n",
        "\n┌─────────┐\n│  ●   ●  │\n│         │\n│  ●   ●  │\n└─────────┘\n",
        "\n┌─────────┐\n│  ●   ●  │\n│    ●    │\n│  ●   ●  │\n└─────────┘\n",
        "\n┌─────────┐\n│  ●   ●  │\n│  ●   ●  │\n│  ●   ●  │\n└─────────┘\n"
        ]

def dadu_gambar(x):
    if 0 < x < 7:
        print(dadu[x])
    else:
        print("Mohon maaf terjadi kesalahan sistem.") # Wayan--------------------------------------------------------------

def main(): # ALin--------------------------------------------------------------
    os.system("cls")
    header()

    saldo = int(input("Masukkan saldo anda = $"))
    dadu = Dadu()

    while True:
        os.system("cls")
        header()
        print("Saldo : $",saldo)

        taruhan = int(input("Masukkan taruhan : $"))
        print("\nTebak :")
        print("[1] Ganjil")
        print("[2] Genap")
        pilih = int(input("(1 / 2) : "))

        dadu.roll()
        dadu_gambar(dadu.value)

        print("Jumlah dadu : ", dadu.value) # Alin--------------------------------------------------------------
        
        if dadu.value % 2 == 0: # Gibe--------------------------------------------------------------
            if pilih == 2:
                saldo += taruhan
                print("\nSaldo anda bertambah $",taruhan)
            else:
                saldo -= taruhan
                print("\nSaldo anda berkurang $",taruhan)
        else:
            if pilih == 1:
                saldo += taruhan
                print("\nSaldo anda bertambah $",taruhan)
            else:
                saldo -= taruhan
                print("\nSaldo anda berkurang $",taruhan)

        print("Total Saldo Sekarang : $",saldo) # Gibe--------------------------------------------------------------

        if saldo == 0: # Wayan--------------------------------------------------------------
            print("\nSaldo anda tidak cukup.")
            input("Tekan ENTER untuk keluar...")
            break

        repeat = input("\n\nApakah Anda ingin bermain lagi ( y / n ) : ")
        if repeat.lower() != "y":
            break # Wayan--------------------------------------------------------------

    os.system("cls") # Alin--------------------------------------------------------------
    print("┌─────────────────────────────┐")
    print("│    ~  Have a Nice Day   ~   │")
    print("└─────────────────────────────┘\n")

    if saldo > 0:
        print("Total saldo anda : $",saldo)

if __name__ == "__main__":
    main() # Alin--------------------------------------------------------------
