total = int(input('Podaj liczbe zadań: '))
correct = int(input('Podaj liczbe prawidłowo rozwiązanych zadań: '))

if total/2 < correct:
    print('test zdany')
else:
    print('test niezaliczony')