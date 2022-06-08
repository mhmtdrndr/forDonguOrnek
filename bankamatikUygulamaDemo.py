'''
    V.1.1
'''

def bakiyeDurum(amount):
    print(f"Bakiyeniz : {amount}")
    
def paraYatir(amount):
    yatirilanTutar = int(input("Yarılan parayı giriniz : "))
    if yatirilanTutar < 0:
        print("Girilen tutar hatalı")
    else: 
        amount = amount + yatirilanTutar
        print(f"Para yatırıldı. Güncel bakiye : {amount}")
        
    return amount

def paraCek(amount):
    celilenTutar = int(input("Çekilen parayı giriniz : "))    
    if celilenTutar > amount:
        print("Bakiye yerli değil")
    else:
        amount = amount - celilenTutar
        print(f"Para çekildi. Güncel bakiye : {amount}")
    
    return amount    

print("------------------------------------")
print(" --------- XXXXXXXXX BANK --------- ")
print("------------------------------------")

print("Hoşgeldiniz ->")

amount = 1000
durum = True
while durum:

    print("[1] [ Bakiye Sorma ........ ]")
    print("[2] [ Hesaba Para Yatırma . ]")
    print("[3] [ Hesaptan Para Çekme . ]")
    print("[0] [ ÇIKIŞ ............... ]")

    sec = int(input("Lütfen seçiminizi yapınız : "))
  
    if (sec == 1):
        bakiyeDurum(amount)
    elif (sec == 2):        
        paraYatir(amount)
    elif (sec == 3):
        paraCek(amount)
    else:
        print("Hoşçakalın")
        durum = False