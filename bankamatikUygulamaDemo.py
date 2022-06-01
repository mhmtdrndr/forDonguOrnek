amount = 1000

print("------------------------------------")
print(" --------- DERINDERE BANK --------- ")
print("------------------------------------")

print("Hoşgeldiniz ->")

sec = ""
while(sec != 0 ):

    print("[1] [ Bakiye Sorma ]")
    print("[2] [ Hesaba Para Yatırma ]")
    print("[3] [ Hesaptan Para Çekme ]")
    print("[0] [ ÇIKIŞ ]")

    sec = int(input("Lütfen seçiminizi yapınız : "))
  
    if (sec == 1):
        print(f"Bakiyeniz : {amount}")
    elif (sec == 2):
        yatirilanTutar = int(input("Yarılan parayı giriniz : "))
        amount = amount + yatirilanTutar
        print(f"Para yatırıldı. Güncel bakiye : {amount}")
    elif (sec == 3):
        celilenTutar = int(input("Çekilen parayı giriniz : "))
        amount = amount - celilenTutar
        print(f"Para çekildi. Güncel bakiye : {amount}")
    else:
        print("Hoşçakalın")
        break