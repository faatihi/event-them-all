from lib.Component import Component
from lib.Utils import literal

from Player import Player

class PlayersManagerView (Component):
    def __init__ (self, name = 'players_manager_view'):
        super().__init__(name)

        self.listeners.append({ 'event': 'request-player-name', 'callback': self.onRequestPlayerName })

    def onRequestPlayerName (self, player):
        name = input(f"Name of Player {player.id}: ") or ('Player ' + str(player.id))

        self.send('player-name-acquired', literal(id = player.id, name = name))
