from lib.Utils import literal
from lib.Console import console

from lib.Component import Component
from lib.Adapter import Adapter
from lib.Intercepter import Intercepter
from User import User
from Main import Main
#from MainView import MainView
from Game import Game
from PlayersManager import PlayersManager
#from PlayersManagerView import PlayersManagerView
from Board import Board
from Tile import Tile

user = User()
component_console = Intercepter('console.print', lambda self, data: console.print(data.text) != 'yes', 'console')

sys = Component('sys')

sys.attach(user)
sys.attach(Main())
game = sys.attach(Adapter(['game-start'], ['game-stopped']))

game.attach(user)
game.attach(Game())
game.attach(PlayersManager())
#game.attach(PlayersManagerView())
board = game.attach(Adapter(['board.render']))

board.attach(component_console)
board_dimension = [3, 3]
board.attach(Board(board_dimension))
for tile_id in range(board_dimension[0] * board_dimension[1]):
    board.attach(Tile(tile_id + 1))
board.attach(Intercepter('tile.render', lambda self, data: data.id - 5 or console.print('X') == 'yes'))

sys.start()
