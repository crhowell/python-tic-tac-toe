from _core.recipes import grouper


class Board:
    EMPTY = ' '

    def __init__(self, players, **kwargs):
        self.WIN_CONDITIONS = []
        self.total_moves = 0 if 'total_moves' not in kwargs else kwargs['total_moves']
        self.players = players
        self.dimension = 3 if 'dimension' not in kwargs else kwargs['dimension']
        self.board = (self.build_a_board(self.dimension)
                      if 'board' not in kwargs else kwargs['board'])
        self.game_over = False
        self.fill_win_states(self.dimension)
        self.WIN_STATES_LEFT = self.WIN_CONDITIONS
        self.AVAILABLE_MOVES = (self.init_moves() if 'moves' not in kwargs
                                else kwargs['moves'])
        self.current_player = self.players[0]

    def place_token(self, cell, token):
        new_board = list(self.board)
        new_board[cell - 1] = token
        self.total_moves += 1
        return Board(self.players, board=new_board, moves=self.AVAILABLE_MOVES,
                     dimension=self.dimension, total_moves=self.total_moves)

    def remove_move(self, move):
        if move in self.AVAILABLE_MOVES:
            self.AVAILABLE_MOVES.remove(move)

    def has_won(self):
        if self.total_moves >= 3:
            self.game_over = any(self.line(state) in [
                self.win_case(self.current_player.token)
            ] for state in self.WIN_STATES_LEFT)

        return self.game_over

    def print_board(self):
        print('\n', '-' * 20, '\n')
        for item in list(grouper(self.board, self.dimension)):
            print(*item, sep=' | ')
        print('\n', '-' * 20, '\n')

    def current_move(self):
        return self.players[0]

    def win_case(self, token):
        return token * self.dimension

    def line_size(self):
        return self.dimension

    def moves_left(self):
        return self.AVAILABLE_MOVES

    def valid_move(self, move):
        moves_left = self.moves_left()
        if not moves_left:
            self.game_over = False

        return (False if move not in moves_left else
                self.cell(move) == self.EMPTY)

    def cell(self, move):
        return self.board[move-1]

    def pos(self, move):
        return self.board.index(move-1)

    def moves_made(self):
        return self.total_moves

    def win_conditions(self):
        return self.WIN_CONDITIONS

    def get_players(self):
        return self.players

    def switch_players(self):
        self.players.append(self.players.pop(0))

    def size(self):
        return len(self.board)

    def line_length(self):
        return self.dimension

    def line(self, moves):
        return ''.join(self.cell(move) for move in moves)

    def init_moves(self):
        return [move + 1 for move in range(self.size())]

    def fill_win_states(self, num):
        """
            Creates indexed game board,
            uses it to build the different win states.

            :param num: size of the board
            :return: None
        """
        cells = [i + 1 for i in range(num * num)]
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
        rtl = [cells[num - 1] + (x * cells[num - 2]) for x in range(0, num)]
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
            :return: A new EMPTY board
        """
        return [self.EMPTY for i in range(size * size)]
