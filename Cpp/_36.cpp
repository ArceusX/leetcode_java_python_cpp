// 036: Valid Sudoku (if filled squares are valid)

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        std::unordered_set<char> set;

        for (size_t r = 0; r < 9; r++) {
            for (size_t c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue; 

                // Check insertable (no dupl is already present)
                if (!set.insert(board[r][c]).second) {
                    return false;
                }
            }
            set.clear();
        }

        // Check no dupl in col. Loops swap position
        for (size_t c = 0; c < 9; c++) {
            for (size_t r = 0; r < 9; r++) {
                if (board[r][c] == '.') continue;

                if (!set.insert(board[r][c]).second) {
                    return false;
                }
            }
            set.clear();
        }

        for (size_t i = 0; i < 9; i++) {
            size_t r = 3 * (i / 3);
            size_t c = 3 * (i % 3);

            for (size_t r_ = 0; r_ < 3; ++r_) {
                for (size_t c_ = 0; c_ < 3; ++c_) {
                    if (board[r + r_][c + c_] == '.') continue;

                    if (!set.insert(board[r + r_][c + c_]).second) {
                        return false;
                    }
                }
            }
            set.clear();
        }

        return true;
    }
};