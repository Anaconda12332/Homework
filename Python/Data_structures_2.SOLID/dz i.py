# class Bird:
#     def fly(self):
#         print("летит")

# class Sparrow(Bird): # Sparrow - воробей
#     pass

# class Ostrich(Bird): # Ostrich - страус
#     pass


# birds = [Sparrow(), Ostrich()]
# for bird in birds:
#     bird.fly()

"""
что будет, если у класса Bird вызвать метод fly(), а потмо подставить
туда Ostrich()?
-будет ошибка в логике, тк сраус не может летать
Как повлияет добавление новых типов птиц на текущую реализацию?
-все птицы будут летать
почему страус не должен наследоваться от класса Bird, если Bird требует
умения летать?
-потому что страус не летает
как избежать подобных нарушений в будущем?
-разбивать общие классы на более конкретизированные и исключать использование
лишних методов

"""


class flying_birds:
    def action(self, name):
        print(name, "летит")


class swimming_birds:
    def action(self, name):
        print(name, "плывет")


class swimm_and_fly:
    def action(self, name):
        print(name, "летит и плывет")


class Sparrow(flying_birds):
    # Sparrow - воробей
    pass


class Ostrich(swimming_birds):
    # Ostrich - страус
    pass


class Seagulls(swimm_and_fly):
    # чайки
    pass


birds = [Sparrow(), Ostrich(), Seagulls()]
for i in birds:
    i.action(i.__class__.__name__)
