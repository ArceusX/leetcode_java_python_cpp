import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> hash = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++){
            Integer diff = (Integer) (target - nums[i]);
            if (hash.containsKey(target - nums[i])) {
                return new int[] {hash.get(diff), i};
            }

            hash.put(nums[i], i);
        }
        
        return null; 
    }
}