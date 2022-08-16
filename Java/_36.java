class Solution {
public boolean isValidSudoku(char[][] board) {
    boolean [][] row = new boolean[9][9];
    boolean [][] col = new boolean[9][9];
    boolean [][][] block = new boolean[3][3][9];
    
    for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char x = board[r][c];
                if (x != '.') {
                    
                    if (row[r][x - '1']) return false;
                    if (col[c][x - '1']) return false;
                    if (block[r/3][c/3][x - '1']) return false;
                    
                    row[r][x - '1'] = col[c][x - '1'] = 
                        block[r/3][c/3][x - '1'] = true;
                }
            }
    }
    return true;
}
}

// Slower, using set
/*class Solution {
public boolean isValidSudoku(char[][] board) {
    Set seen = new HashSet();
    for (int r = 0; r < 9; ++r) {
        for (int c = 0; c < 9; ++c) {
            if (board[r][c] != '.') {

            	// Must convert to String from char because char + int -> int, via ascii conversion
                String x = String.valueOf(board[r][c]);
                if (!seen.add(x + "+" + r) || !seen.add(x + "-" + c) || !seen.add(r/3 + x + c/3))
                    return false;
            }
        }
    }
    return true;
}
}*/