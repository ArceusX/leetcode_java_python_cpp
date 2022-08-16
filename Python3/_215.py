class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums) - 1
        
        while True:
            pivot = self.partition(nums, lo, hi)
            
            if pivot == k - 1:
                return nums[pivot]
            
            if pivot > k - 1:
                hi = pivot - 1
                
            else:
                lo = pivot + 1
                
    def partition(self, nums, lo, hi):
        nums[lo], nums[(lo + hi + 1)//2] = nums[(lo + hi + 1)//2], nums[lo]
        pivI, pivot = lo, nums[lo]
        lo += 1
        while (lo <= hi):
            if (nums[lo] < pivot < nums[hi]):
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1; hi -= 1
                
            if nums[lo] >= pivot:
                lo += 1
                
            if nums[hi] <= pivot:
                hi -= 1
                
        nums[pivI], nums[hi] = nums[hi], nums[pivI]
        
        return hi
