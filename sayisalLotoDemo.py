from random import randint

listSayilar = []
sayac = 0

while sayac < 6:
    for i in range(len(listSayilar), 6):
        deger = randint(1, 49)
        if deger in listSayilar:
            i = i - 1
        else:
            listSayilar.append(deger)
            sayac += 1

listSayilar.sort()
print(listSayilar)
