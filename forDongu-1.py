'''
for i in range(1, 6, 1):
  for k in range(i):
    print("*" , end="")
  print("")
'''

text = input("Lütfen yazınızı giriniz : ")

for i in range(0, len(text)):
  for k in range(i+1):
    print(text[k], end="")
  print("")