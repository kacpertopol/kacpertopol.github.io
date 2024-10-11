#!/usr/bin/env python3

def silnia(n):
    x = 1
    for i in range(1 , n + 1):
        x = x * i
    return x

nValue = input("Proszę wprowadzić wartość n do policzenia n! : ")

print(silnia(int(nValue)))

input("Proszę wcisnąć enter aby zakończyć.")
