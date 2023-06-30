// 001: Two Sum
/* For each num, check if {diff = target - num} exists
 * as key in map. If {diff} exists, return map[diff], 
 * val being {diff}'s index in nums, and num's index
 * Else, store [num: its index] in map */

class Solution {
public int[] twoSum(int[] nums, int target) {
        
    // key is search mean and {diff = target - num}
    // is search target, so store diff as key
    Map<Integer, Integer> diffs = new HashMap<>();
    
    for (int i = 0, len = nums.length; i < len; i++){
        Integer diff = (Integer) (target - nums[i]);
        if (diffs.containsKey(diff)) {
            return new int[] {diffs.get(diff), i};
        }

        diffs.put(nums[i], i);
    }
    
    return null; 
}
}