// 2080: Get Count of Target Value Between L, R Array Indices

// Complexity: O(n) space, O(ln n) time 
// Group indices in arr holding same value, each group being
// naturally sorted, and map group to value. Get group from
// key target and return length = upper_bound - lower_bound, 
// where upper is 1 + index of R and lower is index of L in group

class RangeFreqQuery {
public:
    unordered_map<int, vector<size_t>> found;

    RangeFreqQuery(vector<int>& arr) {
        for (int i = 0, size = arr.size(); i < size; i++) {
            found[arr[i]].push_back(i);
        }
    }
    
    int query(int L, int R, int target) {
        vector<size_t>& V = found[target];

        // lower_bound:     leftmost  index in V with value L
        // upper_bound: 1 + rightmost index in V with value R
        // Get index after, but not, final holding target value
        // If none in V exceeds R, upper_bound() gives V.end()
        return upper_bound(begin(V), end(V), R) - lower_bound(begin(V), end(V), L);
    }
};


