def ekok(n1, n2):
    ekok = 1
    if n1 > n2:
        ekok = n1
    else:
        ekok = n2
    
    for i in range(ekok, n1*n2+1):
        if i % n1 == 0 and i % n2 == 0:
            return i

result = ekok(6, 9)
print(result)