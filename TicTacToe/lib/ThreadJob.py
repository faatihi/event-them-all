import threading

class ThreadJob(threading.Thread):
    def __init__(self, callback, interval):
        '''runs the callback function after interval seconds

        :param callback:  callback function to invoke
        :param event: external event for controlling the update operation
        :param interval: time in seconds after which are required to fire the callback
        :type callback: function
        :type interval: int
        '''
        self.callback = callback
        self.event = threading.Event()
        self.interval = interval
        super(ThreadJob, self).__init__()

    def run (self):
        while not self.event.wait(self.interval):
            self.callback()


# event = 

# def foo():
#     print("hello")

# k = ThreadJob(foo,event, 0.5)
# k.start()

# print("It is non-blocking")
