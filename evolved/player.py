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
        return random.choice(board.AVAILABLE_MOVES)


class EvolvedAI(Player):

    def __init__(self, token):
        Player.__init__(self, token)
        self.win_states = None
        self.pattern_choice = []

    def pick_pattern(self, board):
        if self.win_states is None:
            self.win_states = board.win_conditions()

        if self.win_states:
            self.pattern_choice = self.win_states.pop()
        else:
            self.pattern_choice = [board.AVAILABLE_MOVES[0]]

    def move(self, board):
        best = None
        if board.moves_made() >= 3:
            best = self.blocking_move(board)

        if not best:
            best = self.best_move(board)

        return best

    def next_player(self, board):
        return str(board.players[1])

    def near_win(self, state, board, token):
        return board.line(state).count(token) == board.line_length() - 1 and board.EMPTY in board.line(state)

    def check_line(self, line, empty=None):
        return [not (cell == self.token or cell == empty) for cell in line]

    def blocked_me(self, board):
        line = board.line(self.pattern_choice)
        check = self.check_line(line, board.EMPTY)
        return any(check)

    def best_move(self, board):

        best = self.choice(board)
        print('pattern', self.pattern_choice)
        print('chose best move of: ', best)
        if board.valid_move(best):
            if self.blocked_me(board):
                print('Blocked.. ')
                self.pattern_choice = None
                best = self.choice(board)
            else:
                print('not blocked')
                if len(board.AVAILABLE_MOVES) <= 2:
                    best = board.AVAILABLE_MOVES[0]
        else:
            best = self.choice(board)


        return best

    def choice(self, board):
        if not self.pattern_choice or self.pattern_choice is None:
            self.pick_pattern(board)

        choice = random.choice(self.pattern_choice)
        self.pattern_choice.remove(choice)
        if choice not in board.AVAILABLE_MOVES:
            self.choice(board)
        return choice

    def blocking_move(self, board):
        to_block = [state for state in self.win_states if self.near_win(state, board, self.next_player(board))]
        if not to_block:
            return None
        else:
            return to_block[0][board.line(to_block[0]).index(board.EMPTY)]
