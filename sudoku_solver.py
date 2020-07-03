#Print out sudoku
def print_grid(arr):
    for i in range(9):
         for j in range(9):
            print(arr[i][j], end = ' ')
         print('')

#Find any empty space in the sudoku 
def find_valid_space(arr, l):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False

#Check if num has been used in a specific row
def check_row(arr, row, num):
    for j in range(9):
        if(arr[row][j] == num):
            return True
    return False

#Check if num has been used in a specific column
def check_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

#Check if num has been used in a specific 3x3 box
def check_box(arr, row, col, num):
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if arr[i][j] == num and i != row and j != col:
                return True

    return False

#Check if num #Check if num has been used in a specific row, column or 3x3 box
def check_valid_location(arr, row, col, num):
    return not check_row(arr, row, num) and not check_col(arr, col, num) and not check_box(arr, row, col, num)

#Solve the sudoku
def solve_sudoku(arr):
    l = [0,0]
    
    if(not(find_valid_space(arr, l))):
        return True

    row = l[0]
    col = l[1]

    for num in range(1,10):
        if check_valid_location(arr, row, col, num):
            arr[row][col] = num
            if solve_sudoku(arr):
                return True
            
            arr[row][col] = 0
    return False

if __name__ == "__main__":
    grid = [[0 for x in range(9)] for y in range(9)]

    grid = [[0, 4, 0, 2, 5, 0, 0, 6, 0],
            [9, 1, 0, 0, 7, 4, 0, 0, 0],
            [5, 0, 0, 1, 0, 0, 7, 0, 0],
            [0, 0, 0, 9, 0, 0, 5, 0, 3],
            [0, 0, 3, 0, 0, 0, 1, 0, 0],
            [8, 0, 1, 0, 0, 7, 0, 0, 0],
            [0, 0, 5, 0, 0, 2, 0, 0, 9],
            [0, 0, 0, 8, 1, 0, 0, 0, 0],
            [0, 2, 0, 0, 6, 9, 0, 5, 0]]

    print('Before solving:')
    print_grid(grid)
    if(solve_sudoku(grid)):
        print('\nAfter soliving:\n')
        print_grid(grid)
    else:
        print('\nNo Solution!!')



