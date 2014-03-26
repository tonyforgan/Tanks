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

#class MockFileWatcher:
#    def __init__(self):
#        self.fileChanged = Event()
#
#   def watchFiles(self):
#        source_path = "foo"
#        self.fileChanged(source_path)
#
#def log_file_change(source_path):
#    print "%r changed." % (source_path,)
#
#def log_file_change2(source_path):
#    print "%r changed!" % (source_path,)
#
#watcher              = MockFileWatcher()
#watcher.fileChanged += log_file_change2
#watcher.fileChanged += log_file_change
#watcher.fileChanged -= log_file_change2
#watcher.watchFiles()
