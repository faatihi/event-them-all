from Component import Component

class Application (Component):
    def __init__ (self, name):
        super().__init__(name)

        self.listeners = [
            { 'event': 'started', 'callback': self.onAttached },
            { 'event': 'attached', 'callback': self.onAttached },
            { 'event': 'stopped', 'callback': self.onStopped },
        ]

    def onAttached (self, data):
        self.send('needColorSelection')

    def onStopped (self, data):
        pass

    def onColorChanged (self, data):
        pass
