# Left, Right, Node

class Solution:
    def postorderTraversal(self, current: Optional[TreeNode]) -> List[int]:
        l, stack = [], []
        prev = None
        
        while (current or stack):

            # First task: go as far left as possible down
            if current:
                stack.append(current)
                current = current.left
                
            else:

                # Backtrack up one, then try head down right child
                # If right child does not exist, or we backtracked
                # from right child immediately last step,
                # (making prev == current.right), record current,
                # set prev = current for next iteration, then
                # continue backtracking.
                
                # Note: Only pop stack if need to backtrack
                current = stack[-1]
                if (not current.right or prev == current.right):
                    l.append(current.val)
                    stack.pop()
                    prev = current
                    current = None
                else:
                     current = current.right
                        
        return l