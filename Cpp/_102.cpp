/*
Use dummy elem (None) to indicate end of current
level, then add dummy for next level. Level-order 
requires breadth-first, which requires queue
*/

// Iterative
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) return vector<vector<int>>();
        queue<TreeNode*> q;
        q.push(root);
        q.push(nullptr);
        
        vector<vector<int>> li;
        vector<int> levelLi;
        
        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();
            
            if (current) {
                levelLi.push_back(current->val);
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
            else {
                li.push_back(levelLi);
                levelLi.clear();
                if (!q.empty()) q.push(nullptr);
            }
        }
        
        return li;
    }
};