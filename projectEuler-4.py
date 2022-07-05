def palindromeCheck(x):
    value = str(x)
    reverseValue = value[::-1]
    if value == reverseValue:
        return True
    else:
        return False

palindromeList = []

for i in range(100,1000):
    for j in range(100,1000):
        if (palindromeCheck(i * j)):
            palindromeList.append(i*j)

print(palindromeList)
print(max(palindromeList))