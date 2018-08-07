from BaseAI_3 import BaseAI
from Grid_3 import Grid
import numpy as np
import time
import helper as helper

def maximize(grid, depth, start, first_move, alpha, beta):
    if grid.canMove() == False or time.clock() - start > 0.2 or depth == 0:
        return (grid , helper.score(grid), first_move)

    best_max = (None, -np.inf)
    moves = grid.getAvailableMoves()
    for move in moves:
        if depth == 4:
            first_move = move
        child = helper.get_max_child(move, grid)
        max_tuple = minimize(child, depth - 1, start, first_move, alpha, beta)
        if max_tuple[1] > best_max[1]:
            best_max = max_tuple
        if max_tuple[1] >= beta:
            break
        if max_tuple[1] > alpha:
            alpha = max_tuple[1]
    return best_max

def minimize(grid, depth, start, first_move, alpha, beta):
    if grid.canMove() == False or time.clock() - start > 0.2 or depth == 0:
        return (grid ,helper.score(grid), first_move)

    best_min = (None, np.inf)
    free_cells = grid.getAvailableCells()
    for value in [2,4]:
        for pos in free_cells:
            child = helper.get_min_child(pos, value, grid)
            min_tuple = maximize(child, depth - 1, start, first_move, alpha, beta)
            if min_tuple[1] < best_min[1]:
                best_min = min_tuple
            if min_tuple[1] < beta:
                beta = min_tuple[1]
            if min_tuple[1] <= alpha:
                break
    return best_min