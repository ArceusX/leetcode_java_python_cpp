class Solution:
    def missingNumber(self, nums) -> int:
        
        prod = 0
        i = 1
        
        for num in nums:
            prod ^= num
            prod ^= i
            i += 1
            
        return prod
        