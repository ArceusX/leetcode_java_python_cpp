class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
              
        # Two pts: nUnique to write to (then ++) and i to read from
        nUnique = 0

        for i in range(len(nums) - 1):
            # Except for last elem, if elem has same val as
            # successor, leave it to successor to process unique num
            if nums[i] != nums[i + 1]:
                nums[nUnique] = nums[i]
                nUnique += 1

        # If last elem is non-unique, its predecessor would have 
        # left task to it. Either way, process it as unique here
        if len(nums) > 0:
            nums[nUnique] = nums[-1]
            nUnique += 1

        return nUnique
        