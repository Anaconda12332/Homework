salary =float(input('Укажите вашу зарплату: '))
credit =float(input('Укажите сумму платежа по кредиту: '))
utilities =float(input('Укажите задолжность по коммунальным платежам: '))

result= salary - (credit + utilities)
print(f"Сумма, оставшаяся после всех выплтат, равна: {round(result, 1)}")