__author__ = 'tonyforgan'

from tank import Tank
from mockpump import MockPump
from mocksensor import MockSensor


class MockTank:
    def __init__(self):
        self._upper = MockSensor(False)
        self._lower = MockSensor(False)

        self._tank = Tank(self._upper, self._lower)
        self._pump = MockPump()

    def run(self):
        self._pump.empty(self._tank)

        print(self._tank.isempty)