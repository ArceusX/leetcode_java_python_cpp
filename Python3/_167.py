class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        
        while (low < high):
            sum_ = nums[low] + nums[high]
            if sum_ == target:

            	#nums given as range 1 to n
                return [low + 1, high + 1]
                
            elif sum_ > target:
                high -= 1
            else:
                low += 1
    	
