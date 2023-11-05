c_price = float(input('Current product price: '))
p_price = float(input('Previous product price: '))

if c_price/p_price*100 < 90 :
    print(f'Buy the product!! \n Product price reduced by {100 - (c_price/p_price*100)}%')