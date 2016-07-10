from _core.recipes import grouper


class Board:
    EMPTY = ' '

    def __init__(self, board=None, moves=None, **kwargs):
        self.WIN_CONDITIONS = []
        self.total_moves = 0 if 'total_moves' not in kwargs else kwargs['total_moves']
        self.players = ['x', 'o'] if 'players' not in kwargs else kwargs['players']
        self.board_size = 3 if 'size' not in kwargs else kwargs['size']
        self.board = board if board is not None else self.build_a_board(self.board_size)
        self.fill_win_states(self.board_size)
        self.WIN_STATES_LEFT = self.WIN_CONDITIONS
        self.AVAILABLE_MOVES = moves if moves is not None else self.initial_avail_moves()
        self.game_over = False

    def place_token(self, cell, token):
        new_board = list(self.board)
        new_board[cell-1] = token
        self.total_moves += 1
        return Board(new_board, self.AVAILABLE_MOVES,
                     size=self.board_size, total_moves=self.total_moves)

    def remove_move(self, move):
        self.AVAILABLE_MOVES.remove(move)

    def moves_left(self):
        return len(self.AVAILABLE_MOVES)

    def valid_move(self, move):
        return move in self.AVAILABLE_MOVES and self.pos(move) == self.EMPTY

    def pos(self, move):
        return self.board[move-1]

    def size(self):
        return len(self.board)

    def line(self, indexes):
        return ''.join([self.board[i] for i in indexes])

    def has_won(self, player):
        if self.total_moves >= 3:
            self.game_over = any(self.line(state) in [
                self.win_case(player.token)
            ] for state in self.WIN_STATES_LEFT)

        print('has_won: ', self.game_over)
        return self.game_over

    def win_case(self, token):
        print('token: {}'.format(token*self.board_size))
        return token * self.board_size

    def initial_avail_moves(self):
        return [move+1 for move in range(self.size())]

    def print_board(self):
        print('\n', '-'*20, '\n')
        for item in list(grouper(self.board, self.board_size)):
            print(*item, sep=' | ')
        print('\n', '-' *20, '\n')

    def fill_win_states(self, num):
        """
            Creates indexed game board,
            uses it to build the different win states.

            :param num: size of the board
            :return: None
        """
        cells = [i for i in range(num * num)]
        self.build_horizontal_states(cells, num)
        self.build_vertical_states(cells, num)
        self.build_diag_states(cells, num)

    def build_diag_states(self, cells, num):
        """
            Builds a list of the DIAGONAL win states,
            appends them to the WIN_CONDITIONS list.

            :param cells: the current cells on board
            :param num: size of the board
            :return: None
        """
        ltr = [cells[0] + (x * (num + 1)) for x in range(0, num)]
        rtl = [cells[num - 1] + (x * cells[num - 1]) for x in range(0, num)]
        self.WIN_CONDITIONS.extend([ltr])
        self.WIN_CONDITIONS.extend([rtl])

    def build_horizontal_states(self, cells, num):
        """
            Builds a list of all HORIZONTAL win states,
            appends them to the WIN_CONDITIONS list.

            :param cells: the current cells on board
            :param num: size of the board
            :return: None
        """
        for i in range(0, len(cells), num):
            self.WIN_CONDITIONS.extend([cells[i:i + num]])

    def build_vertical_states(self, cells, num):
        """
            Builds a list of all VERTICAL win states,
            appends them to the WIN_CONDITIONS list.

            :param cells: the current cells on board
            :param num: size of the board
            :return: None
        """
        for i in range(num):
            self.WIN_CONDITIONS.extend([cells[i::num]])

    def build_a_board(self, size):
        """
            Creates an empty board of (size)

            :param size: size of the board
            :return: list() of size with EMPTY values
        """
        return [self.EMPTY for i in range(size * size)]
