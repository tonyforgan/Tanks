__author__ = 'tonyforgan'

from abc import ABCMeta, abstractmethod
from event import Event
import threading


class Sensor(object):
    __metaclass__ = ABCMeta

    onstatechanged = Event()

    def __init__(self):
        pass

    @abstractmethod
    def _monitor(self):
        pass

    def activate(self):
        _thread = threading.Thread(target=self._monitor)
        _thread.daemon = True
        _thread.start()