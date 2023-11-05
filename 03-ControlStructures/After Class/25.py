hmany = int(input('Number of products purchased: '))
price = float(input('Product price: '))
sum = 2*price
for i in range(hmany-2):
    sum += (price*0.75)

print(f'Amount to pay: {sum}')
    