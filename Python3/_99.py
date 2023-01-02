"""
Inorder traversal of BST gives sorted list. BST with
two nodes swapped and out of order gives sorted list 
from low to high with two values swapped. To identify
those needing to be swapped back, traverse from
either end and get first elems failing to respect
order. "Reverse inorder" is (Right, Node, Left)
"""

class Solution:
    def recoverTree(self, current):
        
        # n1 : With inorder, first node misplaced
        # n2 : With reverse inorder, first node misplaced
        
        n1 = self.getInorderViolator(current)
        n2 = self.getInorderViolator(current, False)
        n1.val, n2.val = n2.val, n1.val
        
    # not regular: Reverse inorder -> (Right, Node, Left)
    def getInorderViolator(self, current, regular = True):
        stack = []
        prev = None
        
        while current or stack:
            if current:
                stack.append(current)
                current = current.left if regular else current.right
                
            else:
                current = stack.pop()
                if prev:
                    if prev.val == current.val or \
                    (regular and prev.val > current.val) or \
                    (not regular and prev.val < current.val):
                        return prev
                        
                prev = current
                current = current.right if regular else current.left

        