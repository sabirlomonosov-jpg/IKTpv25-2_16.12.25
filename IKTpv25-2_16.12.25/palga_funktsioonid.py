inimesed=["A","B","C","D","E","F"]
palgad=[1000,1200,2500,800,750,1200]

def lisa_andmeid(inimesed, palgad):
    n = int(input("Mitu inimest lisada: "))
    for _ in range(n):
        nimi = input("Nimi: ")
        palk = int(input("Palk: "))
        inimesed.append(nimi)
        palgad.append(palk)

def kustuta_andmeid(inimesed, palgad):
    nimi = input("Sisesta nimi kustutamiseks: ")
    for i in range(len(inimesed)):
        if inimesed[i] == nimi:
            inimesed.pop(i)
            palgad.pop(i)


def suurim_palk(nimed, palgad):
    max_palk = max(palgad)
    print("Suurim palk: ", max_palk)
    print("Saajad:")
    for i in range(len(palgad)):
        if palgad[i] == max_palk:
            print(nimed[i])

def vaikseim_palk(nimed, palgad):
    min_palk = min(palgad)
    print("Vaiksem palk: ", min_palk)
    print("Saajad:")
    for i in range(len(palgad)):
        if palgad[i] == min_palk:
            print(nimed[i])

def jarjesta_palgad(nimed, palgad, kasvav=True):
    for i in range(len(palgad)):
        for j in range(i + 1, len(palgad)):
            if kasvav:
                if palgad[i] > palgad[j]:
                    palgad[i], palgad[j] = palgad[j], palgad[i]
                    nimed[i], nimed[j] = nimed[j], nimed[i]
            else:
                if palgad[i] < palgad[j]:
                    palgad[i], palgad[j] = palgad[j], palgad[i]
                    nimed[i], nimed[j] = nimed[j], nimed[i]
    for i in range(len(nimed)):
        print(nimed[i], ":", palgad[i])

def vordsed_palgad(nimed, palgad):
    kontrol = set()
    leitud = False
    for palk in palgad:
        if palgad.count(palk) > 1 and palk not in kontrol:
            kontrol.add(palk)
            print(f"Palk {palk} saavad:")
            for i in range(len(palgad)):
                if palgad[i] == palk:
                    print(nimed[i])
            leitud = True
    if not leitud:
        print("Võrdseid palku ei leitud.")
