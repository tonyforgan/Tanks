__author__ = 'tonyforgan'

from abc import ABCMeta, abstractmethod


class Pump(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def empty(self, tank):
        while not tank.isempty:
            self.activate()
        self.deactivate()

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass