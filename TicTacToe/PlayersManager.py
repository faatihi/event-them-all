from lib.Component import Component
from lib.Utils import literal

from Player import Player

class PlayersManager (Component):
    def __init__ (self, name = 'players_manager'):
        super().__init__(name)

        self.listeners.append({ 'event': 'game-start', 'callback': self.onGameStart })
        self.listeners.append({ 'event': 'player-name-acquired', 'callback': self.onPlayerNameAcquired })
        self.listeners.append({ 'event': 'players-names-acquired', 'callback': self.onPlayersNamesAcquired })

        self.playersNames = []

    def onGameStart (self, data):
        self.playersNames.clear()

        self.send('request-player-name', literal(id = 1))
        self.send('request-player-name', literal(id = 2))

    def onPlayerNameAcquired (self, player):
        self.playersNames.append(player.name)

        if (len(self.playersNames) == 2):
            self.send('players-names-acquired')

    def onPlayersNamesAcquired (self, data):
        players = list(map(lambda playerName: Player(playerName, ''), self.playersNames))
        players[0].token = 'O'
        players[1].token = 'X'

        self.send('players-ready', players)
