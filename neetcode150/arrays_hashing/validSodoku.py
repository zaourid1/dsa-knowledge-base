"""
medium level. 
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain 
the digits 1-9 without duplicates.
"""

def isValidSudoku(board):
    """
    thought process: use a set 
    """
    row_set = set()
    col_set = set()
    for i in range(9):
        row = board[i]
        for cell in row:
            #print(cell)
            if cell != '.':
                if cell not in row_set:
                    row_set.add(cell)
                else:
                    return False
            #print(row_set)
        row_set = set()
        
        for j in range(9):
            #board[row][col]
            c = board[j][i]
            if c != '.':
                if c not in col_set:
                    col_set.add(c)
                else:
                    return False
        col_set = set()
    
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            # We are now at the starting position of a box!
            for i in board[box_row][box_col]:
                print(i)
                
    return True

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

#print(board)
print(isValidSudoku(board))