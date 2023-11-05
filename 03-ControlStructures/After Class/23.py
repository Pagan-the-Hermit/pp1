h_age = int(input('Enter the dogs age in human years: '))
dog_age = 0
if h_age >= 2:
    dog_age = 21
    for i in range(h_age-2):
        dog_age = dog_age + 4

if h_age == 1:
    dog_age = 10.5

print(f'Dog ageis: {dog_age}')