from random import randint
from BaseAI_3 import BaseAI
from Grid_3 import Grid
import numpy as np
import time
class PlayerAI(BaseAI):

    def getMove(self, grid):
        decision = self.maximize(grid, depth = 3, first_move = None)
        #print(time.clock())
        return decision[2]

    def maximize(self, grid, depth, first_move):
        if grid.canMove() == False or depth==0:
            return (grid ,self.score(grid), first_move)

        best_max = (None, -np.inf)
        moves = grid.getAvailableMoves()
        for move in moves:
            if depth == 3:
                first_move = move
            child = self.get_max_child(move, grid)
            max_tuple = self.minimize(child, depth -1, first_move)
            if max_tuple[1] > best_max[1]:
                best_max = max_tuple
        return best_max

    def minimize(self, grid, depth, first_move):
        if grid.canMove() == False or depth==0:
            return (grid ,self.score(grid), first_move)

        best_min = (None, np.inf)
        free_cells = grid.getAvailableCells()
        for value in [2,4]:
            for pos in free_cells:
                child = self.get_min_child(pos, value, grid)
                min_tuple = self.maximize(child, depth -1, first_move)
                if min_tuple[1] < best_min[1]:
                    best_min = min_tuple
        return best_min



    def get_max_child(self, move, grid):
        eval_grid = grid.clone()
        eval_grid.move(move)
        return eval_grid
    
    def get_min_child(self, pos, value, grid):
        eval_grid = grid.clone()
        eval_grid.insertTile(pos, value)
        return eval_grid

    def score(self, grid):
        return len(grid.getAvailableCells())


if __name__ == '__main__':
    g = Grid()
    player = PlayerAI()
    g.map[0][0] = 2
    g.map[1][0] = 2
    g.map[3][0] = 4

    while True:
        for i in g.map:
            print(i)

        print(g.getAvailableMoves())

        v = player.getMove(g)

        g.move(v)
        