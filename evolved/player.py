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

class OffensiveAI(Player):

    def __init__(self, token, **kwargs):
        Player.__init__(self, token)

    def next_player(self, board):
        player_list = board.get_players()
        if player_list:
            idx = player_list.index(board.current_move()) + 1
            size = len(player_list)
            if idx == size:
                return player_list[size - idx].token
            else:
                return player_list[idx].token
        else:
            return None

    def move(self, board):
        best = self.best_move(board, self.token)
        return best if best else random.choice(board.moves_left())

    def best_move(self, board, token):
        to_win = [state for state in board.win_conditions() if self.near_win(state, board, token)]
        to_block = [state for state in board.win_conditions() if self.near_win(state, board, self.next_player(board))]

        if not to_win:
            if not to_block:
                return False
            else:
                return to_block[0][board.line(to_block[0]).index(board.EMPTY)]
        else:
            return to_win[0][board.line(to_win[0]).index(board.EMPTY)]

    def near_win(self, state, board, token):
        return board.line(state).count(token) == board.line_length() - 1 and board.EMPTY in board.line(state)


class EvolvedAI(Player):

    def __init__(self, token, **kwargs):
        Player.__init__(self, token)
        self.win_states = None
        self.pattern_choice = []

    def pick_pattern(self, board):
        if self.win_states is None:
            self.win_states = board.win_conditions()

        if self.win_states:
            if len(self.win_states) > 2:
                self.pattern_choice = self.get_dual_pattern()
            else:
                self.pattern_choice = self.win_states.pop()
        else:
            self.pattern_choice = [board.AVAILABLE_MOVES[0]]

    def get_dual_pattern(self):
        p1 = []
        p2 = []
        idx = random.choice(range(len(self.win_states)))
        p1 = self.win_states[idx]
        self.win_states.pop(idx)
        for key, choice in enumerate(self.win_states):
            if p1[0] in choice:
                p2 = choice
                self.win_states.pop(key)
                break
        print('P1: {} and P2: {}'.format(p1, p2))
        dual = []
        dual.extend(p1)
        dual.extend(p2)
        return dual


    def move(self, board):
        best = None
        if board.moves_made() >= board.line_length():
            best = self.blocking_move(board)

        if not best:
            best = self.best_move(board)

        return best

    def next_player(self, board):
        player_list = board.get_players()
        if player_list:
            idx = player_list.index(board.current_move()) + 1
            size = len(player_list)
            if idx == size:
                return player_list[size - idx].token
            else:
                return player_list[idx].token
        else:
            return None

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
        if board.valid_move(best):
            if self.blocked_me(board):
                self.pattern_choice = None
                best = self.choice(board)
            else:
                if len(board.AVAILABLE_MOVES) <= 2:
                    best = board.AVAILABLE_MOVES[0]
        else:
            best = self.choice(board)

        return best

    def choice(self, board):
        if not self.pattern_choice or self.pattern_choice is None:
            self.pick_pattern(board)

        print('PATT: ', self.pattern_choice)
        index = random.choice(range(len(self.pattern_choice)))
        print('index: ', index)
        choice = self.pattern_choice[index]
        print('choice: ', choice)
        self.pattern_choice.pop(index)
        print('movesLeft: ', board.moves_left())
        if choice not in board.moves_left():
            self.choice(board)
        return choice

    def blocking_move(self, board):
        to_block = [state for state in self.win_states if self.near_win(state, board, self.next_player(board))]
        if not to_block:
            return None
        else:
            return to_block[0][board.line(to_block[0]).index(board.EMPTY)]
