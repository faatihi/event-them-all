from lib.Component import Component

class Intercepter (Component):
    def __init__ (self, event, callback, name = 'intercepter'):
        super().__init__(name)

        self.listeners.append({ 'event': event, 'callback': self.callback, 'mode': 'intercept' })
        self._callback = callback

    def callback (self, data):
        return self._callback(self, data)
