class Solution:
    def isValid(self, s: str) -> bool:
        toClose = []

        for char in s:
            if char in ['(', '{', '[']:
                toClose.append(char)
                continue
                
            if toClose:
                popped = toClose.pop()
                # Matched incorrectly: invalid
                if ((popped == '(' and char != ')') or 
                    (popped == '[' and char != ']') or
                    (popped == '{' and char != '}')):
                    return False

            else: # Close-token left hanging: invalid
                return False

        # Check all found open-tokens are closed
        return not toClose
                

        