"""
memento
сохранение состояние персонажа Player в игре

хар-ки
level
health
experience
gold

во время игры
повысить уровень
(получить или) потерять здоровье
получить опыт
получить или потерять деньги

user может сохранять и откратываться

Player - Originator
level
health
experience
gold

level_up()
take_damage(amount)
gain_experience(point)
add_gold(amount)
spend_gold(amount)
save_state() - возвращает объект Memento
restore_state(memento) - восстанавливает состояние из объекта Memento

PlayerMemento - Memento
хранит снимок состояния игрока
не дает изменять состояние игрока

Caretaker
управляет созданием и восстановлением снимков состояния игрока
save(player)
undo(player)
(redo(player))
"""
from copy import deepcopy


class PlayerMemento:
    def __init__(self, dict):
        self._dict = deepcopy(dict)

    def get_state(self):
        return self._dict


class Player:
    def __init__(self):
        self._level = 1
        self._health = 100
        self._experience = 0
        self._gold = 0

    def level_up(self):
        self._level += 1

    def take_damage(self, amount: int):
        self._health -= max(0, amount)

    def heal(self, amount: int):
        self._health += min(100, self._health + amount)

    def gain_experience(self, points: int):
        self._experience += points

    def add_gold(self, amount: int):
        self._gold += amount

    def spend_gold(self, amount: int):
        self._gold -= amount

    def save_state(self):
        return PlayerMemento(self.__dict__)

    def restore_state(self, memento: PlayerMemento):
        self.__dict__ = deepcopy(memento.get_state())

    def __str__(self):
        return "---------------------------" \
               f"\nУровень: {self._level}\n" \
               f"Здоровье: {self._health}\n" \
               f"Опыт: {self._experience}\n" \
               f"Золото: {self._gold}\n"


class Caretaker:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, player):
        self._undo_stack.append(player.save_state())
        self._redo_stack.clear()

    def undo(self, player):
        if not self._undo_stack:
            print('нечего отменять')
            return None

        self._redo_stack.append(player.save_state())
        last_state = self._undo_stack.pop()
        player.restore_state(last_state)

    def redo(self, player):
        if not self._redo_stack:
            print('нечего повторять')
            return None

        self._undo_stack.append(player.save_state())
        next_state = self._redo_stack.pop()
        player.restore_state(next_state)


player = Player()
caretaker = Caretaker()


caretaker.save(player)
print('до изменения', player)

player.level_up()
player.level_up()
player.add_gold(100)
player.gain_experience(50)

print(player)

caretaker.undo(player)
print('после undo', player)

caretaker.redo(player)
print('после redo', player)
