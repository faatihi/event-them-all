from lib.Component import Component
from lib.Console import console

from Tile import Tile

class Board (Component):
    def __init__ (self, name = 'board'):
        super().__init__(name)

        self.dimension = [3, 3]
        tiles_ids = range(self.dimension[0] * self.dimension[1])
        self.tiles = list(map(lambda tile_id: Tile(tile_id + 1), tiles_ids))

        self.listeners.append({ 'event': 'board.render', 'callback': self.onRender })
    
    def onRender (self, data):
        self.render()

    def render (self):
        for tile in self.tiles:
            self.send('tile.render')
            if tile.id % self.dimension[0] == 0:
                console.print('\n')

    # def render (self):
    #     for tile in self.tiles:
    #         tile.render()
    #         if tile.id % self.dimension[0] == 0:
    #             console.print('\n')
