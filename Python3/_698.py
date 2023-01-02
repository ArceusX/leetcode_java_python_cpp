"""
Greedy algo: 
Sort []nums, check if adding largest unused num would
fill subset exactly, and if yes, continue onto next 
subset. If adding largest unused would overflow subset, 
backtrack, then try next largest unused num. Continue 
until all bins are filled to goal ( == sum(nums)/ k)
"""

class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        
        goal = sum(nums)
        if goal % k != 0:
            return False

        # Sum to fill for each subset
        goal /= k

        # Greedy algo: check larger vals before smaller ones
        nums.sort(reverse = True)
        used = [False] * len(nums)
        
        def tryPartition(k, setSum = 0, iToCheck = 0):

            # Partition remaining vals over remaining subsets
            if k == 1:
                return True
            
            # Subset filled. Continue to remaining subsets
            if setSum == goal:
                return tryPartition(k - 1)
            
            for i in range(iToCheck, len(nums)):

                # If previous i was checked, and not used, and it
                # share val with current i, skip current i because
                # we know it also won't be used
                if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                    continue

                # If already used or would cause setSum to exceed goal, 
                # don't use current and continue onto next (smaller) val
                if not used[i] and setSum + nums[i] <= goal:
                    used[i] = True
                    if tryPartition(k, setSum = setSum + nums[i], iToCheck = i + 1):
                        return True

                    # Backtrack
                    used[i] = False
                    
            return False 
        
        return tryPartition(k)