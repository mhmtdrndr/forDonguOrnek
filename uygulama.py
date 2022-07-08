
def harfNotuHesapla(param):
    if param >= 90:
        return 'AA'
    elif param >= 80 and param <= 89:
        return 'BA'
    elif param >= 75 and param <= 79:
        return 'BB'
    elif param >= 70 and param <= 75:
        return 'CB'
    elif param >= 60 and param <= 69:
        return 'CC'
    elif param >= 50 and param <= 59:
        return 'DC'
    elif param >= 40 and param <= 49:
        return 'DD'
    elif param >= 30 and param <= 39:
        return 'FD'
    elif param >= 0 and param <= 29:
        return 'FF'

def notHesapla(satir):
    
    satir = satir[:-1]
    liste = satir.split(':')
    
    ogrenciAd = liste[0]
    ogrenciNotlari = liste[1].split(',')
    vizeNot1 = int(ogrenciNotlari[0].strip())
    vizeNot2 = int(ogrenciNotlari[2].strip())
    final = int(ogrenciNotlari[2].strip())
    
    ortalama = (vizeNot1*0.3 + vizeNot2*0.3 + final*0.4)
    
    print(f"{ogrenciAd} isimli öğrencinin not ortalaması : {ortalama} ve başarı notu : {harfNotuHesapla(ortalama)}")
    

def notOku():
    
    with open("sinav_sonuclari.txt","r", encoding="utf-8") as file:
        for satir in file.readlines():
            print(notHesapla(satir))

def notGir():
    
    ad = input("Öğrenci Adı : ")
    soyad = input("Öğrenci Soyadı : ")
    vize1 = input("Birinci Vize Notu : ")
    vize2 = input("İkinci Vize Notu : ")
    final = input("Final Vize Notu : ")
    
    with open("sinav_sonuclari.txt","a", encoding="utf-8") as file:
        file.write(ad.upper() + " " + soyad.upper() + " " + " : " + vize1 + "," + vize2 + "," + final+"\n")

def notKaydet():
    pass


while True:
    print("1. Notları Oku")
    print("2. Not Gir")
    print("3. Notları Kaydet")
    print("4. Çıkış")   
    
    try:
        secim = int(input('Seçiminizi Yapınız : '))
        
        if secim == 4:
            print("Başarılı bir şekilde çıkış yapıldı...")
            break
        elif secim == 1:
            notOku()        
        elif secim == 2:
            notGir()
        elif secim == 3:
            notKaydet()
        else:
            print("HATA !!! : Seçiminiz hatalı ! Yeniden deneyin")        
    except ValueError:
        print("!!! HATA : 1 ile 4 arasında bir değer giriniz")