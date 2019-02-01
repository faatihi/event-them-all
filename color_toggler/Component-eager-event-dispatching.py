class Component:
    def __init__ (self, name):
        self.name = name
        self.parent = None
        
        self.components = 0
        self._listeners = []

        self.listeners = []
        self.listeners.append({ 'event': 'started', 'callback': self.onStarted })
        self.listeners.append({ 'event': 'stopped', 'callback': self.onStopped })

    def onStarted (self, data):
        self.dispatch('started', data)

    def onStopped (self, data):
        self.dispatch('stopped', data)

    def start (self):
        self.dispatch('started')

    def stop (self):
        self.dispatch('stopped')

    def attach (self, component):
        for listener in component.listeners:
            self.listen(listener)

        component.parent = self
        self.dispatch('attached', self, component.listeners)

        self.components += 1

        return component

    def send (self, event, data = None, listeners = None):
        self.parent.dispatch(event, data, listeners)

    def dispatch (self, event, data = None, listeners = None):
        listeners = listeners or self._listeners

        listeners = list(filter(lambda x: x['event'] == event, listeners))
        
        for listener in listeners:
            listener['callback'](data)


    def listen (self, listener):
        self._listeners.append(listener)
