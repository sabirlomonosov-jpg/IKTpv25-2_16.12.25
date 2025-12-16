import abc
from random import *
from string import *

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


