"""
For entry in []nums, interpret its index as inNode and its
val as outNode. Duplicate val is one that has two inEdges:
start of cycle. Problem reduces to that of finding start.
Treat num with index in []nums, but without val as head 
"""
class Solution:
    def findDuplicate(self, nums) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        slow = 0
        while (slow != fast):
            slow = nums[slow]
            fast = nums[fast]
            
        return slow