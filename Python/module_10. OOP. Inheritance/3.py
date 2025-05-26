class Money:
    def __init__(self, money):
        self.money = money
        self.whole = int(self.money)
        self.fractional = round((self.money - self.whole), 4)

    def info(self):
        print(f'У вас {self.whole} рублей и {self.fractional} копеек.')

    def change(self):
        answer = input('Вы хотите внести изменения?\n'
                       '1-Рубли\n2-Копейки\n3-Не менять\n'
                       '(Укажите цифру для продолжения): ')

        if answer == '1':
            self.whole = int(input('Укажите рубли целым числом: '))
        elif answer == '2':
            fractional = float(input('Укажите копейки: '))
            self.fractional = fractional / 10**(
                (len(str(fractional)))-2) if fractional >= 1 else fractional
        self.info()


rubles = Money(12.11)
rubles.info()
rubles.change()
