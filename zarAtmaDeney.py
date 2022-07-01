import random

def zarAt(kacKere):
    liste = []
    gelenZar = {}
    while True:
        zar1 = random.randint(1, 6)
        zar2 = random.randint(1, 6)
        gelenZar["zar1"] = zar1
        gelenZar["zar2"] = zar2
        liste.append(gelenZar)
        if len(liste) == kacKere:
            break
    return liste

print(zarAt(2))