from .EventQueue import EventQueue

class Component:
    def __init__ (self, name):
        self.name = name
        self.parent = None
        
        self.components = 0
        self._listeners = []
        self.listeners = []
        self.eventQueue = EventQueue(self.eventQueueCallback)

        self.listeners.append({ 'event': 'started', 'callback': self._onStarted })
        self.listeners.append({ 'event': 'stopped', 'callback': self._onStopped })

    def _onStarted (self, data):
        self.dispatch('started', data)

    def _onStopped (self, data):
        self.dispatch('stopped', data)

    def start (self):
        self.dispatch('started')

    def stop (self):
        self.dispatch('stopped')
        # self.eventQueue.stop()

    def attach (self, component):
        for listener in component.listeners:
            self.listen(listener)

        component.parent = self
        self.components += 1

        self.dispatch_old('attached', self, component.listeners)
        
        return component

    def send (self, event, data = None):
        self.parent.dispatch(event, data)

    def dispatch (self, event, data = None):
        self.eventQueue.add({ 'event': event, 'data': data })

    def eventQueueCallback (self, event, data):
        listeners = list(filter(lambda x: x['event'] == event, self._listeners))
        
        canProceed = True
        for listener in list(filter(lambda x: x['mode'] == 'intercept', listeners)):
            canProceed = listener['callback'](data)
            if (canProceed == False):
                break

        if (canProceed):
            for listener in list(filter(lambda x: x['mode'] != 'intercept', listeners)):
                listener['callback'](data)

    def dispatch_old (self, event, data = None, listeners = None):
        listeners = listeners or self._listeners

        listeners = list(filter(lambda x: x['event'] == event, listeners))
        
        for listener in listeners:
            listener['callback'](data)

    def listen (self, listener):
        if ('mode' in listener):
            pass
        else:
            listener['mode'] = ''

        self._listeners.append(listener)

    # def forward (self, event, new_event = None):
    #     self.listeners.append({ 'event': event, 'callback': lambda data: self.dispatch(new_event or event, data) })

    # def backward (self, event, new_event = None):
    #     self.listeners.append({ 'event': event, 'callback': lambda data: self.dispatch(new_event or event, data) })
