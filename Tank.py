__author__ = 'tonyforgan'


class Tank:
    def __init__(self, upperSensor, lowerSensor):
        self._upperSensor = upperSensor
        self._lowerSensor = lowerSensor

    @property
    def isfull(self):
        return self._upperSensor.triggered()

    @property
    def isempty(self):
        return not self._lowerSensor.triggered()