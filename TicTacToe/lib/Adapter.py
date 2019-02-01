from lib.Component import Component

class Adapter (Component):
    def __init__ (self, input_events, output_events = [], name = 'adapter'):
        super().__init__(name)

        self.output_events = output_events

        for e in input_events:
            self.listeners.append({ 'event': e, 'callback': lambda data: self.onUpEvent(e, data) })

    def onUpEvent (self, event, data):
        super().dispatch(event, data)

    def dispatch (self, event, data = None):
        if event in self.output_events:
            self.send(event, data)
        else:
            super().dispatch(event, data)
