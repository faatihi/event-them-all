from ThreadJob import ThreadJob

class EventQueue:
    def __init__ (self, callback):
        self.queue = []
        self.callback = callback
        self.inCallbacks = 0

        ThreadJob(self.setIntervalCallback, 0.1).start()

    def add (self, event):
        self.queue.append(event)

    def start (self):
        pass
    
    def setIntervalCallback (self):
        if self.inCallbacks == 0:
            self.dequeue()

    def dequeue (self):
        if len(self.queue):
            event = self.queue.pop(0)
            # print(f'event {event} popped')
            self.inCallbacks += 1
            self.callback(event['event'], event['data'])
            self.inCallbacks -= 1

    def loop_ (self):
        while len(self.queue) and self.queue[0] != 'stop':
            event = self.queue.pop(0)
            # print(f'event {event} popped')
            self.callback(event['event'], event['data'])
