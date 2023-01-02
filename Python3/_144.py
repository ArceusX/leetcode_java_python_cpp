class Solution:
    def preorderTraversal(self, current: Optional[TreeNode]):
        l, stack = [], []
        
        while (current or stack):
            if current:
                l.append(current.val)
                if current.right:
                    stack.append(current.right)
                    
                current = current.left
                
            else:
                current = stack.pop()
                
        return l
        