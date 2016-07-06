from board import Board
from player import Player, RandomAI


def declare_winner(board, player):
    if board.has_won():
        print('Player {} wins!'.format(player))
    else:
        print('This game sucked...')


def valid_move(board, move):
    return move in range(0, board.size()) and board.pos(move) == board.EMPTY


def start():
    players = [RandomAI('x'), RandomAI('o')]
    board = Board()
    winner = None
    while True:
        board.print_board()
        print('Moves Left: ', board.moves_remaining())
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

    board.print_board()
    declare_winner(board, winner)

start()
