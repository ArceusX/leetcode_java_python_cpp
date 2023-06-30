class Solution {
public:
    vector<int> twoSum(vector<int> nums, int target) {
        int low = 0, high = nums.size() - 1;

        while (low < high) {
            int sum = nums[low] + nums[high];

            if (sum == target)
                return vector<int> {low + 1, high + 1};
            else if (sum > target)
                high--;
            else
                low++;
        }
        
        return vector<int> {-1, -1};
    }
};