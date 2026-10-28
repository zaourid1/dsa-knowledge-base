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
    #checking rows
    row_set = set()
    for row in board:
        for element in row:
            if element != '.' and element not in row_set:
                row_set.add(element)
            elif element in row_set:
                return False
            else:
                pass
       
        row_set = set()
    
    #board[row][col]
    #checking cols
    for i in range(9):
        col_set = set()
        for j in range(9):
            #checking cols now
            element = board[j][i]
            if element != '.' and element not in col_set:
                col_set.add(element)
            elif element in col_set:
                return False
            else:
                pass

    #now checking each 3 x 3 box
    for i in range(0,9,3):
        for j in range(0,9,3):
            #trying to print every 3 numbs a break
            #print(i,j)
            start_row = i
            #print("math: ",start_row, start_row + 3)
            start_col = j
            box_set = set()
            #print("math col: ",start_col, start_col + 3)
            for a in range(start_row,start_row+3):
                for b in range(start_col, start_col+3):
                    element = board[a][b]
                    if element != '.' and element not in box_set:
                        box_set.add(element)
                    elif element in box_set:
                        return False
                    else:
                        pass
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

board_two = [["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","1",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board_two))