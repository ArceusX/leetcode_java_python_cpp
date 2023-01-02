// Left, Right, Node

class Solution {
    public List<Integer> postorderTraversal(TreeNode current) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> l = new ArrayList<>();

        TreeNode prev = null;

        while (current != null || !stack.isEmpty()) {
        	if (current != null) {
        		stack.push(current);
        		current = current.left;
        	}
        	else {
        		current = stack.peek();
        		if (current.right == null || current.right == prev) {
        			stack.pop();
        			l.add(current.val);
        			prev = current;
        			current = null;
        		}
        		else {
        			current = current.right;
        		}

        	}
        }

        return l;
    }
}