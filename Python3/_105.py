"""Preorder -> (Node, Left, Right); Inorder -> (Left, Node, Right)

preorder[0] must be root. Get its inorder index, create root 
node, split along that index into lower/left and higher/right 
ranges. For subtree, its range in inorder has same length as
match in preorder, except with nodes in different order.
preorder[0 + 1] to be root of its left subtree. Repeat process:
preorder[1 + 1] to be root of left subtree of preorder[1]
"""

class Solution:
    def buildTree(self, preorder, inorder):
        def toTree(preorder, start, end):
            if end < start:
                return None
            
            nonlocal preI
            
            val = preorder[preI]
            inI = valToInI[val]
            preI += 1
            
            return TreeNode(val, toTree(preorder, start, inI - 1),
                           toTree(preorder, inI + 1, end))
            
        valToInI = {}
        for (inI, val) in enumerate(inorder):
            valToInI[val] = inI 
            
        preI = 0
        return toTree(preorder, 0, len(preorder) - 1)
        
        