# 001: Two Sum
# For each num, check if {diff = target - num} exists
# as key in dict. If {diff} exists, return dict[diff], 
# val being {diff}'s index in nums, and num's index
# Else, store [num: its index] in dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

    	# key is search mean and {diff = target - num}
    	# is search target, so store diff as key
        diffs = {}

        for i, num in enumerate(nums):
            if target - num in diffs:
                return [diffs[target - num], i]

            diffs[num] = i
        