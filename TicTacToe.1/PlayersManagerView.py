from lib.Component import Component
from lib.Console import console

from Player import Player

class PlayersManagerView (Component):
    def __init__ (self, name = 'players_manager_view'):
        super().__init__(name)

        self.listeners.append({ 'event': 'game-start', 'callback': self.onGameStart })

    def onGameStart (self, data):
        playersNames = self.getPlayers()

        players = list(map(lambda playerName: Player(playerName, ''), playersNames))
        players[0].token = 'O'
        players[1].token = 'X'

        self.send('players-ready', players)

    def getPlayers (self):
        console.clear()

        players = [ '', '' ]

        players[0] = input('Name of Player 1: ') or 'Player 1'
        players[1] = input('Name of Player 2: ') or 'Player 2'

        return players
