class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        
        while (low < high):
            sum_ = nums[low] + nums[high]
            
            if sum_ == target:
            	# indices given as range 1 to n (1-indexed)
                return [low + 1, high + 1]
                
            # Case: Invalidate nums[high] as candidate because
            # its sum with lowest still-viable candidate still 
            # exceeds target
            elif sum_ > target:
                high -= 1
            else:
                low += 1
    	
