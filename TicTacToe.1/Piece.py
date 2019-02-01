from lib.Console import console

class Board:
    def __init__ (self):
        pass
    
    def render (self):
        console.clear()

        print('\n' + reduce((lambda x, y: x + ' ' + y), map(lambda position: str(position.token or position.value), self.positions)))