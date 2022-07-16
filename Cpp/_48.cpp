/* Algo:
 *      Number of concentric layers for size n is ceil(n/2).
 *      Each layer has (n-1) groups of four entries that are 
 *      rotated into next in group. A pattern can be observed
 *      and found by trial and error.
*/

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {

        int n = matrix.size();
        if (n == 1) return;
        for (int i = 0; i <= n / 2; i++) {
            for (int j = i; j < n - 1 - i; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][i];
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
                matrix[j][n-1-i] = tmp;
            }
        }
        
    }
};