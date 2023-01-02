# Left, Node, Right

class Solution:
    def inorderTraversal(self, current: Optional[TreeNode]):
        l, stack = [], []
        
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
                
            else:
                current = stack.pop()
                l.append(current.val)
                current = current.right
                
        return l