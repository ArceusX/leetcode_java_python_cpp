class Solution:
    def isValid(self, s: str) -> bool:
        received = []

        for char in s:
            if char in ['(', '{', '[']:
                received.append(char)
            else:
                if received:
                    popped = received.pop()
                    if ((popped == '(' and char != ')') or 
                       (popped == '[' and char != ']') or
                       (popped == '{' and char != '}')):
                        return False

                    else:
                        return False

        return not received or not s
                

        