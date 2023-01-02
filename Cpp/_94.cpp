// Left, Node, Center

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> stack;
        vector<int> l;
        TreeNode* current = root;

        while (current || !stack.empty()) {
            if (current) {
                stack.push(current);
                current = current->left;

            }
            else {
                current = stack.top();
                stack.pop();
                l.push_back(current->val);
                current = current->right;
            }
        }
        return l;
    }
};