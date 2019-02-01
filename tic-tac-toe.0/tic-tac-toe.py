from views import home
from views.game import Game

players = home.getPlayers()

Game().start(players)
