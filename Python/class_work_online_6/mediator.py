
"""
mediator
умный дом

умный будильник
умная кофеварка
умные шторы
аудиосистема
освещение

при срабатывании будильника:
открыть шторы
завести кофеварку
включить свет
включить музыку

центральный посредник mediator - управляет всеми устройствами

интерфейс SmartDevice:
класс HomeMediator - посредник

классы устройств:
AlarmClock
CoffeeMachine
Curtains
Lights
AudioSystem

AlarmClock.trigger() -> включает свет, открывает шторы, включает
кофеварку и музыку
"""
from abc import ABC, abstractmethod
from typing import Any


class Mediator:
    @abstractmethod
    def notify(self, sender: Any, event: str) -> None:
        pass


class SmartDevice(ABC):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        # видимо сохраняет переданный HomeMediator() для каждого обьекта


class HomeMediator(Mediator):
    # основной класс, который запускает события
    def __init__(self):
        self.alarm_clock = None
        self.coffee_machine = None
        self.curtains = None
        self.lights = None
        self.audio_system = None

    def notify(self, sender: Any, event: str) -> None:
        if isinstance(sender, AlarmClock) and event == "up":
            print("[Mediator]: Событие 'сработал будильник'")
            self.curtains.open()
            self.lights.turn_on()
            self.coffee_machine.brew()
            self.audio_system.play_music()


class AlarmClock(SmartDevice):
    def trigger(self):
        print("[AlarmClock]: Будильник сработал!")
        self.mediator.notify(self, "up")


class CoffeeMachine(SmartDevice):
    def brew(self):
        print("[CoffeeMachine]: Кофе готовится!")


class Curtains(SmartDevice):
    def open(self):
        print("[Curtains]: Шторы открываются!")


class Lights(SmartDevice):
    def turn_on(self):
        print("[Lights]: Свет включается!")


class AudioSystem(SmartDevice):
    def play_music(self):
        print("[AudioSystem]: Музыка проигрывается!")


mediator = HomeMediator()

alarm = AlarmClock(mediator)
coffee = CoffeeMachine(mediator)
curtains = Curtains(mediator)
lights = Lights(mediator)
audio = AudioSystem(mediator)

mediator.alarm_clock = alarm
mediator.coffee_machine = coffee
mediator.curtains = curtains
mediator.lights = lights
mediator.audio_system = audio

alarm.trigger()
