def isPrime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

primeNumberList = [2]
value = 3

while len(primeNumberList) < 10001:
    if isPrime(value):
        primeNumberList.append(value)
    value += 1
    
#print(primeNumberList)
print(primeNumberList[-1])