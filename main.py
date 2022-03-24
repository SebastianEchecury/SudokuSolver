import time

def isValidMove(grid, row, column, number): # To see if in this grid, in this row and this column is this number right
    for x in range(9):
        if grid[row][x] == number:
            return False

    for x in range(9):
        if grid[x][column] == number:
            return False

    corner_row = row - row % 3
    corner_column = column - column % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_column + y] == number:
                return False

    return True

def solve(grid, row, column):
    if column == 9:
        if row == 8:
            return True
        row += 1
        column = 0

    if grid[row][column] > 0: # Means there is already a number
        return solve(grid, row, column + 1)

    for number in range(1 ,10): # 1, 2... 8, 9
        if isValidMove(grid, row, column, number):
            grid[row][column] = number
            if solve(grid, row, column):
                return True

        grid[row][column] = 0 # If didnt found any valid move puts 0

    return  False

# 0 = no number
grid = [
    [0, 0, 0, 0, 0, 0, 6, 8, 0],
    [0, 0, 0, 0, 7, 3, 0, 0, 9],
    [3, 0, 9, 0, 0, 0, 0, 4, 5],
    [4, 9, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 3, 0, 5, 0, 9, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [9, 6, 0, 0, 0, 0, 3, 0, 8],
    [7, 0, 0, 6, 8, 0, 0, 0, 0],
    [0, 2, 8, 0, 0, 0, 0, 0, 0]
]

start = time.time()
if solve(grid, 0, 0):
    print('Solution:')
    for i in range(9):
        for j in range (9):
            print(grid[i][j], end=' ')
        print()
else:
    print('No solution for this sudoku')
end = time.time()

print('Took ', end - start, ' seconds')