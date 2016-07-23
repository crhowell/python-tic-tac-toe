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
        win_conds = board.win_conditions()
        to_win = [state for state in win_conds if self.near_win(state, board, token)]
        to_block = [state for state in win_conds if self.near_win(state, board, self.next_player(board))]

        if not to_win:
            if not to_block:
                return False
            else:
                return to_block[0][board.line(to_block[0]).index(board.EMPTY)]
        else:
            return to_win[0][board.line(to_win[0]).index(board.EMPTY)]

    def near_win(self, state, board, token):
        return board.line(state).count(token) == board.line_length() - 1 and board.EMPTY in board.line(state)


class EvolvedAI(OffensiveAI):
    
    def __init__(self, token, **kwargs):
        OffensiveAI.__init__(self, token)
        self.win_states = None
        self.corners = []
        self.pattern_choice = []

    def move(self, board):
        if self.win_states is None:
            self.win_states = board.win_conditions()
            self.set_corners(board.line_size())

        best = self.best_move(board, self.token)
        return best if best else self.from_pattern(board)

    def from_pattern(self, board):
        if board.moves_made() <= board.line_size():
            if self.corners:
                self.pattern_choice = self.corners
                self.corners = []
            else:
                self.pick_pattern(board)
        
        if not self.pattern_choice or self.pattern_choice is None:
            self.pick_pattern(board)

        choice = random.choice(self.pattern_choice)
        moves_left = board.moves_left()

        if choice not in moves_left:
            self.pattern_choice.remove(choice)
            self.from_pattern(board)
        return choice

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

    def set_corners(self, d):
        edges = []
        if self.win_states:
            edges.append(self.win_states[0][0])
            edges.append(self.win_states[d-1][d-1])
            edges.append(self.win_states[0][d-1])
            edges.append(self.win_states[d-1][0])
            #self.win_states[0]
            #self.win_states[d]
            self.corners.extend(edges)
