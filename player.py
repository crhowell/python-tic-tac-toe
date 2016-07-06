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

