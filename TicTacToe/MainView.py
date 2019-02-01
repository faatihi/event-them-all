from lib.Component import Component
from lib.Console import console

class MainView (Component):
    def __init__ (self, name = 'main_view'):
        super().__init__(name)

        self.listeners.append({ 'event': 'started', 'callback': self.onStarted })
        self.listeners.append({ 'event': 'request-start', 'callback': self.onRequestStart })
        self.listeners.append({ 'event': 'game-stopped', 'callback': self.onStarted })

    def onStarted (self, data):
        print('Welcome to\n\n\nTIC-TAC-TOE\n\n\n')

    def onRequestStart (self, data):
        console.readkey('Pess ENTER to start')
        self.send('game-start')
