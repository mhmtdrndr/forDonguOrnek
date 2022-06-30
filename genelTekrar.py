# ekrandan alınan bir sayının faktöriyelini hesaplayan programı yazınız :

faktoriyelHesaplanacakSayi = int(input("Faktöriyeli hesaplanacak sayıyı giriniz : "))

def faktoriyelHesapla(faktoriyelHesaplanacakSayi):

    for i in range(1,faktoriyelHesaplanacakSayi):
        faktoriyelHesaplanacakSayi = i * faktoriyelHesaplanacakSayi

    return faktoriyelHesaplanacakSayi

print(f"Girilen {faktoriyelHesaplanacakSayi} sayısının faktöriyeli : {faktoriyelHesapla(faktoriyelHesaplanacakSayi)}")


# ---------------------------------------------------------------------------------------------------------------------

# ekrandan alınan bir sayının asal olup olmadığını hesaplayan programı yazınız :

def asalMi(sayi):
    for i in range(2,sayi):
        if sayi % i == 0:
            return False
            break
        else:
            return True

asalSayiKontrol = int(input("Sayı giriniz : "))

if asalMi(asalSayiKontrol):
    print(f"Girilen {asalSayiKontrol} asaldır")
else:
    print(f"Girilen {asalSayiKontrol} asal değil")


# ---------------------------------------------------------------------------------------------------------------------

# ekrandan alınan bir sayının kaç adet pozitif böleni olduğunu bulan hesaplayan programı yazınız :

def pozitifBolenBul(x):

    pozitifBolenSayisi = 0

    for i in range(1, x+1):
        if x % i == 0:
            pozitifBolenSayisi += 1

    return pozitifBolenSayisi

sayi = int(input("Sayıyı Giriniz : "))

print(f"{sayi} sayısının poritif bölen sayısı : {pozitifBolenBul(sayi)}")


# ---------------------------------------------------------------------------------------------------------------------

# ekrandan alınan bir sayının rakamlarını toplayan programı hesaplayan programı yazınız :

def rakamlariTopla(sayi):

    strSayi = str(sayi)
    toplam = 0
    for rakam in strSayi:
        toplam += int(rakam)

    return toplam

rakamlariToplanacakSayi = int(input("Sayıyı Giriniz : "))

print(f"Girilen {rakamlariToplanacakSayi} sayısının rakamları toplamı : {rakamlariTopla(rakamlariToplanacakSayi)}")

# ---------------------------------------------------------------------------------------------------------------------

# ekrandan alınan 5 adet sayının en küçüğünü ve en büyüğünü bulan programı yazınız :

valueList = []
for i in range(1,6):
    sayi = int(input(f"{i}. sayıyı giriniz : "))
    valueList.append(sayi)

print(valueList)
maxValue = max(valueList)
minValue = min(valueList)
print(f"Girilen sayılardan en büyük sayı : {maxValue}\nGirilen sayılardan en küçük sayı : {minValue}")

# ---------------------------------------------------------------------------------------------------------------------

# ekrandan alınan  sayının karekökünün olup olmadığını bulan programı yazınız :

sayi = int(input("Sayıyı Giriniz : "))

kareKok = sayi ** 0.5

if kareKok == int(kareKok):
    print(f"Girilen {sayi} sayısının karekökü var")
else:
    print(f"Girilen {sayi} sayısının karekökü YOK")

# ---------------------------------------------------------------------------------------------------------------------

# ekrandan alınan bir metinde hangi harfin kaç kere yazıldığını bulan programı yazınız :

metin = input("Bir metin giriniz. : ")

metinSozluk = dict()

for harf in metin:
    if harf in metinSozluk:
        metinSozluk[harf] += 1
    else:
        metinSozluk[harf] = 1

print(metinSozluk)

for harf,adet in metinSozluk.items():
     print(harf,adet)


# ---------------------------------------------------------------------------------------------------------------------

# ekrandan alınan bir metinde a harflerini büyük yapan programı yazınız :

metin = input("Bir metin giriniz . : ")

metin2 = ""

for harf in metin:
    if harf == "a":
        metin2 += "A"
    else:
        metin2 +=harf

print(metin2)
