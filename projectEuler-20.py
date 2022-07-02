def factoriyelAl(number):
    faktoriyel = 1
    i = 1
    while i <= number:
        faktoriyel = faktoriyel * i
        i += 1
    return faktoriyel

def rakamlariTopla(number):
    toplam = 0
    temp_number = number
    while True:
        basamak = temp_number % 10
        toplam += basamak
        temp_number = temp_number // 10
        if temp_number == 0:
            break
    return toplam

factoriyelNumber = int(input("Faktroyeli hesaplanacak olan sayı : "))

basamakToplam = factoriyelAl(factoriyelNumber)
print(f'''{factoriyelNumber} sayısının faktoriyeli : {factoriyelAl(factoriyelNumber)} ve
faktoriyel sonucu çıkan sayının rakamları toplamı : {rakamlariTopla(basamakToplam)}''')
