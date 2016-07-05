from recipes import grouper


class Board:
    EMPTY = ' '
    WIN_STATES = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    def __init__(self, cells=None):
        self.cells = cells if cells is not None else [self.EMPTY for i in range(9)]

    def place_token(self, cell, token):
        new_cells = list(self.cells)
        new_cells[cell] = token
        return Board(new_cells)

    def print_moves_remaining(self):
        moves = [move + 1 for move in range(0, self.size()) if self.pos(move) is self.EMPTY]
        print('Moves Left: ', moves)

    def line(self, indexes):
        return ''.join(map(lambda i: self.cells[i], indexes))

    def print_board(self):
        print('\n-----------\n')
        for item in list(grouper(self.cells, 3)):
            print(*item, sep=' | ')
        print('\n------------\n')

    def size(self):
        return len(self.cells)

    def has_won(self):
        return any(map(lambda v: (self.line(v) in ['xxx', 'ooo']), self.WIN_STATES))

    def cats_game(self):
        return all(cell is not self.EMPTY for cell in self.cells)

    def game_over(self):
        return self.has_won() or self.cats_game()

    def pos(self, index):
        return self.cells[index]

    def __str__(self):
        return '{}'.format(self.cells)
