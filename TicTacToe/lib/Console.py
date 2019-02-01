import os
import msvcrt
import sys

class Console:
    def clear (self):
        os.system('cls')

    def readkey (self, str = ''):
        print(str)
        msvcrt.getch()

    def print (self, str):
        # if (str == 'eof'):
        #     self.flush()

        # print(str, end='')
        sys.stdout.write(str)

        if (str != ''):
            sys.stdout.flush()

    def printLine (self, str):
        print(f'{str} \n')

    def flush (self):
        sys.stdout.flush()

console = Console()
