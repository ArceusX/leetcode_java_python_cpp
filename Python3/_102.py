"""
Use dummy elem (None) to indicate end of current
level, then add dummy for next level. Level-order 
requires breadth-first, which requires queue
"""

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        li, levelLi, q = [], [], deque([root, None])
        while q:
            current = q.popleft()

            # End of current level, prepare for next
            # level if there are remaining nodes
            if not current:
                if q:
                    q.append(None)
                    
                li.append(levelLi)
                levelLi = []
                continue
                
            levelLi.append(current.val)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        
        return li