from datetime import datetime, timedelta
from evolved.board import Board
from evolved.player import (Player,
    RandomAI,EvolvedAI, OffensiveAI)


def start_game(board):
    while not board.game_over:
        if not len(board.moves_left()) > 0:
            break

        board.print_board()
        player = board.current_move()
        move = player.move(board)
        winner = None
        if board.valid_move(move):
            board = board.place_token(move, player.token)
            board.remove_move(move)
            if board.has_won():
                winner = player
                break
            board.switch_players()
        else:
            print('Not a valid move, try again...')

    board.print_board()
    print('Winner is Player {}', winner)
    return winner


RESULTS = {'X': 0, 'O': 0, 'cats': 0}
START_TIME = datetime.now()

i = 1
for _ in range(i):
    players = [Player('x'), EvolvedAI('o')]
    board = Board(players, dimension=3)
    winner = start_game(board)
    if winner is None:
        RESULTS['cats'] += 1
    else:
        if winner.token is 'x':
            RESULTS['X'] += 1

        if winner.token is 'o':
            RESULTS['O'] += 1


END_TIME = datetime.now()
DIFF_TIME = timedelta.total_seconds(END_TIME - START_TIME)
print('\nIt took {} seconds to run the game {} times\n'.format(DIFF_TIME, i))
print(RESULTS)



