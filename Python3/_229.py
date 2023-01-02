"""
Voting algo:

1. 1st pass: Track counts of most promising candidates
2. 2nd pass: Verify if each candidate meets required benchmark
"""

class Solution:
    def majorityElement(self, nums):
        candidate1, candidate2, count1, count2 = -1, -1, 0, 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
                
            elif num == candidate2:
                count2 += 1
            
            elif count1 == 0:
                candidate1 = num
                count1 = 1
                
            elif count2 == 0:
                candidate2 = num
                count2 = 1
                
            else:
                count1 -= 1
                count2 -= 1
            
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
                
            elif num == candidate2:
                count2 += 1
                
            
        l = []
        if (count1 > len(nums) // 3):
            l.append(candidate1)
        if (count2 > len(nums) // 3):
            l.append(candidate2)
        
        return l
            
        