class Solution {
public:

    // Binary search with sorted structure, except need to convert
    // 1-dim index to to 2-dim index: mid -> (mid / n) x (mid % n)
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix[0].size();
        int high = matrix.size() * n - 1;
        
        if (target > matrix.back()[n-1] || target < matrix[0][0]) return false;
        int low = 0;
        
        while (low <= high) {
            int mid = (low + high) / 2;

            if (matrix[mid / n][mid % n] == target) {
                return true;
            }

            if (matrix[mid / n][mid % n] < target) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }
        return false;
    }
};