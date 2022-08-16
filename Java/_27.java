class Solution {
    public int removeElement(int[] nums, int val) {
        int nCount = 0;
        for (int num : nums) {
        	if (val != num) {
        		nums[nCount] = num;
        		nCount++;
        	}
        }
        return nCount;
    }
}