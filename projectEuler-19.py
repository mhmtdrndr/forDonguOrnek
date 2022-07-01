# 01 Ocak 1901 den 31 Aralık 2000'e kadar kaç sefer bir ayın ilk günü pazar olur?
import datetime

pazarSayisi = 0

for yil in range(1901,2001):
    for ay in range(1,13):
        if datetime.date(yil,ay,1).isoweekday() == 7:
            pazarSayisi += 1

print(pazarSayisi)