__author__ = 'tonyforgan'

from tank import Tank
from mockpump import MockPump
from mocksensor import MockSensor


class MockTank:
    def __init__(self):
        self._upper = MockSensor(False)
        #self._lower = MockSensor(False)
        self._upper.onstatechanged += statechanged

        #self._tank = Tank(self._upper, self._lower)
        #self._pump = MockPump()

    def run(self):
        self._upper.activate()
        raw_input("Press enter to end")

    def statechanged(self, currentstate):
        print "Seconds = %d." % currentstate