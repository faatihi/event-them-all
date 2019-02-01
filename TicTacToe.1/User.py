from lib.Component import Component

class User (Component):
    def __init__ (self, name = 'user'):
        super().__init__(name)

        self.listeners.append({ 'event': 'request-start', 'callback': self.onRequestStart })

    def onRequestStart (self, data):
        self.send('game-start')