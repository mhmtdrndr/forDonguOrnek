sum = 0
number_list = []

for i in range(1,1000):
    if (i % 3 == 0) or (i % 5 == 0) :
        number_list.append(i)
        sum += i

print(number_list)

print(f"1000'in altındaki 3 veya 5'in tüm katlarının toplamı : {sum}")