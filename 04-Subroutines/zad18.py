def numbers(n):
    x = ''
    for i in range(1, n+1):
        x += str(i) +' '
    return x

print(f'Numbers <1,7> {numbers(15)}')
print(f'Numbers <1,7> {numbers(7)}')