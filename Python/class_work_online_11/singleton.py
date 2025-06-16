"""
Система настроек приложения
class AppSettings:
    dict настройки
    set_param
    get_param
    get_instance - для получения экземпляра класса

settings1
settings2
указывают на один и тот же экземпляр класса - при создании через get_instance
"""


class AppSettings:
    _instance = None

    def __init__(self):
        self.dict = {
            'display': '1920x1080',
        }

    def set_param(self, key, value):
        self.dict[key] = value
        return f'Параметр {key} со значением {value} добавлен'

    def get_param(self, key):
        return self.dict[key]

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            return cls._instance
        else:
            return cls._instance

    def get_all(self):
        return self.dict

    @classmethod
    def dell_all(cls):
        cls._instance = None


settings1 = AppSettings.get_instance()
settings2 = AppSettings.get_instance()

print(id(settings1), id(settings2))

print(settings1.set_param('volume', 10))
print(settings1.get_param('display'))
print(settings2.get_param('volume'))

print(settings1.dict)
print(settings2.dict)

AppSettings.dell_all()
settings3 = AppSettings.get_instance()
print(settings3.get_all())

settings4 = AppSettings()
print(id(settings4))
print(settings4.get_all())
