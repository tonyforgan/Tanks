__author__ = 'tonyforgan'

from pump import Pump


class MockPump(Pump):
    def __init__(self):
        self._activated = False

    def activate(self):
        if self._activated:
            print('activated')
        self._activated = True

    def deactivate(self):
        print('deactivated')
        self._activated = False