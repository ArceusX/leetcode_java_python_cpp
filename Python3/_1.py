"""
Algo: For each num, check if {target - num} exists as key
      in dict. If exists, return value of that key, which
      is index of {target - that sum}, and index of num.
      If not, store num and its index as key-value in dict
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Store num as key because that's what we search for
        # and its index as val because that's what we return

        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [idx, values[target - value]]

            values[value] = idx
        