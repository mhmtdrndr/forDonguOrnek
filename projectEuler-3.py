'''
Kısa Yol

number = 600851475143
i = 2

while i * i < number:
  while number % i == 0:
    number = number / i
  i += 1

print(int(number))

'''

# uzun yol

def primeCheck(x):
    isPrime = True
    for i in range(2,x):
        if x % i == 0:
            isPrime = False
            break
        else:
            isPrime = True

    return isPrime

# number = 13195
number = 600851475143
list = []
i = 2

while i * i < number:
    if (number % i == 0) and primeCheck(i):
        list.append(i)
    i += 1

print(max(list))