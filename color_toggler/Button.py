from Component import Component

class Button (Component):
    def __init__ (self, name):
        super().__init__(name)

        self.listeners = [
            { 'event': 'colorChanged', 'callback': self.onColorChanged },
        ]

    def onColorChanged (self, data):
        input('Change color?')
        self.send('needColorSelection')
