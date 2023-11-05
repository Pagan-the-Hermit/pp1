f_person = input('Podaj imie pierwszej osoby: ')
f_age = int(input('Podaj wiek pierwszej osoby: '))
s_person = input('Podaj imie drugiej osoby: ')
s_age = int(input('Podaj wiek drugiej osoby: '))

if f_age and s_age >= 18:
    print(f'{f_person} oraz {s_person} są dorośli')
if f_age and s_age < 18:
    print(f'{f_person} oraz {s_person} nie są dorośli')
if f_age >= 18 and s_age < 18:
    print(f'{f_person} jest dorosły a {s_person} nie jest dorosły')
if f_age < 18 and s_age >= 18:
    print(f'{f_person} nie jest dorosły a {s_person} jest dorosły')