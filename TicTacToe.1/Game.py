from lib.Component import Component
from lib.Console import console

from functools import reduce

class Game (Component):
    def __init__ (self, name = 'game'):
        super().__init__(name)

        self.listeners.append({ 'event': 'players-ready', 'callback': self.onPlayersReady })

    def onPlayersReady (self, data):
        self.players = data

        self.render()
        self.send('game-started')

    def render (self):
        console.clear()

        print("ULTIMATE TIC TAC TOE")

        print(f'\n{self.players[0].name}: {self.players[0].token}\t\t\t{self.players[1].name}: {self.players[1].token}')

        self.send('need-draw-of-board')

        # print('\n' + reduce((lambda x, y: x + ' ' + y), map(lambda position: str(position.token or position.value), self.positions)))