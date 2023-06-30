// 037: Solve Sudoku
// Backtracking: For each empty square, check which digit can
// be placed there without breaking sudoku condition. For such,
// continue to next empty square on same rowUsed. Else, reset
// square, try higher digit and if none suffices, return False to 
// calling function for it to try with its own higher digit 

class Solution {

    // If rowUsed[a][b], digit b + 1 is already used by row a
    // Likewise for colUsed, blkUsed. Entries false at start
    boolean [][]   rowUsed = new boolean[9][9];
    boolean [][]   colUsed = new boolean[9][9];
    boolean [][][] blkUsed = new boolean[3][3][9];

    public void solveSudoku(char[][] board) {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                int digit = board[r][c] - '1';

                rowUsed[r][digit] = colUsed[c][digit] =
                blkUsed[r/3][c/3][digit] = true;
            }
        }

        // From upper-left, recursively solve right, then down
        solve(0, 0, board);
    }

    boolean solve(int r, int c, char[][] board) {
        if (r > 8) return true; // If solve > 8 rows, solved board

        // Arrived at final col of row, so solve col 0 of next row
        if (c > 8) return solve(r + 1, 0, board);

        // (r, c) already filled, so go to next col on same row
        if (board[r][c] != '.') return solve(r, c + 1, board);

        for (int x = 0; x < 9; x++) {
            if (isValid(r, c, x)) {
                board[r][c] = (char)('1' + x);

                blkUsed[r/3][c/3][x] = 
                rowUsed[r][x] = colUsed[c][x]  = true;

                if (solve(r, c + 1, board)) return true;

                // If cannot progress, must backtrack, so clear
                // square and constraints on used digit
                board[r][c] = '.';

                blkUsed[r/3][c/3][x] = 
                rowUsed[r][x] = colUsed[c][x]  = false;
            }
        }
        return false;
    }

    // Check if digit x + 1 is available for row, col, block
    boolean isValid(int r, int c, int x) {
        if (rowUsed[r][x]) return false;
        if (colUsed[c][x]) return false;
        if (blkUsed[r/3][c/3][x]) return false;

        return true;
    }
}