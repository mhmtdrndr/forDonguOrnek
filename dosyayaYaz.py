
ogrenci_bilgi = input("Öğrenci Adını Giriniz : ")
vizeNotu = float(input("Vize Notunu Giriniz : "))
finalNotu = float(input("Final Notunu Giriniz : "))

sonuc = (vizeNotu*0.4 + finalNotu*0.6)

if sonuc >= 85:
    harfNotu = "AA"
elif sonuc >= 70:
    harfNotu = "BA"
elif sonuc >= 60:
    harfNotu = "BB"
elif sonuc >= 50:
    harfNotu = "CB"
elif sonuc >= 40:
    harfNotu = "CC"
else:
    harfNotu = "FF"

print(f"{ogrenci_bilgi} adlı öğrencinin not ortalaması : {sonuc}")

with open("sinavSonuclari.txt","a") as dosya:
    dosya.writelines(f"{ogrenci_bilgi} adlı öğrencinin not ortalaması : {sonuc} , harf notu : {harfNotu}\n") 