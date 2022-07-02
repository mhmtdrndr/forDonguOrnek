sayi = int(input("Bir sayı giriniz : "))
toplam = 0 
# gecici_sayi = sayi

while True:
  # basamak = gecici_sayi % 10
  basamak = sayi % 10
  toplam += basamak
  # gecici_sayi = gecici_sayi // 10
  sayi = sayi // 10
  if basamak == 0:
    break

print(toplam)