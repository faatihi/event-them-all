import time
import os
import msvcrt
import sys

class Console:
    def clear (self):
        os.system('cls')

    def sleep (self, ms):
        time.sleep(ms)

    def readkey (self, str = ''):
        print(str)
        msvcrt.getch()

    def print (self, str):
        sys.stdout.write(str)
        # sys.stdout.flush()

    def printLine (self, str):
        print(f'{str} \n')

console = Console()
