__author__ = 'tonyforgan'

from abc import ABCMeta, abstractmethod
from event import Event
import threading


class Sensor(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.onstatechanged = Event()

    @abstractmethod
    def _monitor(self):
        pass

    def activate(self):
        _thread = threading.Thread(target=self._monitor, args=self)
        _thread.daemon = True
        _thread.start()