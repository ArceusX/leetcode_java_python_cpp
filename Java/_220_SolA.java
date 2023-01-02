/*
TreeSet Approach:

Keep TreeSet of size diffId and when it's filled, remove elem
with index in []nums diffId spaces from current elem. TreeSet
sorts elems, so for current elem, get vals from set from both 
directions with val  closest to current val and check if 
either difference with current val is within diffVal
*/

public class Solution {

// For True, for some i, j, abs(i - j) <= diffId and abs(nums[i] - nums[j]) <= diffVal
public boolean containsNearbyAlmostDuplicate(int[] nums, int diffId, int diffVal) {

	// Use Long rather than Integer because tests provide
	// values too large for Integer to fit
    TreeSet<Long> set = new TreeSet<>();

    for (int i = 0; i < nums.length; i++) {

        // Return smallest num in set >= num[i]
        Long greater = set.ceiling((long) nums[i]);
        if (greater != null && greater - nums[i] <= diffVal) return true;

        // Return largest num in set <= num[i]
        Long lesser = set.floor((long) nums[i]);
        if (lesser != null && nums[i] - lesser <= diffVal) return true;

        set.add((long)nums[i]);

        // Keep set's size within capacity
        if (i >= diffId) {
            set.remove((long)nums[i - diffId]);
        }
    }
    return false;
}
}