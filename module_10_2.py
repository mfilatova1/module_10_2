from threading import Thread
from time import sleep
from random import randint


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name} на нас напали!')
        enemies_count = 100
        day = 0
        while enemies_count > 0:
            enemies_count -= self.power
            day += 1
            print(f'{self.name} сражается {day}..., осталось {enemies_count} воинов.')
            sleep(randint(1, 3))
            if enemies_count < self.power:
                enemies_count = 0
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')