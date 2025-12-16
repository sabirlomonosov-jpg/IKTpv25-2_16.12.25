from ast import Try
from palga_funktsioonid import *
inimesed=["A","B","C","D","E","F"]
palgad=[1000,1200,2500,800,750,1200]

while True:
    print(f"Inimesed {inimesed}")
    print(f"Palgad {palgad}")

    print("1. Lisa Andmeid.")
    print("2. Kustuta Andmeid.")
    print("3. Suurim Palk.")
    print("4. Väikseim Palk.")
    print("5. Järjestamine.")
    print("6. Võrdsed Palgad.")
    print("7. Palga Otsing Nime Järgi.")

    v = input("Valik: ")
    
    if v == "1":
            lisa_andmeid(inimesed, palgad)

    elif v == "2":
            kustuta_andmeid(inimesed, palgad)

    elif v == "3":
            suurim_palk(inimesed, palgad)

    elif v == "4":
            vaikseim_palk(inimesed, palgad)

    elif v == "5":
            jarjesta_palgad(inimesed, palgad)

    elif v == "6":
            vordsed_palgad(inimesed, palgad)

    else:
            palga_otsing(inimesed, palgad)
