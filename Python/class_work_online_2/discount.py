def discount(summ, person):
    if person == 'обычный':
        sale = 0.05
    elif person == "постоянный":
        sale = 0.1
    elif person == 'VIP':
        sale = 0.2
    else:
        return 'Неизвестный тип клиента!'
    return f'Итоговая сумма с учетом скидки: {summ - (summ * sale)}'


price = float(input('Укажите сумму заказа: '))
type = input('Укажите тип клиента: ')

print(discount(price, type))
