import random


class Player:

    def __init__(self, token):
        self.token = token

    def other_player(self, turn):
        return 'o' if turn == 'x' else 'x'

    def move(self, board):
        return int(input('{} > '.format(self.token))) - 1

    def __str__(self):
        return '{}'.format(self.token.upper())


class RandomAI(Player):

    def move(self, board):
        return random.choice(board.moves_remaining()) - 1


class OffensiveAI(Player):

    def move(self, board):
        best = self.best_move(board, self.token)
        return best if best else random.choice(board.moves_remaining()) - 1

    def best_move(self, board, token):
        to_win = [state for state in board.win_states() if self.near_win(state, board, token)]
        to_block = [state for state in board.win_states() if self.near_win(state, board, self.other_player(token))]
        print('toblock: ', to_block)

        if not to_win:
            if not to_block:
                return False
            else:
                return to_block[0][board.line(to_block[0]).index(board.EMPTY)]
        else:
            return to_win[0][board.line(to_win[0]).index(board.EMPTY)]

    def near_win(self, state, board, token):
        return board.line(state).count(token) == board.get_board_size()-1 and board.EMPTY in board.line(state)
