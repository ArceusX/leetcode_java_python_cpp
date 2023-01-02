class Solution {
public:
    vector<int> preorderTraversal(TreeNode* current) {
        stack<TreeNode*> stack;
    	vector<int> l;
        
        while (current || !stack.empty()) {
            if (current) {
                l.push_back(current->val);
                if (current->right) stack.push(current->right);
                current = current->left;
            }
            else {
                current = stack.top();
                stack.pop();
            }
        }
        
        return l;
    }
};