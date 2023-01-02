/*
Greedy algo: 
Sort []nums, check if adding largest unused num would
fill subset exactly, and if yes, continue onto next 
subset. If adding largest unused would overflow subset, 
backtrack, then try next largest unused num. Continue 
until all bins are filled to goal ( == sum(nums)/ k)
*/

class Solution {
	List<Boolean> used;

    public boolean canPartitionKSubsets(int[] nums, int k) {
    	if (k == 1) return true;

        int goal = Arrays.stream(nums).sum();
        if (goal % k != 0) return false;

        used = new ArrayList<Boolean>(Arrays.asList(new Boolean[nums.length]));
        Collections.fill(used, false);

        goal /= k;

        nums = Arrays.stream(nums).boxed().sorted(Comparator.reverseOrder())
        .mapToInt(Integer::intValue)
        .toArray();
        
        return tryPartition(nums, k, goal, 0, 0);
    }

    private boolean tryPartition(int[] nums, int k, int goal, int curSum, int iToCheck) {
    	if (k == 1) return true;

    	if (curSum == goal) return tryPartition(nums, k - 1, goal, 0, 0);

    	for (int i = iToCheck; i < nums.length; i++) {
    		if (i > 0 && !used.get(i - 1) && nums[i - 1] == nums[i]) continue;

    		if (!used.get(i) && (curSum + nums[i]) <= goal) {
    			used.set(i, true);

    			if (tryPartition(nums, k, goal, curSum + nums[i], i + 1)) {
    				return true;
    			}
    			
    			used.set(i, false);
    		}
    	}
    	return false;
    }
}