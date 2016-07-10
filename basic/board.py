from _core.recipes import grouper

class Board:
    EMPTY = ' '

    def __init__(self, cells=None, **kwargs):
        self.DYN_WIN_STATES = []
        self.board_size = 3 if 'size' not in kwargs else kwargs['size']
        self.cells = cells if cells is not None else self.build_a_board(self.board_size)
        self.fill_win_states(self.board_size)

    def build_a_board(self, size):
        """
            Creates an empty board of (size)

            :param size: size of the board
            :return: list() of size with EMPTY values
        """
        return [self.EMPTY for i in range(size*size)]

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
            appends them to the DYN_WIN_STATES list.

            :param cells: the current cells on board
            :param num: size of the board
            :return: None
        """
        ltr = [cells[0] + (x * (num+1)) for x in range(0, num)]
        rtl = [cells[num-1] + (x * cells[num-1]) for x in range(0, num)]
        self.DYN_WIN_STATES.extend([ltr])
        self.DYN_WIN_STATES.extend([rtl])

    def build_horizontal_states(self, cells, num):
        """
            Builds a list of all HORIZONTAL win states,
            appends them to the DYN_WIN_STATES list.

            :param cells: the current cells on board
            :param num: size of the board
            :return: None
        """
        for i in range(0, len(cells), num):
            self.DYN_WIN_STATES.extend([cells[i:i+num]])

    def build_vertical_states(self, cells, num):
        """
            Builds a list of all VERTICAL win states,
            appends them to the DYN_WIN_STATES list.

            :param cells: the current cells on board
            :param num: size of the board
            :return: None
        """
        for i in range(num):
            self.DYN_WIN_STATES.extend([cells[i::num]])

    def win_states(self):
        """
            Get a list of all the win states

            :return: list of all win states
        """
        return self.DYN_WIN_STATES

    def place_token(self, cell, token):
        new_cells = list(self.cells)
        new_cells[cell] = token
        return Board(new_cells, size=self.board_size)

    def moves_remaining(self):
        return [move + 1 for move in range(0, self.size()) if self.pos(move) is self.EMPTY]

    def line(self, indexes):
        return ''.join([self.cells[i] for i in indexes])

    def print_board(self):
        print('\n-----------\n')
        for item in list(grouper(self.cells, self.board_size)):
            print(*item, sep=' | ')
        print('\n------------\n')

    def get_board_size(self):
        return self.board_size

    def size(self):
        return len(self.cells)

    def has_won(self):
        return any(self.line(state) in ['x'*self.board_size, 'o'*self.board_size] for state in self.DYN_WIN_STATES)

    def cats_game(self):
        return all(cell is not self.EMPTY for cell in self.cells)

    def game_over(self):
        return self.has_won() or self.cats_game()

    def pos(self, index):
        return self.cells[index]

    def __str__(self):
        return '{}'.format(self.cells)
