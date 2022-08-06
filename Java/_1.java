class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++){
            Integer numToFind = (Integer) (target - nums[i]);
            if (map.containsKey(target - nums[i])) {
                return new int[] {i, map.get(numToFind)};
            }

            map.put(nums[i], i);
        }
        
        return null; 
    }
}