class Solution {
public int minSubArrayLen(int target, int[] nums) {
        int start = 0, end = 0, sum = 0;
        int minLen = Integer.MAX_VALUE;

        while (end < nums.length) {

            if (sum + nums[end] >= target) {
                minLen = Math.min(minLen, end - start);
                sum -= nums[start];
                start += 1;
            }
            else {
                sum += nums[end];
                end += 1;
            }
        }

        return minLen == Integer.MAX_VALUE ? 0 : minLen + 1;
    }
}