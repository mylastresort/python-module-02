import time
from random import randint
import os
from datetime import datetime


def log(func):
    def inner(self, *args, **kwargs):
        start = datetime.now()
        ret = func(self, *args, **kwargs)
        duration = datetime.now() - start
        seconds, microseconds = duration.seconds, duration.microseconds
        duration = '%.3f ms' % (
            microseconds / 1000) if not seconds else '%.3f s' % seconds
        action = ' '.join([w.capitalize() for w in func.__name__.split('_')])
        self.log_machine.write('({})Running: {:20} [ exec-time = {} ]\n'.format(
            os.environ.get('USER'), action, duration))
        self.log_machine.flush()
        return ret
    return inner


class CoffeeMachine():
    def __init__(self) -> None:
        self.water_level = 100
        self.log_machine = open('machine.log', 'w')

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
