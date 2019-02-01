from lib.Component import Component

class Main (Component):
    def __init__ (self, name = 'main'):
        super().__init__(name)

        self.listeners.append({ 'event': 'started', 'callback': self.onStarted })
        self.listeners.append({ 'event': 'game-stopped', 'callback': self.onStarted })

    def onStarted (self, data):
        self.send('request-start')
