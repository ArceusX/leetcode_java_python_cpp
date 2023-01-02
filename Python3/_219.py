"""
HashMap Approach:

Store (num, its index in nums[]) in map. For each num, if
its duplicate already exists in map, check if duplicate's 
value in map/duplicate's index in []nums is not more
than diffId spaces from current num's index in []nums.

Set Approach:
Maintain set of size diffId. Check for duplicates. After 
iteration i, remove earliest entry nums[i - diffId] if set 
is "full" for purpose of problem (set.size() > diffId).
"""

# Map/Dict
class Solution:
    def containsNearbyDuplicate(self, nums, diffId: int) -> bool:
    	d = {}

    	for (i, num) in enumerate(nums):
    		if num in d:
    			if (i - d[num] <= diffId):
    				return True

    		d[num] = i

    	return False

# Set with capacity of diffId
class Solution:
    def containsNearbyDuplicate(self, nums, diffId: int) -> bool:
    	s = set()

    	for (i, num) in enumerate(nums):
            if num in s:
                return True
            
            s.add(num)
            if i > diffId:
                s.remove(nums[i - diffId])

    	return False
        