from lib.Component import Component
from lib.Utils import literal

class User (Component):
    def __init__ (self, name = 'user'):
        super().__init__(name)

        self.listeners.append({ 'event': 'request-start', 'callback': self.onRequestStart })
        self.listeners.append({ 'event': 'request-player-name', 'callback': self.onRequestPlayerName })

    def onRequestStart (self, data):
        self.send('game-start')

    def onRequestPlayerName (self, player):
        #name = 'Player ' + str(player.id)
        name = 'Gwen' if player.id == 1 else 'Stacy'

        self.send('player-name-acquired', literal(id = player.id, name = name))
