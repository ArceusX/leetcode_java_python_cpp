/* Preorder -> (Node, Left, Right); Inorder -> (Left, Node, Right)

preorder[0] must be root. Get its inorder index, create root 
node, split along that index into lower/left and higher/right 
ranges. For subtree, its range in inorder has same length as
match in preorder, except with nodes in different order.
preorder[0 + 1] to be root of its left subtree. Repeat process:
preorder[1 + 1] to be root of left subtree of preorder[1]
*/

class Solution {
public:
	unordered_map<int, int> valToInI;
	int preI;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {

        for (int i = 0; i < inorder.size(); i++) {
        	valToInI.emplace(inorder[i], i);
        }

        return toTree(preorder, 0, preorder.size() - 1);
    }

    TreeNode* toTree(vector<int>& preorder, int start, int end) {
    	if (end < start) return nullptr;

    	int val = preorder[preI++];
    	int valIndex = valToInI[val];

    	return new TreeNode(val, 
    		toTree(preorder, start, valIndex - 1),
    		toTree(preorder, valIndex + 1, end));

    }
};