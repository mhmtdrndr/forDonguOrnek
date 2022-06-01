#Faktöriyel hesaplama
sayi = int(input("Faktöriyeli hesaplanacak olan sayı : "))
faktoriyel = 1
i = 1

#while döngüsü ile
while i<=sayi:
  faktoriyel = faktoriyel * i
  i = i+1
print(faktoriyel)

#for döngüsü ile
for i in range(sayi):
  faktoriyel * faktoriyel * i
print(faktoriyel)