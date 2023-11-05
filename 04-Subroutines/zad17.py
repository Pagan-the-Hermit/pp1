x1 = int(input("Enter the first number: "))
x2 = int(input("Enter the second number: "))
x3 = int(input("Enter the third number: "))

def difference(n1,n2,n3):
    if n1 != n2 and n3 != n1 and n3 != n2:
        return True

if difference(x1, x2, x3) == True:
    print(f'Numbers {x1}, {x2}, and {x3} are different')
else:
    print(f'Numbers {x1}, {x2}, and {x3} are not different')