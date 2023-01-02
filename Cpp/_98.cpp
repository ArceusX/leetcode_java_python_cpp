/*
Binary search tree satisfies 3 conditions:

1. All nodes in left subtree have lower val
2. All nodes in right subtree have higher val
3. Left and right subtrees must also be BST

BST follows inorder (Left-Node-Right) traversal
For inorder, nodes of left subtree are traversed
[before] subtree root and they must have lower val
than root in BST. Likewise, nodes of right subtree
traversed [after] root and they must have higher
val than root in BST
*/

// Iterative
class Solution {
public:
    bool isValidBST(TreeNode* current) {
        stack<TreeNode*> stack;
        TreeNode* prev = nullptr;

        while (current || !stack.empty()) {
            if (current) {
                stack.push(current);
                current = current->left;
            }
            else {
                current = stack.top();
                stack.pop();
                if (prev && prev->val >= current->val) {
                    return false;
                }
                prev = current;
                current = current->right;
            }
        }
        return true;
    }
};

//Recursive

// Passing bound values for recursion as in _98.py returns
// wrong result if any node has val INT_MAX or INT_MIN

// To avoid issues with INT_MAX or INT_MIN comparisons,
// pass nodes providing boundaries directly

class Solution {
public:
    bool isValidBST(TreeNode* current) {
        return BSTUtil(current, nullptr, nullptr);
    }
    
    bool BSTUtil(TreeNode* current, TreeNode* lo, TreeNode* hi) {
        if (!current) return true;
        
        if (lo && current->val <= lo->val) return false;
        if (hi && current->val >= hi->val) return false;
        
        return BSTUtil(current->left, lo, current) && BSTUtil(current->right, current, hi);
    }
};