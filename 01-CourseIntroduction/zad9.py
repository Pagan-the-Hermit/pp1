list = [15, 1, 8, 6, 31]

def suma(list):
    suma = 0
    for i in list:
        suma += i
    return suma

def sqsuma(list):
    suma = 0
    for i in list:
        suma += (i**2)
    return suma

print('1. ',suma(list))
print('2. ',sqsuma(list))
print('3. ', 3/5)
print('4. ', list[2] == list[3])