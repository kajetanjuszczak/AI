from random import randint
from BaseAI_3 import BaseAI
from Grid_3 import Grid
import numpy as np
import time
import minimax as minimax
import helper as helper
import alphabeta as ab

class PlayerAI(BaseAI):

    def getMove(self, grid):
        decision = ab.maximize(grid, 4, time.clock() , None, -np.inf, np.inf)
        return decision[2]

if __name__ == '__main__':
    g = Grid()
    player = PlayerAI()
    g.map[0][0] = 2
    g.map[1][0] = 128
    g.map[3][0] = 512

    for b in range(3):
        for i in g.map:
           print(i)

        print(g.getAvailableMoves())

        v = player.getMove(g)

        g.move(v)
