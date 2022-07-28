#listNumber = [1,2,3,4,5,6,7,8,9,10]

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