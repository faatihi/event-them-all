from Component import Component

class ColorPicker (Component):
    def __init__ (self, name):
        super().__init__(name)

        self.colors = ['red', 'yellow', 'green']
        self.color = -1

        self.listeners = [
            { 'event': 'needColorSelection', 'callback': self.onNeedColorSelection },
        ]

    def onNeedColorSelection (self, data):
        self.color = (self.color + 1) % len(self.colors)
        self.send('needColorChange', self.colors[self.color])
