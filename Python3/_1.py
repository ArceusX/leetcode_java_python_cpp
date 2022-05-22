"""
Algo: For each num, check if {target - that sum} exists as
      key in dict. If it does, return value of that key, which
      is index of {target - that sum}, and index of num.
      If not, store num and its index as key-value in dict.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx
        