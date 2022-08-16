class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
    	// Place k largest elems from [begin, end] at first
    	// k slots from begin. Algo uses partial heapsort/select
        partial_sort(nums.begin(), nums.begin() + k, nums.end(), greater<int>());
        return nums[k - 1];
    }
};

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
    	// Place kth largest at (begin + k - 1) and (k - 1)
    	// elems greater from [begin, begin + k - 1)
    	// Algo uses introsort, variant of quicksort
        nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), greater<int>());
        return nums[k - 1];
    }
};

// Priority queue/heap with <less> having lower priority
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> pq(nums.begin(), nums.end());
        for (int i = 0; i < k - 1; i++) pq.pop();

        return pq.top();
    }
};