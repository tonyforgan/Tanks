__author__ = 'tonyforgan'

from sensor import Sensor
from datetime import datetime
import time


class MockSensor(Sensor):
    def _monitor(self):
        while True:
            second = datetime.now().second
            if second % 5 == 0:
                self._triggered = not self._triggered
                self.onstatechanged(self._triggered)
                time.sleep(1)

    def __init__(self, triggered):
        self._triggered = triggered

    def triggered(self):
        return self._triggered