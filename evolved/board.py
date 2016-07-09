

class Board:
    EMPTY = ' '

    def __init__(self, board=None, **kwargs):
        self.WIN_CONDITIONS = []
        self.players = ['x', 'o'] if 'players' not in kwargs else kwargs['players']
        self.board_size = 3 if 'size' not in kwargs else kwargs['size']
        self.cells = board if board is not None else self.build_a_board(self.board_size)
        self.fill_win_states(self.board_size)
        self.WIN_STATES_LEFT = self.WIN_CONDITIONS

    def build_a_board(self, size):
        """
            Creates an empty board of (size)

            :param size: size of the board
            :return: list() of size with EMPTY values
        """
        return [self.EMPTY for i in range(size * size)]

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
