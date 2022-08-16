class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

    	int nUnique = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
        	if (nums[i] != nums[i + 1]) {
        		nums[nUnique] = nums[i];
        		nUnique++;
        	}
        }

        if (nums.size() > 0) {
        	nums[nUnique] = nums.back();
        	nUnique++;
        }
        
        return nUnique;
    }
};