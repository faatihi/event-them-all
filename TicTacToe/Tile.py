from lib.Component import Component
from lib.Console import console

class Tile (Component):
    def __init__ (self, id, name = None):
        super().__init__(name)

        self.id = id
        self.name = name or str(id)

        self.listeners.append({ 'event': 'tile.render', 'callback': self.onRender })
    
    def onRender (self, data):
        if (data.id != self.id):
            return

        self.render()

    def render (self):
        console.print(f'{self.name}')
