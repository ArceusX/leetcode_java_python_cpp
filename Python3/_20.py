class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if stack:
                    popped = stack.pop()
                    # Matched incorrectly
                    if ((popped == '(' and char != ')') or 
                       (popped == '[' and char != ']') or
                       (popped == '{' and char != '}')):
                        return False

                # Not matched at all
                else:
                    return False

        # For True: either s is empty or all open-token properly closed
        return not s or not stack
                

        