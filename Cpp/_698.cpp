class Solution {
public:
    bool* used;
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        if (k == 1) return true;
    
        int goal = std::accumulate(nums.begin(), nums.end(), 0);
        if (goal % k != 0) return false;
        
        goal /= k;
        
        used = new bool[nums.size()];
        std::fill(used, used + nums.size(), false);
        
        std::sort(nums.begin(), nums.end(), std::greater<>());
        
        return tryPartition(nums, k, goal);
    }
    
    bool tryPartition(const vector<int>& nums, int k, int goal,
                      int currSum = 0, int iToCheck = 0) {
        
        if (k == 1) return true;
        if (currSum == goal) return tryPartition(nums, k - 1, goal);
        
        for (int i = iToCheck; i < nums.size(); i++) {
            if (i > 0 && !used[i - 1] && nums[i - 1] == nums[i]) continue;
            
            if (!used[i] && (currSum + nums[i]) <= goal) {
                used[i] = true;
                
                if (tryPartition(nums, k, goal, currSum + nums[i], i + 1)) {
                    return true;
                }
                
                used[i] = false;
            }
        }
                    
        return false;
    }
};