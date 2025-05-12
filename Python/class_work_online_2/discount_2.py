"""
правильный вариант(просто вынести прайс)

"""

# def discount(summ, person, price):
#     if person in price:
#         sale = price[person]
#     else:
#         return 'Неизвестный тип клиента!'
#     return f'Итоговая сумма с учетом скидки: {summ - (summ * sale)}'


# order = float(input('Укажите сумму заказа: '))
# type = input('Укажите тип клиента: ')
# price = {
#         'обычный': 0.05,
#         'постоянный': 0.1,
#         'VIP': 0.2,
#         }
# print(discount(order, type, price))

"""
неправильный вариант(скаорее всего)

"""
# def discount(person, price):
#     if person in price:
#         return f'Итоговая сумма с учетом скидки: {price[person]}'
#     else:
#         return 'Неизвестный тип клиента!'


# order = float(input('Укажите сумму заказа: '))
# type = input('Укажите тип клиента: ')
# price = {
#         'обычный': order - (order * 0.05),
#         'постоянный': order - (order * 0.1),
#         'VIP': order - (order * 0.2)
#         }

# print(discount(order, type, price))

"""
неправильный вариант(прайс в функции)

"""

# def discount(summ, person):
#     price = {
#             'обычный': 0.05,
#             'постоянный': 0.1,
#             'VIP': 0.2,
#             }
#     if person in price:
#         sale = price[person]
#     else:
#         return 'Неизвестный тип клиента!'
#     return f'Итоговая сумма с учетом скидки: {summ - (summ * sale)}'


# order = float(input('Укажите сумму заказа: '))
# type = input('Укажите тип клиента: ')

# print(discount(order, type))

"""
непроверенный вариант без функции

"""

order = float(input('Укажите сумму заказа: '))
types = input('Укажите тип клиента: ')
price = {
        'обычный': order - (order * 0.05),
        'постоянный': order - (order * 0.1),
        'VIP': order - (order * 0.2)
        }

print(f'Итоговая сумма с учетом скидки: {price[types]}'
      if types in price else 'Неизвестный тип клиента!')
