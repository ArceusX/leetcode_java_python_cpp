/* 
HashMap Approach:

Store (num, its index in nums[]) in map. For each num, if
its duplicate already exists in map, check if duplicate's 
value in map/duplicate's index in []nums is not more
than diffId spaces from current num's index in []nums.

Set Approach:
Maintain set of size diffId. Check for duplicates. After 
iteration i, remove earliest entry nums[i - diffId] if set 
is "full" for purpose of problem (set.size() > diffId).

*/

// HashMap
class Solution {
public boolean containsNearbyDuplicate(int[] nums, int diffId) {
	Map<Integer, Integer> map = new HashMap<>();
	for (int i = 0; i < nums.length; i++) {
		if (map.containsKey(nums[i])) {
			if (i - map.get(nums[i]) <= diffId) return true;
		}
		map.put(nums[i], i);
	}
	return false;
}
}

// Set
class Solution {
public boolean containsNearbyDuplicate(int[] nums, int diffId) {
	Set<Integer> set = new HashSet<>();
	for (int i = 0; i < nums.length; i++) {
		if (set.contains(nums[i])) return true;
		set.add(nums[i]);
		if (i >= diffId) set.remove(nums[i - diffId]);
	}
	return false;
}
}