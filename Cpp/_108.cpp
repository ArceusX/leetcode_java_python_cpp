/*
Given range (initially [0, nums.size() - 1]), make mid elem
root of subtree, then split that range into two ranges,
one lower and one higher, and run same process to create
its left and right children. If for given node, its range
is impossible (hi < lo), that node cannot exist.

To work, initial range must exclude nums.size() and
mid elem index must be rounded-up.
*/
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return makeRecur(nums, 0, nums.size() - 1);
    }

    TreeNode* makeRecur(vector<int>& nums, int lo, int hi) {
        if (hi < lo) return nullptr;
        int mid = (lo + hi + 1) / 2;
        return new TreeNode(nums[mid], makeRecur(nums, lo, mid - 1),
            makeRecur(nums, mid + 1, hi));
    }
};