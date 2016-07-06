from board import Board
from player import Player, RandomAI, OffensiveAI
from datetime import datetime, timedelta

def declare_winner(board, player):
    if board.has_won():
        print('Player {} wins!'.format(player))
    else:
        print('This game sucked...')


def valid_move(board, move):
    return move in range(0, board.size()) and board.pos(move) == board.EMPTY


def start():
    players = [RandomAI('x'), OffensiveAI('o')]
    board = Board()

    winner = None
    while True:
        #board.print_board()
        #print('Available Moves: ', board.moves_remaining())
        player = players[0]
        move = player.move(board)
        if valid_move(board, move):
            board = board.place_token(move, player.token)
            if board.game_over():
                winner = player
                break
            players.append(players.pop(0))
        else:
            pass
            #print('Not a valid move')

    #board.print_board()
    declare_winner(board, winner)
    return winner

i = 10001
RESULTS = {'playerX': 0, 'playerO': 0, 'cats': 0}
START_TIME = datetime.now()

for i in range(i):
    player_won = start()
    if player_won.token == 'x':
        RESULTS['playerX'] += 1
    elif player_won.token == 'o':
        RESULTS['playerO'] += 1
    else:
        RESULTS['cats'] += 1

END_TIME = datetime.now()
DIFF_TIME = timedelta.total_seconds(END_TIME - START_TIME)
print('\nIt took {} seconds to run the game {} times\n'.format(DIFF_TIME, i))
print(RESULTS)



