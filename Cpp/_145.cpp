//Left, Right, Node

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* current) {
    	stack<TreeNode*> stack;
    	vector<int> l;
    	TreeNode* prev = nullptr;

    	while (current || !stack.empty()) {
            // First task: go as far left as possible down
            
    		if (current) {
    			stack.push(current);
    			current = current->left;
    		}
    		else {

                // Backtrack up one, then try head down right child
                // If right child does not exist, or we backtracked
                // from right child immediately last step,
                // (making prev == current.right), record current,
                // set prev = current for next iteration, then
                // continue backtracking.
                
                // Note: Only pop stack if need to backtrack

    			current = stack.top();
    			if (!current->right || prev == current->right) {
    				l.push_back(current->val);
    				stack.pop();
    				prev = current;
    				current = nullptr;
    			}
    			else current = current->right;
    		}
    	}
    	return l;
    }
};