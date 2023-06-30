"""Dynamic Programming: 
   str is "valid" if it is splittable into "valid" substr and word
   in wordDict. Anchoring i, sliding j given (j < i) to 0, if s[j:i]
   is in wordDict, str inherits validity of its substr str[0:j]
   If str[0:j] was earlier marked valid, str[0:i] will also be valid 
"""
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        isValid = [False for _ in range(len(s) + 1)]

        # To affirm s[0:i] is splittable into s[0:0] and s[0:i]
        # and if s[0:i] is in wordDict, s[0:i] should be marked
        # true and for that, isValid[0] needs to be already true
        isValid[0] = True
        
        # Flag early-exit of iteration i if length of s[j:i] 
        # exceeds maxLen of any word in wordDict
        maxLen = max(len(w) for w in wordDict)
        
        # i is window-end. This outer-loop shifts window-end right   
        for i in range(1, len(s) + 1):

            # j is window-start. -1 because i starts count at 1
            j = i - 1

            # Stop slide once end reached or if length of s[j:i] 
            # exceeds maxLen of any word that exists in wordDict
            while (j >= 0 and maxLen >= (i - j)):

                # Check for split of s[0:i] into s[0:j] and s[j:i],
                # if s[0:j] can itself be splitted (marked so 
                # earlier) and if s[j:i] is word within wordDict
                isValid[i] = isValid[j] and (s[j:i] in wordDict)
                
                # Need only 1 pair of s[0:j] and s[j:i]
                if isValid[i]: break

                j -= 1 #Shift window-start left 1
                
        return isValid[-1] # Return if entire str is splittable
        
        