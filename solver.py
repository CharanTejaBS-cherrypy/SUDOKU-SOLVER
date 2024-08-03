def is_valid_sudoku(grid):
    def is_valid_block(block):
        nums = [num for num in block if num != 0]
        return len(nums) == len(set(nums))

    for i in range(9):
        row = [grid[i][j] for j in range(9)]
        if not is_valid_block(row):
            return False

        column = [grid[j][i] for j in range(9)]
        if not is_valid_block(column):
            return False

        subgrid = [grid[m][n] for m in range(
            i // 3 * 3, (i // 3 + 1) * 3) for n in range(i % 3 * 3, (i % 3 + 1) * 3)]
        if not is_valid_block(subgrid):
            return False

    return True


def solve_sudoku(grid):
    solve_sudoku_util(grid)
    return grid


def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def is_safe(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku_util(grid):
    location = find_empty_location(grid)
    if not location:
        return True
    row, col = location

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku_util(grid):
                return True
            grid[row][col] = 0

    return False
