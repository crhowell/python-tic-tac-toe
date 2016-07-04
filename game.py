from board import Board
from player import Player


def declare_winner(board, player):
    if board.has_won():
        print('Player #{} wins!'.format(player))
    else:
        print('This game sucked...')


def valid_move(board, move):
    return move in range(0, board.size()) and board.pos(move) == board.EMPTY


def start():
    players = [Player('x'), Player('o')]
    board = Board()
    winner = None
    while True:
        board.print_board()
        player = players[0]
        move = player.move(board)
        if valid_move(board, move):
            board = board.place_token(move, player.token)
            if board.game_over():
                winner = player
                break
            players.append(players.pop(0))
        else:
            print('Not a valid move')

    declare_winner(board, winner)
    board.print_board()

start()
