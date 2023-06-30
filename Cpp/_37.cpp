// 037: Solve Sudoku
// Backtracking: For each empty square, check which digit can
// be placed there without breaking sudoku condition. For such,
// continue to next empty square on same rowUsed. Else, reset
// square, try higher digit and if none suffices, return False to 
// calling function for it to try with its own higher digit 

class Solution {
public:

    // If rowUsed[a][b], digit b + 1 is already used by row a
    // Likewise for colUsed, blkUsed. Entries false at start
    bool rowUsed[9][9];
    bool colUsed[9][9];
    bool blkUsed[3][3][9];

    void solveSudoku(vector<vector<char>>& board) {

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;
                int digit = board[r][c] - '1';
                
                // Mark digit at board[r][c] as used for
                // board[r][c] particular row, col, block
                // digit evaluated as distance from '1'
                rowUsed[r][digit] = colUsed[c][digit] =
                blkUsed[r/3][c/3][digit] = true;
            }
        }

        // From upper-left, recursively solve right, then down
        solve(0, 0, board);
    }

    bool solve(int r, int c, vector<vector<char>>& board) {
        if (r > 8) return true; // If solve > 8 rows, solved board

        // Arrived at final col of row, so solve col 0 of next row
        if (c > 8) return solve(r + 1, 0, board);

        // (r, c) already filled, so go to next col on same row
        if (board[r][c] != '.') return solve(r, c + 1, board);

        for (int i = 0; i < 9; i++) {
            if (isValid(board, r, c, i)) {
                board[r][c] = '1' + i;
                rowUsed[r][i] = colUsed[c][i] = blkUsed[r/3][c/3][i] = true;

                if (solve(r, c + 1, board)) return true;

                // If cannot progress, must backtrack, so clear
                // square and constraints on used digit
                board[r][c] = '.';
                rowUsed[r][i] = colUsed[c][i] = blkUsed[r/3][c/3][i] = false;
            }
        }

        return false;
    }

    // Check if digit x + 1 is available for row, col, block
    bool isValid(vector<vector<char>>& board, int r, int c, int i) {
        if (rowUsed[r][i]) return false;
        if (colUsed[c][i]) return false;
        if (blkUsed[r/3][c/3][i]) return false;

        return true;
    }
};