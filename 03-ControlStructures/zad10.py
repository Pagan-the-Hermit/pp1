value = input('Podaj liczbe: ')
if int(value) >= 0:
    print(f'|{value}| = {value}')
else:
    print(f'|{value}| = {value[1:]}')