def powIndex(*param):    
    t = 0
    for i in param:
        t += i ** 2        
    return t

def sumPow(*param):
    t = 0
    for i in param:
        t += i
    return (t ** 2)

listNumber = [ x for x in range(1,101) ]

pi = powIndex(*listNumber)

sp = sumPow(*listNumber)

print(sp - pi)