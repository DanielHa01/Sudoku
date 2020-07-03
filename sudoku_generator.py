from sudoku_solver import *
import random
import pdb

#Create an empty sudoku
def make_empty_grid():
    grid = [[0 for x in range(9)] for y in range(9)]
    for i in range(9):
        for j in range(9):
            grid[i][j] = 0
    return grid

#Empty a given sudoku
def empty_grid(arr):
    for i in range(9):
        for j in range(9):
            grid[i][j] = 0
    return grid

#Remove a certain amount of space randomly inside the sudoku
def remove(grid, num_remove):
    for i in range(num_remove):
        row = random.randrange(9)
        col = random.randrange(9)
        grid[row][col] = 0
    return grid

#Make a sudoku
def make_sudoku(grid):

    for i in range(40):
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        if check_valid_location(grid, row, col, num):
            grid[row][col] = num

    if not solve_sudoku(grid):
        empty_grid(grid)
        make_sudoku(grid)
    
    remove(grid, 50)
    return grid
    
    
            
if __name__ == "__main__":
    grid = make_empty_grid()
    print('ready to make sudoku')
    make_sudoku(grid)
    print_grid(grid)
    print('finish')