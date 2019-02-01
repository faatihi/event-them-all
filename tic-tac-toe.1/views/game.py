from functools import reduce
from views import console
import operator

def parse_int(s, base=10, val=None):
 if s.isdigit():
  return int(s, base)
 else:
  return val

class Game:
    def start (self, playersNames):
        self.players = list(map(lambda playerName: Player(playerName, ''), playersNames))
        self.players[0].token = 'O'
        self.players[1].token = 'X'
        self.positions = list(map(lambda number: Position(number), [1, 2, 3, 4, 5, 6, 7, 8, 9]))
        
        self.playTurn = -1
        self.player = None

        while True:
            self.render()

            pos = self.getNextPlay()

            self.player.numbers.append(pos)

            position = list(filter(lambda position: position.value == pos, self.positions))[0]
            position.token = self.player.token

            if self.hasPlayerWon():
                print(f'\n\n{self.player.name}, CONGRATULATIONS! YOU WON!!')
                break

    def render (self):
        self.playTurn += 1
        self.player = self.players[self.playTurn % 2]

        console.clear()

        print("ULTIMATE TIC TAC TOE")

        print(f'\n{self.players[0].name}: {self.players[0].token}\t\t\t{self.players[1].name}: {self.players[1].token}')

        print('\n' + reduce((lambda x, y: x + ' ' + y), map(lambda position: str(position.token or position.value), self.positions)))

    def getNextPlay (self):
        position = 0
        playedPositions = reduce(lambda x, y: x + y, map(lambda p: p.numbers, self.players))
        maxPosition = max(map(lambda p: p.value, self.positions))
        
        while not position:
            positionStr = input(f'\n{self.player.name}, your turn: ')        
            position = parse_int(positionStr)

            if not position:
                position = 0
            elif position < 1:
                position = 0
            elif position > maxPosition:
                position = 0
            elif position in playedPositions:
                position = 0

        return position

    def hasPlayerWon (self):
        nums = list(sorted(self.player.numbers))       
        diffs = list(map(operator.sub, nums[1:], nums[:-1]))
        diff = set(diffs)
        
        return len(nums) == 3 and len(diff) == 1



class Player:
    def __init__ (self, name, token):
        self.name = name
        self.token = token
        self.numbers = []
        self.score = 0

class Position:
    def __init__ (self, value):
        self.value = value
        self.token = ''
