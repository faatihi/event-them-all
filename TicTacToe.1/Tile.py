from lib.Console import console

class Tile:
    def __init__ (self, id, name = None):
        self.id = id
        self.name = name or str(id)
    
    def render (self):
        console.print(f' {self.name} ')
