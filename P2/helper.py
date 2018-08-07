from Grid_3 import Grid
import time
import math

def get_max_child(move, grid):
    eval_grid = grid.clone()
    eval_grid.move(move)
    return eval_grid

def get_min_child(pos, value, grid):
    eval_grid = grid.clone()
    eval_grid.insertTile(pos, value)
    return eval_grid

def score(grid):
    return available_cells(grid) + 2*max_tile(grid) + 2*max_in_corner(grid) + 0.1*lines_priority(grid)

def available_cells(grid):
    return len(grid.getAvailableCells())

def max_tile(grid):
    tile = grid.getMaxTile()
    return math.log2(tile)

def max_in_corner(grid):
    corners = [(0,0)]
    tile = grid.getMaxTile()
    for i in range(grid.size):
        for j in range(grid.size):
            if grid.map[i][j] == tile:
                if (i,j) in corners:
                    return math.log2(tile)
                else:
                    return 0

def lines_priority(grid):
    bonus = 0
    for i in range(grid.size):
        if grid.map[i][0] >= grid.map[i][1] and grid.map[i][0] >= grid.map[i][2] and grid.map[i][0] >= grid.map[i][3]:
            try:
                bonus += math.log2(grid.map[i][0])
            except ValueError:
                bonus += 0
        if grid.map[i][0] >= grid.map[i][1] and grid.map[i][0] >= grid.map[i][2]:
            try:
                bonus += math.log2(grid.map[i][0])
            except ValueError:
                bonus += 0
        if grid.map[i][0] >= grid.map[i][1]:
            try:
                bonus += math.log2(grid.map[i][0])
            except ValueError:
                bonus += 0
        if grid.map[i][1] >= grid.map[i][2] and grid.map[i][1] >= grid.map[i][3]:
            try:
                bonus += math.log2(grid.map[i][1])
            except ValueError:
                bonus += 0
        if grid.map[i][2] >= grid.map[i][3]:
            try:
                bonus += math.log2(grid.map[i][2])
            except ValueError:
                bonus += 0
    for j in range(grid.size):
        if grid.map[0][j] >= grid.map[1][j] and grid.map[0][j] >= grid.map[2][j] and grid.map[0][j] >= grid.map[3][j]:
            try:
                bonus += math.log2(grid.map[0][j])
            except ValueError:
                bonus += 0
        if grid.map[0][j] >= grid.map[1][j] and grid.map[0][j] >= grid.map[2][j]:
            try:
                bonus += math.log2(grid.map[0][j])
            except ValueError:
                bonus += 0
        if grid.map[0][j] >= grid.map[1][j]:
            try:
                bonus += math.log2(grid.map[0][j])
            except ValueError:
                bonus += 0
        if grid.map[1][j] >= grid.map[2][j] and grid.map[1][j] >= grid.map[3][j]:
            try:
                bonus += math.log2(grid.map[1][j])
            except ValueError:
                bonus += 0
        if grid.map[2][j] >= grid.map[3][j]:
            try:
                bonus += math.log2(grid.map[2][j])
            except ValueError:
                bonus += 0
    return bonus
