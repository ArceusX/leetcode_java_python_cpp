// 001: Two Sum
/* For each num, check if {diff = target - num} exists
 * as key in map. If {diff} exists, return map[diff], 
 * val being {diff}'s index in nums, and num's index
 * Else, store [num: its index] in map */

class Solution {
public:
vector<int> twoSum(vector<int>& nums, int target) {

	// key is search mean and {diff = target - num}
    // is search target, so store diff as key
    unordered_map<int, int> diffs;
    
	for (int i = 0, sz = nums.size(); i < sz; i++) {
		int diff = target - nums[i];
		if (diffs.find(diff) != diffs.end()) {
			return vector<int> {i, diffs[diff]};
		}
		
		diffs[nums[i]] = i;
	}
        
	return vector<int>();
}
};