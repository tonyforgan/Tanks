__author__ = 'tonyforgan'

from abc import ABCMeta, abstractproperty


class Sensor(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def triggered(self):
        pass