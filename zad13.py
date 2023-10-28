print('podaj dłogośc krawędzi')
size = int(input())

def pole(l):
    pole = 6 * (l**2)
    return pole

print(f'Pole powierzchni całkowitej sześcianu wynosi: {pole(size)}')