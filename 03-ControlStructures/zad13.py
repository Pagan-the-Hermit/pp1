first = int(input('Podaj pierwszą liczbę: '))
secound = int(input('Podaj drugą liczbę: '))

if first or secound >= 0:
    print(f'Przyznajmniej jedna z liczb {first} i {secound} jest dodatnia')
else:
    print('żadna z liczb nie jest dodatnia')