// Node, Left, Right

class Solution {
    public List<Integer> preorderTraversal(TreeNode current) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> l = new ArrayList<>();

        while (current != null || !stack.isEmpty()) {
        	if (current != null) {
        		l.add(current.val);
        		if (current.right != null) stack.push(current.right);
        		current = current.left;
        	}
        	else {
        		current = stack.pop();
        	}
        }

        return l;
    }
}