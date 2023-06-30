# 037: Solve Sudoku
# Backtracking: For each empty square, check which digit can
# be placed there without breaking sudoku condition. For such,
# continue to next empty square on same rowUsed. Else, reset
# square, try higher digit and if none suffices, return False to 
# calling function for it to try with its own higher digit 

class Solution:
    def solveSudoku(self, board) -> None:

        # If rowUsed[a][b], digit b + 1 is already used by row a
        # Likewise for colUsed, blkUsed. Entries false at start
        self.rowUsed = [[False for _ in range(9)] for _ in range(9)]
        self.colUsed = [[False for _ in range(9)] for _ in range(9)]
        self.blkUsed = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                self.rowUsed[r][ord(board[r][c]) - ord('1')] = True
                self.colUsed[c][ord(board[r][c]) - ord('1')] = True
                self.blkUsed[r//3][c//3][ord(board[r][c]) - ord('1')] = True
                    
        # From upper-left, recursively solve right, then down
        self.solve(0, 0, board)
        
    def solve(self, r, c, board):
        if (r > 8): return True # If solve > 8 rows, solved board

        # Arrived at final col of row, so solve col 0 of next row
        if (c > 8): return self.solve(r + 1, 0, board)

        // (r, c) already filled, so go to next col on same row
        if (board[r][c] != '.'): return self.solve(r, c + 1, board)
        
        for x in range(0, 9):
            if (self.isValid(r, c, x)):
                board[r][c] = string.digits[x + 1]
                self.rowUsed[r][x] = True
                self.colUsed[c][x] = True
                self.blkUsed[r//3][c//3][x] = True
                
                if (self.solve(r, c + 1, board)): return True

                # If cannot progress, must backtrack, so clear
                # square and constraints on used digit
                
                board[r][c] = '.'
                self.rowUsed[r][x] = False
                self.colUsed[c][x] = False
                self.blkUsed[r//3][c//3][x] = False
                
        return False
    
    # Check if digit x + 1 is available for row, col, block
    def isValid(self, r, c, x):
        if self.rowUsed[r][x]: return False
        if self.colUsed[c][x]: return False
        if self.blkUsed[r//3][c//3][x]: return False
        
        return True