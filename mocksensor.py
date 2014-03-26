__author__ = 'tonyforgan'

from sensor import Sensor
from datetime import datetime


class MockSensor(Sensor):
    def _monitor(self):
        while True:
            second = datetime.now().second
            if second % 5 == 0:
                self.onstatechanged(second)

    def __init__(self, triggered):
        self._triggered = triggered

    def triggered(self):
        return self._triggered