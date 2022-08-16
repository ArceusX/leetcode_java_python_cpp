class Solution:
    row = col = block = None
    def solveSudoku(self, board) -> None:
        self.row = [[False for _ in range(9)] for _ in range(9)]
        self.col = [[False for _ in range(9)] for _ in range(9)]
        self.block = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]
        
        for r in range(9):
            for c in range(9):
                if (board[r][c] != '.'):
                    self.row[r][ord(board[r][c]) - ord('1')] = True
                    self.col[c][ord(board[r][c]) - ord('1')] = True
                    self.block[r//3][c//3][ord(board[r][c]) - ord('1')] = True
                    
        self.solve(0, 0, board)
        
    def solve(self, r, c, board):
        if (r == 9): return True
        if (c == 9): return self.solve(r + 1, 0, board)
        if (board[r][c] != '.'): return self.solve(r, c + 1, board)
        
        for x in string.digits[1:]:
            if (self.isValid(r, c, x)):
                board[r][c] = x
                self.row[r][ord(x) - ord('1')] = True
                self.col[c][ord(x) - ord('1')] = True
                self.block[r//3][c//3][ord(x) - ord('1')] = True
                
                if (self.solve(r, c + 1, board)): return True
                
                self.row[r][ord(x) - ord('1')] = False
                self.col[c][ord(x) - ord('1')] = False
                self.block[r//3][c//3][ord(x) - ord('1')] = False
                
                board[r][c] = '.'
                
        return False
    
    def isValid(self, r, c, x):
        if self.row[r][ord(x) - ord('1')]: return False
        if self.col[c][ord(x) - ord('1')]: return False
        if self.block[r//3][c//3][ord(x) - ord('1')]: return False
        
        return True