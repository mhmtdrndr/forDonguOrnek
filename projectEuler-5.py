# from math import lcm
# from math import factorial

# print(lcm(*range(1,21)))

# print(factorial(10)) 

# def ekok(n1, n2):
#     ekok = 1
#     if n1 > n2:
#         ekok = n1
#     else:
#         ekok = n2
    
#     for i in range(ekok, n1*n2+1):
#         if i % n1 == 0 and i % n2 == 0:
#             return i

# result = ekok(6, 9)
# print(result)

def ekok(num):
    
    def factorial(x):
        f, i = 1, 1
        while i <= x:
            f = f * i
            i = i + 1
        return f

    for i in range(1, factorial(num) + 1):
        if (i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0
            and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0):
            return i
 

result = ekok(20)
print(result)
   