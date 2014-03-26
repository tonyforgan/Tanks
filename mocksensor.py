__author__ = 'tonyforgan'

from sensor import Sensor


class MockSensor(Sensor):
    def __init__(self, triggered):
        self._triggered = triggered

    def triggered(self):
        return self._triggered