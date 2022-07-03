'''
    ilk 10 fibonachi sayılarını bulan program
'''

fiboNumber = []
x = 0
y = 1

while True:
    fiboNumber.append(x + y)
    x , y = y , x + y # x'in degerini y'ye y'nin değerini de x + y'ye eşitledik
    if len(fiboNumber) == 10:
        break 

print(fiboNumber)
