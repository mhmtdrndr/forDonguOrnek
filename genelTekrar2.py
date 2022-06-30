# ilk 10000 asal sayının kaç tanesi 3 ile başlar 7 ile biter

prime_list = []
prime_list.append(2)

sayi = 3

while True:
    prime = True
    for i in range(2,int(sayi ** 0.5 + 1)):
        if sayi % i == 0:
            prime = False
            break

    if prime:
        prime_list.append(sayi)
        if len(prime_list) == 10000:
            break

    sayi += 1

prime_list_2 = []

for value in prime_list:
    strValue = str(value)
    if strValue.startswith("3") and strValue.endswith("7"):
        prime_list_2.append(strValue)

print(prime_list_2)

# ---------------------------------------------------------------------------------------------------------------------

# üç basamaklı sayıların kaç tanesi rakamlarının küplerinin toplamına eşittir

liste = []

for sayi in range(100,1000):

    toplam = 0
    geciciSayi = sayi

    while geciciSayi != 0:
        basamak = geciciSayi % 10
        toplam += basamak ** 3
        geciciSayi //= 10

    if toplam == sayi:
        liste.append(sayi)

print(liste)

# ---------------------------------------------------------------------------------------------------------------------

# ilk 100 fibonacci sayısını ekrana yazdıran programı yazınız

fiboList = []
fiboList.append(1)
fiboList.append(1)

index = 2

while True:
    fiboList.append(fiboList[index - 2] + fiboList[index - 1])
    index += 1

    if len(fiboList) == 100:
        break

print(fiboList)
