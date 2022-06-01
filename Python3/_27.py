class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nCount = 0
        
        for num in nums:
            if num != val:
                nums[nCount] = num
                nCount += 1
                
        return nCount