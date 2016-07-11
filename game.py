from datetime import datetime, timedelta

from basic.board import Board

from basic.player import Player, OffensiveAI, RandomAI


def declare_winner(board, player):
    if board.has_won():
        print('Player {} wins!'.format(player))
        return player

    else:
        print('This game sucked...')
        return None


def valid_move(board, move):
    return move in range(0, board.size()) and board.pos(move) == board.EMPTY


def start():
    players = [RandomAI('x'), OffensiveAI('o')]
    board = Board(size=3)
    winner = None
    while True:
        board.print_board()
        print('Available Moves: ', board.moves_remaining())
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
            print('Not a valid move')

    board.print_board()
    return declare_winner(board, winner)

i = 100
RESULTS = {'playerX': 0, 'playerO': 0, 'cats': 0}
START_TIME = datetime.now()

for _ in range(i):
    player_won = start()

    print('PLAYER WON: ', player_won)
    if player_won is None:
        RESULTS['cats'] += 1
    elif player_won.token == 'x':
        RESULTS['playerX'] += 1
    elif player_won.token == 'o':
        RESULTS['playerO'] += 1


END_TIME = datetime.now()
DIFF_TIME = timedelta.total_seconds(END_TIME - START_TIME)
print('\nIt took {} seconds to run the game {} times\n'.format(DIFF_TIME, i))
print(RESULTS)