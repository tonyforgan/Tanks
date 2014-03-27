__author__ = 'tforgan'


class Event:
    def __init__(self):
        self._handlers = set()

    def handle(self, handler):
        self._handlers.add(handler)
        return self

    def unhandle(self, handler):
        try:
            self._handlers.remove(handler)
        except:
            raise ValueError("Handler is not handling this event, so cannot unhandle it.")
        return self

    def fire(self, *args, **kargs):
        for handler in self._handlers:
            handler(*args, **kargs)

    def getHandlerCount(self):
        return len(self._handlers)

    __iadd__ = handle
    __isub__ = unhandle
    __call__ = fire
    __len__ = getHandlerCount