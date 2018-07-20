import numpy as np


class Game(object):

    def __init__(self, n, config,cost = 0):
        array = np.array(config)
        self.board = array.reshape((n, n))
        blank = np.where(self.board == 0)
        self.blanky = int(blank[0])
        self.blankx = int(blank[1])
        self.n = n
        self.cost = cost

    def move_up(self):
        if self.blanky - 1 < 0:
            return None
        ay, ax = self.blanky, self.blankx
        by, bx = self.blanky - 1, self.blankx
        self.board[ay, ax], self.board[by, bx] = self.board[by, bx], self.board[ay, ax]
        self.blanky = self.blanky - 1
        self.cost += 1

    def move_down(self):
        if self.blanky + 1 > n:
            return None
        ay, ax = self.blanky, self.blankx
        by, bx = self.blanky + 1, self.blankx
        self.board[ay, ax], self.board[by, bx] = self.board[by, bx], self.board[ay, ax]
        self.blanky = self.blanky + 1
        self.cost += 1

    def move_left(self):
        if self.blankx - 1 < 0:
            return None
        ay, ax = self.blanky, self.blankx
        by, bx = self.blanky, self.blankx - 1
        self.board[ay, ax], self.board[by, bx] = self.board[by, bx], self.board[ay, ax]
        self.blankx = self.blankx - 1
        self.cost += 1

    def move_right(self):
        if self.blankx - 1 < 0:
            return None
        ay, ax = self.blanky, self.blankx
        by, bx = self.blanky, self.blankx + 1
        self.board[ay, ax], self.board[by, bx] = self.board[by, bx], self.board[ay, ax]
        self.blankx = self.blankx + 1
        self.cost += 1

    def visualise(self):
        return(self.board)

    def return_blank(self):
        return(self.blanky, self.blankx)


n = 3
config = sorted([1, 2, 5, 3, 4, 0, 6, 7, 8])
print(config)
Game = Game(n, config)
print(Game.visualise())
