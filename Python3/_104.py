# Iterative
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        Max = 0
        q = deque([root, None])
        
        while q:
            current = q.popleft()
            
            if current:
                if current.left: 
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                
            else:
                Max += 1
                if q:
                    q.append(None)
                    
        return Max
                
# Recursive
class Solution:
    def maxDepth(self, current):
        if not current:
            return 0
        
        return max(self.maxDepth(current.left), self.maxDepth(current.right)) + 1
        
            
        