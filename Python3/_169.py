"""
Majority Voting Algo:

Initialize nums[0] as candidate elem and its count to 1.
Everytime we encounter elem of same val as candidate,
count++. If encounter different val to candidate, 
count-- and update candidate to that new val.

At end, check that count of candidate indeed is
half or more of total votes/size of nums
"""

class Solution:
    def majorityElement(self, nums) -> int:
        
        candidate = nums[0]
        nCandidate = 0
        
        for num in nums:
            if candidate == num:
                nCandidate += 1
                
            else:
                nCandidate -= 1
                
                if nCandidate == 0:
                    candidate = num
                    nCandidate = 1
                    
        return candidate
        