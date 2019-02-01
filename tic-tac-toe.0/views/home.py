from views import console

def getPlayers ():
    console.clear()

    print('THE ULTIMATE\nTIC TAC TOE\n\n')

    players = [ '', '' ]

    players[0] = input('Name of Player 1: ') or 'Player 1'
    players[1] = input('Name of Player 2: ') or 'Player 2'

    return players
