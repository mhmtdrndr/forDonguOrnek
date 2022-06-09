def asalMi(sayi):
  for i in range(2,sayi):
   if sayi % i == 0:
       return False
       break
   else:
       return True 

sayi = int(input("Sayı : "))

if asalMi(sayi):
  print(f"Girilen {sayi} sayısı ASAL dır.")
else:
  print(f"Girilen {sayi} sayısı asal değil.") 