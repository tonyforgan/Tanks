__author__ = 'tonyforgan'

from pump import Pump


class MockPump(Pump):
    def __init__(self):
        self._activated = False

    def activate(self):
        if self._activated:
            pass
        self._activated = True

    def deactivate(self):
        self._activated = False