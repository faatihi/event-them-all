from lib.Component import Component
from lib.Adapter import Adapter
from User import User
from Main import Main
from MainView import MainView
from Game import Game
from PlayersManager import PlayersManager
from Board import Board

sys = Component('sys')
sys.attach(Main())
sys.attach(User())
game = sys.attach(Adapter(['game-start'], ['game-stopped']))

game.attach(Game())
game.attach(PlayersManager())
game.attach(Board())

sys.start()
