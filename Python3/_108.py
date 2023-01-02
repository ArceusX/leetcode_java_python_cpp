"""
Given range (initially [0, nums.size() - 1]), make mid elem
root of subtree, then split that range into two ranges,
one lower and one higher, and run same process to create
its left and right children. If for given node, its range
is impossible (hi < lo), that node cannot exist.

To work, initial range must exclude nums.size() and
mid elem index must be rounded-up.
"""
class Solution:
    def sortedArrayToBST(self, nums):
        return self.treeRecur(nums, 0, len(nums) - 1)
    
    def treeRecur(self, nums, lo, hi):
        if (hi < lo):
            return None
        
        mid = (lo + hi + 1) // 2
        return TreeNode(nums[mid], self.treeRecur(nums, lo, mid -1), self.treeRecur(nums, mid + 1, hi))
        
        