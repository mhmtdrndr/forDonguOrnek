import random

def createCompHand():
    n = random.randint(1,3)
    if n==1:
        return "tas"
    elif n==2:
        return "kagit"
    else:
        return "makas"

myScore = 0
compScore = 0

while True:

  myHand = input("tas ?, kagit ? , makas ? : ")
  compHand = createCompHand()
  print(f"Bilgisayar : {compHand}")

  if  myHand == compHand:
      print("Berabere")
  elif myHand == "kagit" and compHand == "tas":
      myScore += 1
  elif myHand == "tas" and compHand == "makas":
      myScore += 1
  elif myHand == "makas" and compHand == "kagit":
      myScore += 1
  else:
      compScore += 1

  print(f"Skorunuz : {myScore}, Bilgisayar: {compScore}") 

  if (myScore == 3 or compScore ==3):
    break

if (myScore > compScore):
  print("Siz kazandınız")
else:
  print("Kaybettiniz :(")