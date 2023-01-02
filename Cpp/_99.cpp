/*
Inorder traversal of BST gives sorted list. BST with
two nodes swapped and out of order gives sorted list 
from low to high with two values swapped. To identify
those needing to be swapped back, traverse from
either end and get first elems failing to respect
order. "Reverse inorder" is (Right, Node, Left)
*/

class Solution {
public:
    void recoverTree(TreeNode* current) {
        TreeNode* n1 = BSTUtil(current);
        TreeNode* n2 = BSTUtil(current, false);

        int temp = n1->val;
        n1->val = n2->val;
        n2->val = temp;
    }

    TreeNode* BSTUtil(TreeNode* current, bool regular = true) {
        stack<TreeNode*> stack;
        TreeNode* prev = nullptr;

        while (current || !stack.empty()) {
            if (current) {
                stack.push(current);
                current = regular ? current->left : current->right;
            }
            else {
                current = stack.top();
                stack.pop();
                if (prev) {
                    if ((prev->val == current->val) ||
                        (prev->val > current->val && regular) ||
                        (prev->val < current->val && !regular)) {

                        return prev;
                    }
                }
                prev = current;
                current = regular ? current->right : current->left;
            }
        }
        return nullptr;
    }
};