import random


class Player:

    def __init__(self, token):
        self.token = token

    def my_turn(self, turn):
        return turn == self.token

    def move(self, board):
        return int(input('{} > '.format(self.token)))

    def __str__(self):
        return '{}'.format(self.token.upper())


class RandomAI(Player):

    def move(self, board):
        print(board.AVAILABLE_MOVES)
        return random.choice(board.AVAILABLE_MOVES)
