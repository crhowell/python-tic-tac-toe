import random


class Player:

    def __init__(self, token):
        self.token = token

    def other_player(self):
        return 'x' if self.token == 'x' else 'o'

    def move(self, board):
        return int(input('{} > '.format(self.token))) - 1

    def __str__(self):
        return '{}'.format(self.token.upper())


class RandomAI(Player):

    def move(self, board):
        return random.choice(board.moves_remaining()) - 1


class OffensiveAI(Player):

    def move(self, board):
        return (self.winning_move(board) or self.blocking_move(board) or
                random.choice(board.moves_remaining()) - 1)

    def winning_move(self, board):
        foo = [state for state in board.WIN_STATES if self.near_win(state, board, self.token)]

        if not foo:
            return False
        else:
            return foo[0][board.line(foo[0]).index(board.EMPTY)]

    def blocking_move(self, board):
        foo = [state for state in board.WIN_STATES if self.near_win(state, board, self.other_player())]

        if not foo:
            return False
        else:
            return foo[0][board.line(foo[0]).index(board.EMPTY)]

    def near_win(self, state, board, token):
        return board.line(state).count(token) == 2 and board.EMPTY in board.line(state)
