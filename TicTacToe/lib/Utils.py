from collections import namedtuple
import time

def literal (**kw):
    return namedtuple('literal', kw)(**kw)

def sleep (ms):
    time.sleep(ms)
