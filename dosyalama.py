# with open("dosyaislemleri.txt") as file:
#   print(file.read())

# with open("dosyaislemleri.txt") as file:
#   print(file.readline())
#
# with open("dosyaislemleri.txt")as file:
#   print(file.readlines())

with open("dosyaIslemleri.txt","r") as file:
  icerik = file.readlines()
  for satir in icerik:
    print(satir, end=" ")