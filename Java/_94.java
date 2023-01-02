// Left, Node, Right

class Solution {
    public List<Integer> inorderTraversal(TreeNode current) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> l = new ArrayList<>();

        while (current != null || !stack.isEmpty()) {
        	if (current != null) {
        		stack.push(current);
        		current = current.left;
        	}
        	else {
        		current = stack.pop();
        		l.add(current.val);
        		current = current.right;
        	}
        }

        return l;
    }
}