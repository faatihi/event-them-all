from lib.Component import Component
from lib.Console import console
from lib.Utils import literal

class Board (Component):
    def __init__ (self, dimension, name = 'board'):
        super().__init__(name)

        self.dimension = dimension

        self.listeners.append({ 'event': 'board.render', 'callback': self.onRender })
        # self.listeners.append({ 'event': 'board.print', 'callback': lambda data: console.print(data.text) })
    
    def onRender (self, data):
        self.render()

    def render (self):
        matrix = [
            [' ', '|', '|'],
            ['--', ' ', ' '],
            ['---', '     ', '  .  '],
            ['\n', '\n', '\n'],
        ]

        tile_id = 0

        for y in [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0]:
            for x in [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 3]:
                val = matrix[x][y]

                if (val.find('.') >= 0):
                    tile_id += 1
                    self.send('console.print', literal(text = val.split('.')[0]))
                    self.send('tile.render', literal(id = tile_id))
                    self.send('console.print', literal(text = val.split('.')[1]))
                else:
                    self.send('console.print', literal(text = val))
