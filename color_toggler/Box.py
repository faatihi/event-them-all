from Component import Component

class Box (Component):
    def __init__ (self, name):
        super().__init__(name)

        self.listeners = [
            { 'event': 'needColorChange', 'callback': self.onChangeColor }
        ]

    def onChangeColor (self, data):
        print(f'{self.name}: color changed to {data}')
        self.send('colorChanged', data)
