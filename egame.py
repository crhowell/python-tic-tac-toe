from datetime import datetime, timedelta
from evolved.board import Board
from evolved.player import Player, RandomAI


def start_game(board, players):
    while not board.game_over:
        if not board.moves_left() > 0:
            break

        board.print_board()
        player = players[0]
        move = player.move(board)
        winner = None
        if board.valid_move(move):
            board = board.place_token(move, player.token)
            board.remove_move(move)
            if board.has_won(player):
                winner = player
                break
            players.append(players.pop(0))
        else:
            print('Not a valid move, try again...')

    board.print_board()
    print('Winner is Player {}', winner)
    return winner


RESULTS = {'playerX': 0, 'playerO': 0, 'cats': 0}
START_TIME = datetime.now()

for _ in range(1000):
    board = Board()
    players = [RandomAI('x'), RandomAI('o')]
    winner = start_game(board, players)
    if winner is None:
        RESULTS['cats'] += 1
    else:
        if winner.token is 'x':
            RESULTS['playerX'] += 1

        if winner.token is 'o':
            RESULTS['playerO'] += 1


END_TIME = datetime.now()
DIFF_TIME = timedelta.total_seconds(END_TIME - START_TIME)
print('\nIt took {} seconds to run the game {} times\n'.format(DIFF_TIME, 1))
print(RESULTS)



