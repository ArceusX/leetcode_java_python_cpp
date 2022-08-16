class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False for _ in range(9)] for _ in range(9)]
        col = [[False for _ in range(9)] for _ in range(9)]
        block = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]
        
        for r in range(9):
            for c in range(9):
                x = board[r][c]
                
                if x != '.':
                    if row[r][ord(x) - ord('1')]: return False
                    if col[c][ord(x) - ord('1')]: return False
                    if block[r//3][c//3][ord(x) - ord('1')]: return False
                    
                    row[r][ord(x) - ord('1')] = \
                    col[c][ord(x) - ord('1')] = \
                    block[r//3][c//3][ord(x) - ord('1')] = True
                    
        return True
                    
                    
        