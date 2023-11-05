
def phone_keyboard():
    for i in range(1, 10):
        print(f'{i} ', end="")
        if i%3 == 0:
            print()
            
phone_keyboard()