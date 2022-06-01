class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
              
        # We increment this when we scan a new unique int,
        # for which we overrite that index in nums
        nUnique = 0

        for i in range(len(nums) - 1):
            #For all except last elem, compare elem to its successor
            #If same value, leave it to successor elem to process unique number
            if nums[i] != nums[i + 1]:
                nums[nUnique] = nums[i]
                nUnique += 1

        #If last elem is non-unique, its predecessors would have left responsibility
        #to it. Either way, it is processed as unique here.
        if len(nums) > 0:
            nums[nUnique] = nums[-1]
            nUnique += 1

        return nUnique
        