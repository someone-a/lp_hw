def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
    except ValueError:
        print("Нужно вводить числа")
        return
    
    if max_discount > 99:
        print('Слишком большая максимальная скидка')
        return
    
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)
        