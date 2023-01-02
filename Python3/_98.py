"""Binary search tree satisfies 3 conditions:

1. All nodes in left subtree have lower val
2. All nodes in right subtree have higher val
3. Left and right subtrees must also be BST

BST follows inorder (Left-Node-Right) traversal
For inorder, nodes of left subtree are traversed
[before] subtree root and they must have lower val
than root in BST. Likewise, nodes of right subtree
traversed [after] root and they must have higher
val than root in BST
"""

# Iterative
class Solution:
    def isValidBST(self, current) -> bool:
        stack = []
        prev = None
        
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
                
            else:
                current = stack.pop()
                if (prev and prev.val >= current.val):
                    return False
                
                prev = current
                current = current.right
                
        return True

# Recursive
class Solution:
    def isValidBST(self, current):
        return self.BSTUtil(current, float('-inf'), float('inf'))
    
    def BSTUtil(self, current, lo, hi):
        if not current:
            return True
        
        if current.val <= lo:
            return False
        
        if current.val >= hi:
            return False
        
        # For left subtree of current of which current is on right subtree of
        # some ancestor, ensure left subtree is lowerBound by ancestor's val
        # For upper bound of left subtree, use parent/current's

        # For right subtree of current of which current is on left subtree
        # of ancestor, ensure right subtree is upper by ancestor's val
        # For lower bound of right subtree, use parent/current's
        return self.BSTUtil(current.left, lo, current.val) and self.BSTUtil(current.right, current.val, hi)
    
    