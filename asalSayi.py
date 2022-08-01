'''
def isPrime(number):
  for i in range(2,int(number**0.5)+1):
    if number % i == 0:
      return False
  return True
'''

def isPrime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

sayi = int(input("Sayı : "))

if isPrime(sayi):
  print(f"Girilen {sayi} sayısı ASAL dır.")
else:
  print(f"Girilen {sayi} sayısı asal değil.") 
