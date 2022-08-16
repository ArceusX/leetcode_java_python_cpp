class Solution {

	// If row[a][b] == True, digit b + 1 already
	// selected in row. Similar for col, block
	bool row[9][9], col[9][9], block[3][3][9];
public:
    void solveSudoku(vector<vector<char>>& board) {

    	// Intialize each digit as unused for all
        memset(row, false, sizeof(row));
        memset(col, false, sizeof(col));
        memset(block, false, sizeof(block));

        for (int r = 0; r < 9; r++) {
        	for (int c = 0; c < 9; c++) {
        		if (board[r][c] != '.') {

        			// Mark non-. board[r][c] as used for
        			// its particular row, col, + block
        			row[r][board[r][c] - '1'] = true;
        			col[c][board[r][c] - '1'] = true;
        			block[r/3][c/3][board[r][c] - '1'] = true;
        		}
        	}
        }

        // From upper-left solve recurisvely right, then down
        solve(0, 0, board);
    }

    bool solve(int r, int c, vector<vector<char>>& board) {
    	if (r == 9) return true;

    	// Got to last col of row, so solve next row
    	if (c == 9) return solve(r + 1, 0, board);

    	// (r, c) already filled, so go to next on same row
    	if (board[r][c] != '.') return solve(r, c + 1, board);

    	for (char x = '1'; x <= '9'; x++) {
    		if (isValid(r, c, x)) {
                
                board[r][c] = x;
    			row[r][x - '1'] = col[c][x - '1'] = 
    			block[r/3][c/3][x - '1'] = true;

    			if (solve(r, c + 1, board)) return true;

                // If continuing forward, had to backtrack, 
                // clear square and used digit
                board[r][c] = '.';
    			row[r][x - '1'] = col[c][x - '1'] = 
    			block[r/3][c/3][x - '1'] = false;
    		}
    	}

    	return false;
    }

    bool isValid(int r, int c, char x) {
    	if (row[r][x - '1']) return false;
    	if (col[c][x - '1']) return false;
    	if (block[r/3][c/3][x - '1']) return false;

    	return true;
    }
};